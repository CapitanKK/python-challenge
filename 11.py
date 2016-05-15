from PIL import Image

image = Image.open("cave.jpg")
result = Image.new("RGB", (320, 240))

for x in range(640):
    for y in range(480):
        if x % 2 == 1 and y % 2 == 1:
            result.putpixel((x >> 1, y >> 1), image.getpixel((x, y)))

result.save("result.jpg")