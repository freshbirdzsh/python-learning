print("hello")

#连接
print("hello"+' world'+"!")

#三引号表示把下一行当成换行
print('''我
是
大
帅
哥
''')

import math
print(math.log2(8))

a=-1
b=-2
c=3
print((-b+math.sqrt(b**2-4*a*c))/2*a)
print((-b-math.sqrt(b**2-4*a*c))/2*a)

'''
多行
注释
'''
#会打印两行空行
#print("\n")
print()

#python数据类型
'''
字符串，整型，浮点型，空值，布尔值
'''
s="hello world"
s_len=len(s)
print(s_len)
index=s_len-1
print(s[0])
print(s[index])

b1=True
b2=False
print(b1,b2)

#空值类型
n=None
print(n,n)

#type函数
print(type(s))

#计算BMI
#input的默认返回值是 字符串
# user_weight=float(input("请输入你的体重(单位：kg): "))
# user_height=float(input("请输入你的身高(单位：m ): "))
#
# result=user_weight/user_height**2
# print("您的BMI值是"+str(result))

#if-else
# grade=int(input("您的成绩是："))
# if grade>=90:
#     if grade>=95:
#         print("非常优秀")
#     else:
#         print("优秀")
# elif grade>=80:
#     print("合格")
# else:
#     print("一般")

#逻辑运算符 and or not
#优先级：not > and > or
print((5>3)and(4>3))

#列表
# shopping_list=[]
# shopping_list.append("键盘")
# shopping_list.append("音响")
# shopping_list.remove("音响")
# shopping_list.append("电竞椅")
# shopping_list.append("鼠标")
# print(shopping_list)
# shopping_list[len(shopping_list)-1]="显示器"
# print(shopping_list)
#
# price=[799,800,200,1200]
# min_price=min(price)
# max_price=max(price)
# print(min_price,max_price)
# print(sorted(price))

#字符串（str）是“不可变对象”（Immutable）
# s="hello"
# s[0]="H"
# print(s)

s = "hello"
s = s.capitalize()  # 生成了一个全新的字符串 "Hello"，并重新赋给 s
print(s)  # 输出: Hello

s = "hello"
# s[0] 是 'h'，s[1:] 是 'ello'
s = "H" + s[1:]
print(s)  # 输出: Hello

s = "hello"
s_list = list(s)    # 变成 ['h', 'e', 'l', 'l', 'o']
s_list[0] = "H"     # 列表支持直接修改：['H', 'e', 'l', 'l', 'o']
s = "".join(s_list) # 拼回字符串
#join() 的核心作用就是把一个列表（或者任何可迭代对象）里的所有字符串元素，用“”连接（拼接）成一个完整的字符串
print(s)  # 输出: Hello
