'''
例子1：扑克游戏。
说明：简单起见，我们的扑克只有52张牌（没有大小王），游戏需要将 52 张牌发到 4 个玩家的手上，每个玩家手上有 13 张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。

使用面向对象编程方法，首先需要从问题的需求中找到对象并抽象出对应的类，此外还要找到对象的属性和行为。
当然，这件事情并不是特别困难，我们可以从需求的描述中找出名词和动词，名词通常就是对象或者是对象的属性，而动词通常是对象的行为。
扑克游戏中至少应该有三类对象，分别是牌、扑克和玩家，牌、扑克、玩家三个类也并不是孤立的。
类和类之间的关系可以粗略的分为 is-a关系（继承）、**has-a关系（关联）**和 use-a关系（依赖）。
很显然扑克和牌是 has-a 关系，因为一副扑克有（has-a）52 张牌；玩家和牌之间不仅有关联关系还有依赖关系，因为玩家手上有（has-a）牌而且玩家使用了（use-a）牌。
'''

'''
牌类(Card)
'''
# from enum import Enum

# class Suite(Enum):
#     """花色(枚举)"""
#     #黑桃，红桃，梅花，方片
#     SPADE, HEART, CLUB, DIAMOND=range(4) #0,1,2,3

# # for suite in Suite:
# #     print(f"{suite}:{suite.value}")

# class Card:
#     '''牌'''
#     def __init__(self,suite,face):
#         self.suite=suite
#         self.face=face
    
#     def __repr__(self):
#         suites='♠♥♣♦'
#         faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         return f"{suites[self.suite.value]}{faces[self.face]}" #返回牌的花色和点数
#     #重载比较运算符
#     def __lt__(self, other):
#         if self.suite == other.suite:
#             return self.face < other.face   # 花色相同比较点数的大小
#         return self.suite.value < other.suite.value   # 花色不同比较花色对应的值
    
# # card1=Card(Suite.SPADE,5)
# # card2=Card(Suite.CLUB,11)
# # print(card1)
# # print(card2)

# '''
# 扑克类
# '''
# import random

# class Poker:
#     def __init__(self):
#         self.cards=[Card(suite,face) for suite in Suite for face in range(1,14)]
#         self.current=0 #记录发牌位置
    
#     def shuffle(self):
#         '''洗牌'''
#         self.current=0
#         random.shuffle(self.cards)
    
#     def deal(self):
#         '''发牌'''
#         card=self.cards[self.current]
#         self.current+=1
#         return card
    
#     @property
#     def has_next(self):
#         """还有没有牌可以发"""
#         return self.current<len(self.cards)

# # poker=Poker()
# # print(poker.cards) #洗前的牌
# # print("=======================")
# # poker.shuffle()
# # print(poker.cards) #洗后的牌

# '''
# 玩家类
# '''
# class Player:
#     def __init__(self,name):
#         self.name=name
#         self.cards=[] #玩家手上的牌
    
#     def get_one(self,card):
#         '''摸牌'''
#         self.cards.append(card)
    
#     def arrange(self):
#         '''理牌'''
#         self.cards.sort() #需要对运算符重载

# #创建四个玩家并将牌发到他们手上
# poker=Poker()
# poker.shuffle()
# players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# # 将牌轮流发到每个玩家手上每人13张牌
# for _ in range(13):
#     for player in players:
#         player.get_one(poker.deal())
# # 玩家整理手上的牌输出名字和手牌
# for player in players:
#     player.arrange()
#     print(f"{player.name}",end='')
#     print(f"{player.cards}")

'''
例子2：工资结算系统。
要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。其中，部门经理的月薪是固定 15000 元；程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。

通过对上述需求的分析，可以看出部门经理、程序员、销售员都是员工，有相同的属性和行为，那么我们可以先设计一个名为Employee的父类，再通过继承的方式从这个父类派生出部门经理、程序员和销售员三个子类。
很显然，后续的代码不会创建Employee 类的对象，因为我们需要的是具体的员工对象，所以这个类可以设计成专门用于继承的抽象类。
Python 语言中没有定义抽象类的关键字，但是可以通过abc模块中名为ABCMeta 的元类来定义抽象类。
关于元类的概念此处不展开讲解，当然大家不用纠结，照做即可。
'''

from abc import ABCMeta,abstractmethod

#创建抽象类
class Employee(metaclass=ABCMeta):
    '''员工'''
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def get_salary(self):
        '''结算月薪'''
        pass #空函数

class Manager(Employee):
    '''部门经理'''
    def get_salary(self):
        return 15000.00
    
class Programmer(Employee):
    '''程序员'''
    def __init__(self,name,working_hour=0):
        super().__init__(name)
        self.working_hour=working_hour
    
    def get_salary(self):
        return 200 * self.working_hour

class Salesman(Employee):
    """销售员"""
    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05
    
emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    #isinstance() 是 Python 的一个内置函数（Built-in Function），作用是：
    #判断一个对象是不是某个类（或其子类）的实例。
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')