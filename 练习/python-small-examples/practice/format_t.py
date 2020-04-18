# str.format() 格式化数字
print('{:.2f}'.format(3.1415926))   # 3.14  保留小数点后两位
print('{:+.2f}'.format(3.1415926))  # +3.14 带符号保留小数点后两位
print('{:+.2f}'.format(-1))         # -1.00 带符号保留小数点后两位
print('{:.0f}'.format(3.1415926))   # 3  不带小数
print('{:.0f}'.format(2.71828))     # 3  不带小数
print('{:2>3d}'.format(5))          # 225 数字补全 (填充左边, 宽度为3)
print('{:5<4d}'.format(10))         # 1055 数字补全 (填充右边, 宽度为4)
print('{:,}'.format(10456123))      # 10,456,123  以逗号分隔的数字格式
print('{:.3%}'.format(0.456789))    # 45.679%  百分比格式
print('{:.2e}'.format(123456789))   # 1.23e+08  指数记法
print('{:>10d}'.format(123))        # '       123' 右对齐 (默认, 宽度为10)
print('{:<10d}'.format(123))        # '123       ' 左对齐 (宽度为10)
print('{:^10d}'.format(123))        # '   123    ' 中间对齐 (宽度为10)

