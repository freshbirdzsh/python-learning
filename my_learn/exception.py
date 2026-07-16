try:
    user_weight = float(input("请输入您的体重（单位：kg）："))
    user_height = float(input("请输入您的身高（单位：m）："))
    user_BMI = user_weight / user_height ** 2

except ValueError:
    print("输入不为合理数字，请重新运行程序，并输入正确的数字。")

except ZeroDivisionError:
    print("身高不能为零，请重新运行程序，并输入正确的数字。")

except Exception:  # 原代码中是匿名的 except:，在规范中通常写为 except Exception: 来捕获其他未知错误
    print("发生了未知错误，请重新运行程序。")

else:
    # 这里原代码使用了用 + 拼接 str 的老方法，推荐改用 f-string 更加优雅：
    print(f"您的BMI值为：{user_BMI}")

finally:
    print("程序结束运行。")