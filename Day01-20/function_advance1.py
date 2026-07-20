'''
我们回到之前讲过的一个例子，设计一个函数，传入任意多个参数，对其中int类型或float类型的元素实现求和操作。
我们对之前的代码稍作调整，让整个代码更加紧凑一些，如下所示。
'''

def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result

#实现更多的甚至是自定义的二元运算
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

# def add(x, y):
#     return x + y


# def mul(x, y):
#     return x * y

# print(calc(0, add, 1, 2, 3, 4, 5))  # 15
# print(calc(1, mul, 1, 2, 3, 4, 5))  # 120 

import operator

print(calc(0, operator.add, 1, 2, 3, 4, 5))  # 15
print(calc(1, operator.mul, 1, 2, 3, 4, 5))  # 120

'''
Python内置高阶函数
filter和map函数就是高阶函数，前者可以实现对序列中元素的过滤，后者可以实现对序列中元素的映射

map(function, iterable):把一个函数作用到可迭代对象的每一个元素上，并返回一个新的迭代器。

filter(function, iterable):根据条件筛选数据。
'''
#例如我们要去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表
def is_even(num):
    return num%2==0

def square(num):
    return num**2

old_nums=[35, 12, 8, 99, 60, 52]
new_nums=list(map(square,filter(is_even,old_nums)))
print(new_nums)

#列表生成式
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = [num ** 2 for num in old_nums if num % 2 == 0]
print(new_nums)  # [144, 64, 3600, 2704]

'''
sorted函数从功能上来讲跟列表的sort方法没有区别，但它会返回排序后的列表对象，
而不是直接修改原来的列表，这一点我们称为函数的 无副作用设计
'''
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']
new_strings = sorted(old_strings, key=len)
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']

'''
Lambda函数
在使用高阶函数的时候，如果作为参数或者返回值的函数本身非常简单，
一行代码就能够完成，也不需要考虑对函数的复用，那么我们可以使用 lambda 函数。
Python 中的 lambda 函数是没有的名字函数，所以很多人也把它叫做匿名函数，
lambda 函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。
'''
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

import operator
import functools
#functools Python 标准库中的函数工具模块
#functools.reduce()：对一个序列中的元素进行累计计算
#例如:reduce(f,[a,b,c,d])
#执行类似:f(f(f(a,b),c),d)

#利用lambda实现阶乘
fac=lambda x:functools.reduce(operator.mul,range(2,x+1),1)
#等价于
# def fac(n):
#     result = 1
#     for i in range(2,n+1):
#         result *= i
#     return result

#用一行代码实现判断素数
#all():判断一个可迭代对象里的所有元素是否都为 True。
is_prime=lambda x:all(map(lambda f:x%f,range(2,int(x**0.5)+1)))
# 调用Lambda函数
print(fac(6))        # 720
print(is_prime(37))  # True


'''
偏函数
偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。
在 Python 语言中，我们可以使用functools模块的partial函数来创建偏函数
'''
import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)
#partial函数的第一个参数和返回值都是函数，它将传入的函数处理成一个新的函数返回

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097
