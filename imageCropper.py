from PIL import Image
import glob

imagesPath = "C:/Users/Lukas/Documents/Rainmeter/Skins/Honeycomb/@Resources/Images/*.png"

def crop(image_path, coords):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(image_path)

for image in glob.glob(imagesPath):
    crop(image, (66, 24, 512-66, 512-24))