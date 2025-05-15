from datasets import load_dataset
from PIL import Image

# Load first 10,000 images from training set
dataset = load_dataset("imagenet-1k", split="train[:5000]")
dataset = dataset.shuffle(seed=42)

# Save them to disk (optional)
for i, example in enumerate(dataset):
    image = example['image']  # This is a PIL.Image
    file_name = f"img_{i:05d}"
    print(f'saving file: {file_name}')
    image.save(f"/home/swf_developer/storage/attack/clean_images/{file_name}.jpg")
