'''
文件读写
'''
from pathlib import Path

# 获取当前脚本所在的目录
script_dir = Path(__file__).parent

# with open(script_dir/'致橡树.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

file = open(script_dir/'致橡树.txt', 'r', encoding='utf-8')
for line in file:
    print(line, end='')
file.close()

file = open(script_dir/'致橡树.txt', 'r', encoding='utf-8')
#readlines方法将文件按行读取到一个列表容器中
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()

file = open(script_dir/'致橡树.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()

'''
异常处理
'''
file = None
try:
    file = open(script_dir/'致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally:
    if file:
        file.close()


class InputError(ValueError):
    """自定义异常类型"""
    pass


def fac(num):
    """求阶乘"""
    if num < 0:
        #raise可以主动抛异常
        raise InputError('只能计算非负整数的阶乘')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

flag = True
while flag:
    num = int(input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as err:
        print(err)

'''
上下文管理语法
对于open函数返回的文件对象，还可以使用with上下文管理器语法在文件操作完成后自动执行文件对象的close方法，这样可以让代码变得更加简单优雅，因为不需要再写finally代码块来执行关闭文件释放资源的操作。
需要提醒大家的是，并不是所有的对象都可以放在with上下文语法中，只有符合上下文管理器协议（有__enter__和__exit__魔术方法）的对象才能使用这种语法，Python 标准库中的contextlib模块也提供了对with上下文语法的支持
'''
try:
    with open(script_dir/'致橡树.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')


'''
读取二进制文件

'''
# try:
#     with open(script_dir/'guido.jpg', 'rb') as file1:
#         data = file1.read()
#     with open(script_dir/'吉多.jpg', 'wb') as file2:
#         file2.write(data)
# except FileNotFoundError:
#     print('指定的文件无法打开.')
# except IOError:
#     print('读写文件时出现错误.')
# print('程序执行结束.')

try:
    with open(script_dir/'guido.jpg', 'rb') as file1, open(script_dir/'吉多.jpg', 'wb') as file2:
        #指定size:512字节
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read(512)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')