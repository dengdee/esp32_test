from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn
import os
import wave
import json
from vosk import Model, KaldiRecognizer

# 初始化 FastAPI
app = FastAPI()

@app.get("/test")
async def test():
    return PlainTextResponse("OK")

# 設定上傳資料夾
uploads = "uploads"
os.makedirs(uploads, exist_ok=True)

# 載入 Vosk 模型（請先下載相應語言的模型）
# 例如中文模型: vosk-model-small-cn-0.22
# 英文模型: vosk-model-small-en-us-0.15
MODEL_PATH = "vosk-model-small-cn-0.22"
if not os.path.exists(MODEL_PATH):
    raise RuntimeError("❌ 找不到模型資料夾，請先下載 Vosk 模型並放在相同目錄中。")

model = Model(MODEL_PATH)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = os.path.join(uploads, file.filename)
    
    # 儲存音檔
    with open(save_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    print(f"✅ File saved: {save_path} ({len(content)} bytes)")
    
    # 進行語音辨識
    try:
        wf = wave.open(save_path, "rb")
    except Exception as e:
        return JSONResponse({"error": f"無法打開音檔: {e}"}, status_code=400)

    # 檢查音檔格式
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000]:
        return JSONResponse({
            "error": "音檔格式需為 16-bit PCM mono，取樣率 8k 或 16k。"
        }, status_code=400)

    rec = KaldiRecognizer(model, wf.getframerate())
    result_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            result_text += part_result.get("text", "") + " "

    final_result = json.loads(rec.FinalResult())
    result_text += final_result.get("text", "")

    wf.close()

    print("🗣️ 辨識結果:", result_text.strip())

    return JSONResponse({
        "status": "ok",
        "filename": file.filename,
        "text": result_text.strip()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
