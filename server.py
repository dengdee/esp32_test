from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn
import os

app = FastAPI()

# 建立 uploads 資料夾（若不存在）
os.makedirs("uploads", exist_ok=True)

@app.get("/test")
async def test():
    return PlainTextResponse("OK")

@app.post("/upload_data")
async def upload_data(value: float = Form(...)):
    print(f"Received value: {value}")
    return JSONResponse(content={"status": "ok", "received": value})

@app.post("/upload_file")
async def upload_file(file: UploadFile):
    content = await file.read()
    filename = file.filename
    with open(f"uploads/{filename}", "wb") as f:
        f.write(content)
    print(f"Saved file: {filename}, size: {len(content)} bytes")
    return {"status": "ok", "filename": filename}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



# pip install fastapi uvicorn
# pip install python-multipart
# mkdir uploads
# python server.py
