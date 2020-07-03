from PIL import Image

img = Image.open(r'C:\Users\KIIT\Documents\bROI_29.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(r'C:\Users\KIIT\Documents\tROI_29.png')
