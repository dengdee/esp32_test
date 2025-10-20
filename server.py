from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn
import os

app = FastAPI()

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
    os.makedirs("uploads", exist_ok=True)
    with open(f"uploads/{filename}", "wb") as f:
        f.write(content)
    return {"status": "ok", "filename": filename}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
