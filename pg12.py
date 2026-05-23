import os
# pyrefly: ignore [missing-import]
from PIL import Image, ImageFilter

INPUT_FOLDER="input_images"
OUTPUT_FOLDER="output_images"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_image(image_name):
    try:
        input_path = os.path.join(INPUT_FOLDER, image_name) 
        output_path = os.path.join(OUTPUT_FOLDER, image_name)

        img = Image.open(input_path) 

        img = img.resize((400, 400))
        img = img.filter(ImageFilter.DETAIL)
        img = img.convert("L")
        img = img.rotate(90)

        img.save(output_path) # img.save()
        print(f"Process {image_name}")

    except Exception as e:
        print(f"Error processing {image_name}: {e}")

def main():
    print("Image processing Lab")
    images = [img for img in os.listdir(INPUT_FOLDER) if img.endswith((".jpg", ".png", ".jpeg"))]

    if not images:
        print("no images")
        return
    
    print("Images found: ", images)

    for  image in images:
        process_image(image)
    
if __name__ == "__main__":
    main()
