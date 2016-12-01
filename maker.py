#*-- coding=utf-8 --
import Image
import sys
usage = u"""用法 : python maker.py 白背景时图片 黑背景时图片 输出文件 使用方法(1 or 2)\n示例 : python maker.py a.jpg b.jpg output.png 1\n两种方法生成效果不同"""


def oneway():
    bright = Image.open(sys.argv[2]).convert("LA")
    dark = Image.open(sys.argv[1]).convert("LA")
    dark = dark.resize(bright.size,Image.ANTIALIAS)
    pixel = dark.load()
    for i in range(dark.size[0]):
        for j in range(dark.size[1]):
            t = pixel[i,j]
            pixel[i,j]=(t[0],0 if t[0]>130 else 130-t[0])
    pixel = bright.load()
    for i in range(bright.size[0]):
        for j in range(bright.size[1]):
            t = pixel[i,j]
            pixel[i,j]=(t[0],0 if t[0]<40 else t[0]/3)
    l,a = bright.split()
    dark.paste(bright,bright.getbbox(),mask=a)
    dark.save(sys.argv[3],"png")


def anotherway():
    a = Image.open(sys.argv[1])
    b = Image.open(sys.argv[2])
    b = b.resize(a.size,Image.ANTIALIAS)
    a = a.convert("1")
    b = b.convert("1")
    output = Image.new("LA",a.size)
    pixel = output.load()
    for i in range(output.size[0]):
        for j in range(output.size[1]):
            if a.getpixel((i,j))==255 and b.getpixel((i,j))==255:
                pixel[i,j]=(128,255)
            elif a.getpixel((i,j))==255 and b.getpixel((i,j))==0:
                pixel[i,j]=(0,128)
            elif a.getpixel((i, j)) == 0 and b.getpixel((i, j)) == 255:
                pixel[i,j]=(255,128)
            elif a.getpixel((i, j)) == 0 and b.getpixel((i, j)) == 0:
                pixel[i,j]=(128,0)
    output.save(sys.argv[3],"png")


if __name__ == '__main__':
    if len(sys.argv)<4:
        print usage
        exit()
    elif len(sys.argv)==4:
        anotherway()
        print u"成功生成"
    else:
        if sys.argv[4]==1:
            anotherway()
        elif sys.argv[4]==2:
            oneway()
        else:
            print "wrong"