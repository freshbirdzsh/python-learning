"""
算术运算符
"""
print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
#除法需要额外注意
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241

"""
算术运算的优先级
"""
print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
#幂运算符优先级高
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625

"""
赋值运算符和复合赋值运算符
"""
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么?--> 195

"""
海象运算符
"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符
# Python 3.8 中引入了一个新的赋值运算符:=，我们称之为海象运算符。
# 海象运算符也是将运算符右侧的值赋值给左边的变量，与赋值运算符不同的是，运算符右侧的值也是整个表达式的值。
print((a := 10))  # 10
print(a)          # 10

"""
比较运算符和逻辑运算符的使用
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False

"""
将华氏温度转换为摄氏温度
"""
f=float(input('请输入华氏温度: '))
c=(f-32)/1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
# str.format() 写法
#print("{:.1f}华氏度 = {:.1f}摄氏度".format(f, c))
# % 旧式格式化写法
#print("%.1f华氏度 = %.1f摄氏度" % (f, c))

'''
计算圆的周长和面积
'''
r=float(input("请输入圆的半径:"))
l=2*3.1416*r
s=3.1416*r**2
print(f"圆的周长:{l:.2f}")
print("圆的面积:%.2f" %s)
#print("圆的周长:{:.2f}".format(l))

'''
输入半径计算圆的周长和面积
'''

import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}') 
print(f'面积: {area:.2f}')
#python3.8 之后可以使用 f-string 的等号语法来输出变量名和变量值
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
print(f'{area = :.2f}')       # 输出：area = 95.03

"""
输入年份，闰年输出True，平年输出False

"""
year=int(input("请输入年份:"))
is_leap_year=((year%4==0 and year%100!=0)or year%400==0)
print(f"{year}年是闰年吗？{is_leap_year}")

