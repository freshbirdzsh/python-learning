#整型
print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数
#浮点型
print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法
#字符串型
print('hello world')  # 单引号
print("hello world")  # 双引号
#布尔型
print(True)   # True
print(False)  # False

"""
使用type函数检查变量的类型
"""
a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

"""
变量的类型转换操作
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串（在可能的情况下）转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码方式。
chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。
"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100
'''
说明：str类型转int类型时可以通过base参数来指定进制，
可以将字符串视为对应进制的整数进行转换。
str类型转成bool类型时，只要字符串有内容，不是''或""，对应的布尔值都是True。
bool类型转int类型时，True会变成1，False会变成0。
在 ASCII 字符集和 Unicode 字符集中， 字符'd'对应的编码都是100。
'''