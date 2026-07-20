'''
装饰器
Python 语言中，装饰器是“用一个函数装饰另外一个函数并为其提供额外的能力”的语法现象。
装饰器本身是一个函数，它的参数是被装饰的函数，它的返回值是一个带有装饰功能的函数

一句话理解：装饰器就是在不修改原函数代码的情况下，给函数增加额外功能。
'''

import random
import time


def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    #random.random() 生成一个 0.0 到 1.0 之间的随机浮点数
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

    
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

    
# start = time.time()
# download('MySQL从删库到跑路.avi')
# end = time.time()
# print(f'花费时间: {end - start:.2f}秒')
# start = time.time()
# upload('Python从入门到住院.pdf')
# end = time.time()
# print(f'花费时间: {end - start:.2f}秒')

def record_time(func):

    #Python支持函数的嵌套定义
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result
    
    return wrapper

# download = record_time(download)
# upload = record_time(upload)
# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')

#语法糖
@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

import random
import time

'''
如果在代码的某些地方，我们想去掉装饰器的作用执行原函数，
那么在定义装饰器函数的时候，需要做一点点额外的工作。
Python 标准库functools模块的wraps函数也是一个装饰器，我们将它放在wrapper函数上，
这个装饰器可以帮我们保留被装饰之前的函数，这样在需要取消装饰器时，
可以通过被装饰函数的__wrapped__属性获得被装饰之前的函数。
'''
from functools import wraps


def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# 调用装饰后的函数会记录执行时间
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')

#递归调用
def fac(num):
    if num in (0,1):
        return 1
    return num*fac(num-1)

print(fac(5))

def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 21):
    print(fib1(i))

def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

'''
除此以外，我们还可以使用 Python 标准库中functools模块的lru_cache函数来优化上面的递归代码。
lru_cache函数是一个装饰器函数，我们将其置于上面的函数fib1之上，
它可以缓存该函数的执行结果从而避免在递归调用的过程中产生大量的重复运算，
这样代码的执行性能就有“飞一般”的提升
'''

from functools import lru_cache

@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(i, fib1(i))