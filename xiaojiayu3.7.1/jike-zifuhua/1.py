# import PIL
from PIL import Image
img = Image.open("lem.jpg")
out = img.convert("L")
# out.show()

width,height = out.size

out = out.resize((int(width * 0.3),int(height * 0.3 * 0.6)))
width,height = out.size
print(width,height)


asciis = "@%#*+=-:. "
text = ""
for i in range(height):
    for j in range(width):
        gray = out.getpixel((j,i))
        text += asciis[int(gray / 255 * 9)]  # 根据灰度值选择不同复杂度的 ASCII 字符
    text += '\n'

with open('lem.txt',"w") as f:
    f.write(text)