f = open('evil2.gfx', 'rb')
data = f.read()
f.close()

for i in range(5):
    f = open("img" + str(i + 1), 'wb')
    f.write(data[i::5])
    f.close()