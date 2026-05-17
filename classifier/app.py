from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

model_id = "chriamue/bird-species-classifier"

processor = AutoImageProcessor.from_pretrained(model_id)
model = AutoModelForImageClassification.from_pretrained(model_id)

#image = Image.open("/workspaces/watergun/20260319_173350.jpg")
image = Image.open("/workspaces/watergun/20260325_063841.jpg")

inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits
predicted_class_id = logits.argmax(dim=-1).item()

print("Class ID:", predicted_class_id)