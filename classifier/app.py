from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
from pathlib import Path
import argparse

def classifyImage(image: int | str | Path):
    if isinstance(image, int):
        image_dir = Path("/workspace/img/doves")
        images = sorted(image_dir.glob("*.jpg"))

        if image < 0 or image >= len(images):
            raise IndexError(
                f"Image index {image} is out of range. "
                f"There are {len(images)} images."
            )

        image_path = images[image]

    else:
        image_path = Path(image)
        if not image_path.exists():
            raise FileNotFoundError(image_path)

    print(f"Using image: {image_path}")

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("index", type=int)
    args = parser.parse_args()

    classifyImage(args.index)