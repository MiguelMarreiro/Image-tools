from PIL import Image, ImageDraw, ImageFilter
from tkinter import filedialog

# Open the image file
file_path = filedialog.askopenfilename()

# Print the selected file path
if file_path:
    print(f"Selected file: {file_path}")
else:
    print("No file selected.")

image_format = file_path.split(".")[1]
image_name = file_path.split("/")[-1].split(".")[0]

im = Image.open(file_path)

# Convert RGBA to RGB
if im.mode == 'RGBA':
    # Create a new background (white) image
    background = Image.new("RGB", im.size, (255, 255, 255))
    # Paste the original image on the background
    background.paste(im, mask=im.split()[3])  # 3 is the alpha channel
    im = background

# # Display the image
# im.show()

# Convert and save the image to JPEG format
jpeg_image_path = fr"output/{image_name}.jpeg"
im.save(jpeg_image_path, 'JPEG', quality=90)