class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        #使用字典来存储三科成绩
        self.grades={"语文":0,"数学":0,"英语":0}

    def set_grade(self,subject,grade):
        if subject in self.grades:
            self.grades[subject]=grade
            print(f"成功将{self.name}的{subject}的成绩设置为:{grade}")
        else:
            print(f"设置失败：没有 {subject} 这个科目，目前只支持设置 语文、数学、英语。")

    def print_grades(self):
        print("-" * 30)
        print(f"学生姓名: {self.name}")
        print(f"学生学号: {self.student_id}")
        print("各科成绩如下:")
        for subject, score in self.grades.items():
            print(f"  - {subject}: {score} 分")
        print("-" * 30)

#========测试========
# if __name__ == "__main__":
#     # 1. 创建一个学生实例
#     student1 = Student("张三", "20260101")
#
#     # 打印初始成绩（默认为0）
#     student1.print_grades()
#
#     # 2. 设置该学生某科目的成绩
#     student1.set_grade("语文", 92)
#     student1.set_grade("数学", 98)
#     student1.set_grade("英语", 85)
#
#     # 尝试设置一个不存在的科目（测试容错）
#     student1.set_grade("物理", 100)
#
#     # 3. 打印出该学生的所有科目成绩
#     student1.print_grades()

# ==================== 1. 定义父类 (员工基类) ====================
class Employee:
    def __init__(self, name, id):
        """全职和兼职都有 '姓名 name'、'工号 id' 属性"""
        self.name = name
        self.id = id

    def print_info(self):
        """都具备 '打印信息 print_info'（打印姓名、工号）方法"""
        print(f"员工工号: {self.id} | 员工姓名: {self.name}")

    def calculate_monthly_pay(self):
        """
        全职和兼职都有的方法，但具体计算过程不一样。
        在父类中通常只定义接口，由子类去具体实现（重写）。
        """
        pass


# ==================== 2. 定义子类：全职员工 ====================
class FullTimeEmployee(Employee):  # 括号里写 Employee 表示继承它
    def __init__(self, name, id, monthly_salary):
        # 使用 super() 调用父类的初始化方法，继承 name 和 id
        super().__init__(name, id)
        # 全职特有属性：月薪
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        """全职员工月薪计算逻辑：直接返回月薪"""
        return self.monthly_salary


# ==================== 3. 定义子类：兼职员工 ====================
class PartTimeEmployee(Employee):  # 同样继承 Employee
    def __init__(self, name, id, daily_salary, work_days):
        # 继承父类的 name 和 id
        super().__init__(name, id)
        # 兼职特有属性：日薪、每月工作天数
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        """兼职员工月薪计算逻辑：日薪 * 工作天数"""
        return self.daily_salary * self.work_days


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("--- 自动化人力系统测试 ---")

    # 1. 创建一个全职员工实例（姓名：张三，工号：FT001，月薪：8000）
    ft_emp = FullTimeEmployee("张三", "FT001", 8000)
    ft_emp.print_info()  # 调用继承自父类的方法
    print(f"当月实发工资: {ft_emp.calculate_monthly_pay()} 元")

    print("-" * 30)

    # 2. 创建一个兼职员工实例（姓名：李四，工号：PT002，日薪：200，工作：15天）
    pt_emp = PartTimeEmployee("李四", "PT002", 200, 15)
    pt_emp.print_info()  # 调用继承自父类的方法
    print(f"当月实发工资: {pt_emp.calculate_monthly_pay()} 元")