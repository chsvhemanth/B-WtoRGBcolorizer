# utils.py
from PIL import Image
import torch
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.Resize((150, 150)),
    transforms.Grayscale(num_output_channels=1),
    transforms.ToTensor(),
])

def preprocess_image(image_file):
    image = Image.open(image_file).convert("RGB")
    gray = transform(image).unsqueeze(0)
    return gray
