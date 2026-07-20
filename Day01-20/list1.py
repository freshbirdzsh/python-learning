items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]
items4 = list(range(1, 10))
items5 = list('hello')
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']

'''
列表的运算
'''
#连接运算
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

#重复运算
print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']

#逻辑运算
print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False

'''
索引运算
需要说明的是，[]的元素位置可以是0到N - 1的整数，
也可以是-1到-N的整数，分别称为正向索引和反向索引，
其中N代表列表元素的个数。
对于正向索引，[0]可以访问列表中的第一个元素，[N - 1]可以访问最后一个元素；
对于反向索引，[-1]可以访问列表中的最后一个元素，[-N]可以访问第一个元素
'''
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon
items8[2] = 'durian'
print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-5])  # 'apple'
print(items8[-4])  # 'waxberry'
print(items8[-1])  # watermelon
items8[-4] = 'strawberry'
print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']

"""
切片运算。切片运算是形如[start:end:stride]的运算符，
其中start代表访问列表元素的起始位置，end代表访问列表元素的终止位置（终止位置的元素无法访问），
而stride则代表了跨度，简单的说就是位置的增量，比如我们访问的第一个元素在start位置，
那么第二个元素就在start + stride位置，当然start + stride要小于end。
我们给上面的代码增加下面的语句，来使用切片运算符访问列表元素。
"""
print(items8[1:3:1])     # ['strawberry', 'durian']
print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2:1])   # ['strawberry', 'durian']
print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
'''
如果start值等于0，那么在使用切片运算符时可以将其省略；
如果end值等于N，N代表列表元素的个数，那么在使用切片运算符时可以将其省略；
如果stride值等于1，那么在使用切片运算符时也可以将其省略
'''
print(items8[1:3])     # ['strawberry', 'durian']
print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
print(items8[::2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2])   # ['strawberry', 'durian']
print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']

#通过切片运算修改元素
items8[1:3] = ['x', 'o']
print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']

#关系运算
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True 比较规则，按元素比依次较
print(nums2 >= nums3)  # False

'''
元素遍历
'''
languages = ['Python', 'Java', 'C++', 'Kotlin']
#方法一：在循环结构中通过索引运算，遍历列表元素。
for index in range(len(languages)):
    print(languages[index])
#方法二：在循环结构中直接遍历列表元素。
for language in languages:
    print(language)

"""
将一颗色子掷6000次，统计每种点数出现的次数
"""
import random

counters = [0] * 6
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# 输出每种点数出现的次数
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')
