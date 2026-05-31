from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "index",
    type=int,
    help="Index of the image to classify"
)
args = parser.parse_args()

# Get all images from the directory
image_dir = Path("/workspace/img/doves")
images = sorted(image_dir.glob("*.jpg"))

if args.index < 0 or args.index >= len(images):
    raise IndexError(
        f"Image index {args.index} is out of range. "
        f"There are {len(images)} images."
    )

image_path = images[args.index]

print(f"Using image #{args.index}: {image_path}")

model_id = "chriamue/bird-species-classifier"

processor = AutoImageProcessor.from_pretrained(model_id)
model = AutoModelForImageClassification.from_pretrained(model_id)

image = Image.open(image_path)

inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits
probs = torch.nn.functional.softmax(logits, dim=-1)[0]
top5_probs, top5_ids = torch.topk(probs, 5)

print("Top 5 predictions:")
for score, class_id in zip(top5_probs, top5_ids):
    class_id = class_id.item()
    label = model.config.id2label[class_id]
    print(f"{class_id:3d}: {label:30s} {score.item():.2%}")