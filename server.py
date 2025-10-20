from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn
import os

app = FastAPI()

@app.get("/test")
async def test():
    return PlainTextResponse("OK")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = os.path.join(uploads, file.filename)
    
    with open(save_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    print(f"✅ File saved: {save_path} ({len(content)} bytes)")
    return {"status": "ok", "filename": file.filename, "size": len(content)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
