from PIL import Image

image = Image.open("mozart.gif")
rgb_im = image.convert('RGB')
result = Image.new("RGB", (640, 480))
for y in range(480):
    index = -1
    for x in range(640):
        if rgb_im.getpixel((x, y)) == (255, 0, 255) and rgb_im.getpixel((x + 1, y)) == (255, 0, 255):
            index = x
            break
    for x in range(640):
        result.putpixel((x, y), rgb_im.getpixel(((index + x) % 640, y)))

result.save("result.jpg")