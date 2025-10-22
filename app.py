
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from blip_captioner import BLIPCaptioner

app = FastAPI(title="BLIP Captioning Service")
captioner = BLIPCaptioner()

@app.post("/caption")
async def generate_caption(image: UploadFile = File(...)):
    contents = await image.read()
    caption = captioner.generate_caption(contents)
    return JSONResponse({"caption": caption})

@app.get("/")
def root():
    return {"message": "BLIP Captioning Service is running."}
