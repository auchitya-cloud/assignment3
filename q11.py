import os
import threading
from google_images_download import google_images_download
from PIL import Image

def download_images(keyword, num_images, output_folder):
    response = google_images_download.googleimagesdownload()

    arguments = {
        "keywords": keyword,
        "limit": num_images,
        "print_urls": True,
        "output_directory": output_folder
    }

    try:
        paths = response.download(arguments)
        print("Images downloaded successfully!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def rescale_image(image_path, output_folder, scale_percent):
    try:
        img = Image.open(image_path)
        width, height = img.size
        new_width = int(width * scale_percent / 100)
        new_height = int(height * scale_percent / 100)
        resized_img = img.resize((new_width, new_height))
        new_image_path = os.path.join(output_folder, os.path.basename(image_path))
        resized_img.save(new_image_path)
        print(f"Image '{os.path.basename(image_path)}' rescaled to 50% and saved as '{os.path.basename(new_image_path)}'")
    except Exception as e:
        print(f"Error occurred while rescaling image: {str(e)}")

def process_image(image_path, output_folder, scale_percent):
    rescale_image(image_path, output_folder, scale_percent)
    os.remove(image_path)

if __name__ == "__main__":
    keyword = "Dog"
    num_images = 500
    output_folder = "images"
    scale_percent = 50
    num_threads = 10

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create a list to hold the thread objects
    threads = []

    download_images(keyword, num_images, output_folder)

    # Get a list of all image files in the 'images' folder
    image_files = [f for f in os.listdir(output_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        image_path = os.path.join(output_folder, image_file)

        # Create a thread for each image and start it
        thread = threading.Thread(target=process_image, args=(image_path, output_folder, scale_percent))
        thread.start()
        threads.append(thread)

        # Wait for a certain number of threads to finish before starting the next batch
        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []

    # Wait for any remaining threads to finish
    for thread in threads:
        thread.join()

    print("All images downloaded and rescaled successfully.")
