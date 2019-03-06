from PIL import Image, ImageDraw, ImageFont


def main():
    # 打开图片，获取图片宽度和高度
    im = Image.open('avatar.jpg')
    w, h = im.size
    
    # 创建Draw对象
    draw = ImageDraw.Draw(im)
    # 导入字体创建Font对象
    font = ImageFont.truetype('Arial.ttf', 36)
    # 图片左上角为(0, 0), 绘制文本为'99+', 字体为导入的字体，填充颜色为红色
    draw.text((w*0.90, h*0.01),'99+', font=font,fill='#FF0000')

    im.show()

if __name__ == "__main__":
    main()