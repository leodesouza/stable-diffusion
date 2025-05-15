from datasets import load_dataset
from PIL import Image

# Load first 10,000 images from training set
dataset = load_dataset("imagenet-1k", split="train[:5000]")

# Save them to disk (optional)
for i, example in enumerate(dataset):
    image = example['image']  # This is a PIL.Image
    image.save(f"/home/swf_developer/storage/attack/clean_images/img_{i:05d}.jpg")
