from PIL import Image

img = Image.open('oxygen.png')
rgb_im = img.convert('RGB')
for x in range(3, 608, 7):
    r, g, b = rgb_im.getpixel((x, 48))
    print(chr(r), end='')

print()
a = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for x in a:
    print(chr(x), end='')