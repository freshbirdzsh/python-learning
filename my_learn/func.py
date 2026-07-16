"""
写一个计算BMI的函数，函数名为 calculate_BMI。

可以计算任意体重和身高的BMI值

执行过程中打印一句话，"您的BMI分类为：xx"

返回计算出的BMI值

BMI = 体重 / (身高  2)

BMI分类
偏瘦：BMI <= 18.5
正常：18.5 < BMI <= 25
偏胖：25 < BMI <= 30
肥胖：BMI > 30
"""


def calculate_BMI(weight, height):
    bmi = weight / (height ** 2)

    # 修正了打印的文本，严格对应题目要求的“您的BMI分类为：xx”
    if bmi <= 18.5:
        print("您的BMI分类为：偏瘦")
    elif bmi <= 25:
        print("您的BMI分类为：正常")
    elif bmi <= 30:
        print("您的BMI分类为：偏胖")
    else:
        print("您的BMI分类为：肥胖")

    return bmi


# 第一个参数传体重(62.5kg)，第二个参数传身高(1.7m)
result = calculate_BMI(62.5, 1.7)

# 顺便把返回的 bmi 值打印出来看看 f_string方法
print(f"实际算出的BMI值为：{result:.2f}")