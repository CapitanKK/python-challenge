from PIL import Image

image = Image.open("wire.png")
result = Image.new("RGB", (100, 100))

x = 0
y = 0
d = 1
top = 1
right = 99
bottom = 99
left = 0
for i in range(10000):
    print(i, x, y)
    result.putpixel((x, y), image.getpixel((i, 0)))
    if d == 0 and y == top:
        d = 1
        top += 1
    if d == 1 and x == right:
        d = 2
        right -= 1
    if d == 2 and y == bottom:
        d = 3
        bottom -= 1
    if d == 3 and x == left:
        d = 0
        left += 1
    if d == 0:
        y -= 1
    elif d == 1:
        x += 1
    elif d == 2:
        y += 1
    else:
        x -= 1

result.save("result.jpg")