'''
CSV（Comma Separated Values）全称逗号分隔值文件是一种简单、通用的文件格式，
被广泛的应用于应用程序（数据库、电子表格等）数据的导入和导出以及异构系统之间的数据交换。
因为 CSV 是纯文本文件，不管是什么操作系统和编程语言都是可以处理纯文本的，
而且很多编程语言中都提供了对读写 CSV 文件的支持，因此 CSV 格式在数据处理和数据科学中被广泛应用。

CSV 文件有以下特点：

纯文本，使用某种字符集（如 ASCII、Unicode、GB2312等）；
由一条条的记录组成（典型的是每行一条记录）；
每条记录被分隔符（如逗号、分号、制表符等）分隔为字段（列）；
每条记录都有同样的字段序列。
'''

'''
将数据写入 CSV 文件
现有五个学生三门课程的考试成绩需要保存到一个 CSV 文件中，要达成这个目标，
可以使用 Python 标准库中的csv模块，该模块的writer函数会返回一个csvwriter对象，
通过该对象的writerow或writerows方法就可以将数据写入到 CSV 文件中，具体的代码如下所示。
'''
from pathlib import Path
import csv
import random

script_dir=Path(__file__).parent

with open(script_dir/'scores.csv','w') as file:
    # writer=csv.writer(file)
    writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names=['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores=[random.randrange(50,101) for _ in range(3)]
        scores.insert(0,name)
        writer.writerow(scores)

with open(script_dir/'scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for data_list in reader:
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem, end='\t')
        print()
'''
将来如果大家使用Python做数据分析，很有可能会用到名为pandas的三方库，它是Python数据分析的神器之一。
pandas中封装了名为read_csv和to_csv的函数用来读写 CSV 文件，其中read_csv会将读取到的数据变成一个DataFrame对象，
而DataFrame就是pandas库中最重要的类型，它封装了一系列用于数据处理的方法（清洗、转换、聚合等）；
而to_csv会将DataFrame对象中的数据写入 CSV 文件，完成数据的持久化。read_csv函数和to_csv函数远远比原生的csvreader和csvwriter强大。
'''