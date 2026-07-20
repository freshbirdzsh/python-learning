import time 

'''
左闭右开
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。'''
# for i in range(10):
#     print("hello")
#     time.sleep(1)

# for _ in range(10):
#     print("hello")
#     time.sleep(1)

total = 0
for i in range(1,101,2):
    total += i
print(total)

"""
从1到100的偶数求和
直接使用内置函数sum()和range()函数
"""
print(sum(range(2, 101, 2)))

"""
从1到100的偶数求和
while循环实现
"""
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(total)

"""
从1到100的偶数求和
break
continue
"""
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total) 

total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)

"""
打印乘法口诀表
嵌套结构
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()

"""
输入一个大于1的正整数判断它是不是素数
"""
num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

    """
输入两个正整数求它们的最大公约数
"""
x = int(input('x = '))
y = int(input('y = '))
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f'最大公约数: {i}')
        break

"""
猜数字小游戏
"""
import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('大一点.')
    elif num > answer:
        print('小一点.')
    else:
        print('猜对了.')
        break
print(f'你一共猜了{counter}次.')
'''
如果事先知道循环结构重复的次数，我们通常使用for循环；
如果循环结构的重复次数不能确定，可以用while循环。
此外，我们可以在循环结构中使用break终止循环，
也可以在循环结构中使用continue关键字让循环结构直接进入下一轮次。
'''