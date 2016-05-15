import zipfile

file = zipfile.ZipFile('channel.zip')
nothing = 90052

comment = ''
try:
    while nothing:
        with open('6zip/%d.txt' % nothing) as f:
            comment += chr(file.getinfo('%d.txt' % nothing).comment[0])
            s = f.readline()
            nothing = int(s.split()[-1])
finally:
    print(comment)



