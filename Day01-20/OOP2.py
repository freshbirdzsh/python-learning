'''
可见性和属性装饰器
可以用__name表示一个私有属性，_name表示一个受保护属性
'''
class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
#本质上是名称重整
#print(stu.__name)  # AttributeError: 'Student' object has no attribute '__name'
print(stu.__dict__)
print(stu._Student__name)

'''
动态属性
Python 语言属于动态语言，维基百科对动态语言的解释是：
“在运行时可以改变其结构的语言，例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化”。
'''
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
stu.sex = '男'  # 给学生对象动态添加sex属性
#如果不希望在使用对象时动态的为对象添加属性，可以使用 Python 语言中的__slots__魔法
class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
#stu.sex = '男'

'''
静态方法和类方法
除了对象方法之外，类中还可以有静态方法和类方法，这两类方法是发给类的消息
类方法的第一个参数是类对象本身，而静态方法则没有这个参数。
简单的总结一下，对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，
区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。
静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定。
'''
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
      

if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'周长: {t.perimeter()}')
    print(f'面积: {t.area()}')
else:
    print('无效的边长!!!')

'''
这里做一个补充说明，我们可以给上面计算三角形周长和面积的方法添加一个property装饰器（Python 内置类型），
这样三角形类的perimeter和area就变成了两个属性，不再通过调用方法的方式来访问，而是用对象访问属性的方式直接获得，修改后的代码如下所示
'''
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'周长: {t.perimeter}')
    print(f'面积: {t.area}')
else:
    print('无效的边长!!!')

'''
继承和多态
'''
class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')
