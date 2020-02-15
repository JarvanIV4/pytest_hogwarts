#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 验证码识别.py
# Author: Helen
# Date  : 2020/2/12

import subprocess
from PIL import Image

# # 读取图片
image = Image.open('tess2.jpg')
# # 识别图片里面的字体
# text = pytesseract.image_to_string(image)
# print(text)
#  阈值过滤  (黑色 白色  143以下都黑色  255 白色)
image = image.point(lambda x: 0 if x < 143 else 255)
image.save('abc.png')

# 图片识别
subprocess.call(['tesseract', 'abc.png', 'output'])






