'''
Set (集合)
无序性：一个集合中，每个元素的地位都是相同的，元素之间是无序的。
互异性：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次。
确定性：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合，二者必居其一，不允许有模棱两可的情况出现。
Python 程序中的集合跟数学上的集合没有什么本质区别，需要强调的是上面所说的无序性和互异性。
无序性说明集合中的元素并不像列中的元素那样存在某种次序，可以通过索引运算就能访问任意元素，集合并不支持索引运算。
另外，集合的互异性决定了集合中不能有重复元素，这一点也是集合区别于列表的地方，我们无法将重复的元素添加到一个集合中。
集合类型必然是支持in和not in成员运算的，这样就可以确定一个元素是否属于集合，也就是上面所说的集合的确定性。
集合的成员运算在性能上要优于列表的成员运算
'''
set1={1, 2, 3, 4, 5}
print(set1)  # {1, 2, 3, 4, 5}

set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)

set3 = set('hello') #l不会重复存储，只会存储一个l
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

set6=set(num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0)
print(set6)

#遍历(体会无序性)
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elem in set1:
    print(elem)
print()
for _ in range(len(set1)):
    print(set1.pop())# pop()方法会随机删除集合中的一个元素，并返回该元素的值

#集合的运算
set1 = {11, 12, 13, 14, 15}
print(10 in set1)      # False 
print(15 in set1)      # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}

# 并集
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}

# 对称差
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
# set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set1)  # {3, 6}
set2 -= set1
# set2.difference_update(set1)
print(set2)  # {2, 4}

set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

# 比较运算（判断子集）
print(set1 < set2)   # True
print(set1 <= set2)  # True
print(set2 < set3)   # False
print(set2 <= set3)  # True
print(set2 > set1)   # True
print(set2 == set3)  # True

print(set1.issubset(set2))    # True
print(set2.issuperset(set1))  # True

set1 = {1, 10, 100}

# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}

# 清空元素
set1.clear()
print(set1)  # set()

#isdisjoint的方法可以判断两个集合有没有相同的元素，如果没有相同元素，该方法返回True，否则该方法返回False
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True

#不可变集合
'''
set跟frozenset的区别就如同list跟tuple的区别，
frozenset由于是不可变类型，能够计算出哈希码，因此它可以作为set中的元素
'''
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False