from PIL import Image, ImageDraw, ImageFilter


# Open the WebP image file
webp_image_name = "The-God-Machine-Blind-Guardian2"
im = Image.open(f"images/{webp_image_name}.webp")

# Display the image
im.show()

# Convert and save the image to JPEG format
jpeg_image_path = f"output/{webp_image_name}.jpeg"
im.save(jpeg_image_path, 'JPEG', quality=90)