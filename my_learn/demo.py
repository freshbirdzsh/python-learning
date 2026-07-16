#循环
#
# temperature_list={"111":"37.2","112":"38.1","113":"39"}
#
# for id,temperature in temperature_list.items():
#     print(id)
#     print(temperature)
#     print()
#
# for tuple in temperature_list.items():
#     print(tuple[0])
#     print(tuple[1])
#     print()
#
# total=0
# for i in range(1,101):
#     total+=i
# print(total)
from functools import total_ordering
from my_unittest import result

#三种循环
# 字典必须是键值对：{"key": "value"}
# 集合只是去重的元素组合：{"A", "B", "C"}
list1=["你","好","吗","兄","弟"]

for char in list1:
    print(char)
for i in range(len(list1)):
    print(list1[i])
i=0
while i<len(list1):
    print(list1[i])
    i+=1

#计算用户多个输入的平均值
print("我是计算平均值的计算器！")
total=0
count=0
user_input=input("请输入数字（输入q视为结束）：")
while user_input!="q":
    total+=float(user_input)
    count+=1
    user_input = input("请输入数字（输入q视为结束）：")
if count==0:
    result=count
else :
    result=total/count
print("您输入的数字平均值为："+str(result))

# 1. 定义一个包含学生姓名和绩点的字典
gpa_dict = {
    "小明": 3.251,
    "小花": 3.869,
    "小李": 2.683,
    "小张": 3.685
}

# 用于累加总绩点，方便后面算平均分
total_gpa = 0

print("--- 开始打印每位同学的绩点 ---")

# 2. 使用 items() 同时循环获取字典的 键(name) 和 值(gpa)
for name, gpa in gpa_dict.items():
    # 使用 f-string 格式化，{gpa:.2f} 表示保留2位小数
    print(f"{name}你好，你的当前绩点为：{gpa:.2f}")
    # 坑里的 :.2f 规则和 f-string 完全一样，只是变量放到了后面
    #print("{0}你好，你的当前绩点为：{1:.2f}".format(name, gpa))
    #print("{}你好，你的当前绩点为：{:.2f}".format(name, gpa)) 默认按顺序

    # 顺便把绩点累加起来
    total_gpa += gpa

print("--------------------------------")

# 3. 计算并打印全班平均绩点
student_count = len(gpa_dict)
average_gpa = total_gpa / student_count

print(f"全班一共 {student_count} 名同学。")
print(f"全班平均绩点为：{average_gpa:.2f}")



