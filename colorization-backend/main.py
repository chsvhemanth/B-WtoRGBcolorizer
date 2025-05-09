from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import torch
from model import ColorAutoEncoder
from utils import preprocess_image
import io
from torchvision.transforms import ToPILImage

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = ColorAutoEncoder()
model.load_state_dict(torch.load("model.pth", map_location=torch.device("cpu")))
model.eval()

@app.post("/colorize_image/")  # Updated the endpoint to match frontend
async def colorize_image(file: UploadFile = File(...)):
    input_tensor = preprocess_image(file.file)
    with torch.no_grad():
        output = model(input_tensor)

    output_image = ToPILImage()(output.squeeze(0))
    buf = io.BytesIO()
    output_image.save(buf, format='PNG')
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")
