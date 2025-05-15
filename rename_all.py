import os


folder_path = '/home/swf_developer/storage/attack/targeted_images/samples/'
start_count = 2347
png_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])


for i, filename in enumerate(png_files):
    new_name = f"{start_count + i:05}.png"  # Format as 5-digit number
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)
    print(f"Renamed '{filename}' to '{new_name}'")
