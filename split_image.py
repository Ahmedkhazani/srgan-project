
import os
from PIL import Image
import tifffile

def split_tif_image(image_path, output_dir, patch_size=250):
    os.makedirs(output_dir, exist_ok=True)

    # Load TIF image using tifffile
    img_array = tifffile.imread(image_path)

    # Convert to PIL Image if necessary
    img = Image.fromarray(img_array).convert('RGB')
    width, height = img.size

    patch_id = 0
    for top in range(0, height, patch_size):
        for left in range(0, width, patch_size):
            right = left + patch_size
            bottom = top + patch_size

            if right <= width and bottom <= height:
                patch = img.crop((left, top, right, bottom))
                patch.save(os.path.join(output_dir, f'patch_{patch_id}.png'))
                patch_id += 1

    print(f"Saved {patch_id} patches to {output_dir}")

# Example usage
if __name__ == "__main__":
    input_path = "data/satellite_hr.tif"
    output_path = "data/patches_250"
    split_tif_image(input_path, output_path, patch_size=250)
