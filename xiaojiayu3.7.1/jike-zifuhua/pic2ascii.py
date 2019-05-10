from PIL import Image

def pic2ascii(pic,asciis,zoom,vscale):
    img = Image.open(pic)
    # 打开图片并转换为灰度模式
    out = img.convert("L")
    # 获取图片的宽度和高度
    width , height = out.size
    # 由于字符的宽度并不会等于高度，所以需要进行调整
    out = out.resize((int(width * zoom),int(height * zoom * vscale)))
    asciis_len = len(asciis)
    text = ""

    for row in range(out.height):
        for col in range(out.width):
            gray = out.getpixel((col,row))
            text += asciis[int(gray / 255 * (asciis_len - 1))]
        text += "\n"

    return text

def exe():
    pic = "3.jpg"
    # 字符表示按“灰度级别”从高到低排序
    asciis =  "@%#*+=-:. "
    # 设置缩放系数
    zoom = 0.5
    # 设置垂直比例系数
    vscale = 0.5
    text = pic2ascii(pic,asciis,zoom,vscale)

    text_name = '%s.txt'%(pic[0:pic.find('.')])
    with open(text_name , 'w') as f:
        f.write(text)

exe()