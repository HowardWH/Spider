# 中文识别

# coding:utf-8
from PIL import Image,ImageEnhance
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
im = Image.open('Image1.png')
#下面为增强部分
enh_con = ImageEnhance.Contrast(im)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
#image_contrasted.show()

#增强亮度
enh_bri = ImageEnhance.Brightness(image_contrasted)
brightness = 1.5
image_brightened = enh_bri.enhance(brightness)
#image_brightened.show()
#增强对比度
enh_col = ImageEnhance.Color(image_brightened)
color = 1.5
image_colored = enh_col.enhance(color)
#image_colored.show()
#增强锐度
enh_sha = ImageEnhance.Sharpness(image_colored)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
#image_sharped.show()

#灰度处理部分
im2=image_sharped.convert("L")
im2.show()
text=pytesseract.image_to_string(im2,lang='chi_sim').strip() #使用image_to_string识别验证码
print(text)