from PIL import Image, ImageDraw, ImageFont

# pip install pillow

#1. Load the image to watermark.
image = Image.open('w1.png')

#2. Create a new image for the 
#  watermark with transparency.
watermark = Image.new('RGBA', image.size,(0,0,0,0))

#3. Create a draw object for the watermark image.
draw = ImageDraw.Draw(watermark)

#4. Load a font for the watermark text.
# Specify the font size for the watermark text.
font_size = 38  # Adjust the font size as needed

#5. Load a font for the watermark text 
# with the specified font size.
# You can replace 'sans.otf' with 
# the path to your font file.
font = ImageFont.truetype('sans.otf', font_size)

# font = ImageFont.load_default() 
#  Use a default built-in font

#6. Specify the watermark text.
watermark_text = "Subscribe @epythonlab"

#7. Calculate the bounding box of 
# the watermark text.
text_bbox = draw.textbbox((0,0), 
                          watermark_text, font=font)

text_wdith = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

#8. Calculate the position to place 
# the watermark text at the center.
img_width, img_height = image.size

x = (img_width - text_wdith) // 2
y = (img_height - text_height) // 2

#9. Specify the fill (font color) for 
# the watermark (semi-transparent black).

fill_color = (0, 0, 0, 128)  # Semi-transparent black

#10. Draw the watermark text on the watermark image.
draw.text((x, y), watermark_text, fill=fill_color)

#11. Create a transparent diagonal watermark image.
rotated_watermark = Image.new('RGBA', image.size, (0,0,0,0))

#12. Rotate the watermark text by 45 
# degrees and paste it onto the transparent image.
rotated_watermark_draw = ImageDraw.Draw(rotated_watermark)
rotated_watermark_draw.text((x, y), 
                            watermark_text,
                            font=font, 
                            fill=fill_color)
rotated_watermark = rotated_watermark.rotate(45, center=(x,y))


#13. Add the watermark to the image.
image.alpha_composite(rotated_watermark)

#14. Save the watermarked image.
image.save('watermarked_image.png', format='png')
