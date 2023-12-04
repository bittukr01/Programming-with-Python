from PIL import Image, ImageDraw, ImageFont

# Create a blank white image with a specified size
width, height = 400, 400
background_color = (255, 255, 255)
image = Image.new("RGB", (width, height), background_color)

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Draw Radha Krishna - you can customize this as you like
# For a basic example, we'll draw two circles and two lines to represent Radha and Krishna
radha_color = (255, 0, 0)  # Red
krishna_color = (0, 0, 255)  # Blue

draw.ellipse([100, 100, 200, 200], fill=radha_color)  # Radha's circle
draw.line((150, 100, 150, 200), fill=radha_color)  # Radha's body

draw.ellipse([250, 100, 350, 200], fill=krishna_color)  # Krishna's circle
draw.line((300, 100, 300, 200), fill=krishna_color)  # Krishna's body

# Save the image
image.save("radha_krishna.png")