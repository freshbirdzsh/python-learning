'''
读写JSON格式数据
json模块有四个比较重要的函数，分别是：

dump - 将 Python 对象按照 JSON 格式序列化到文件中
dumps - 将 Python 对象处理成 JSON 格式的字符串
load - 将文件中的 JSON 数据反序列化成对象
loads - 将字符串的内容反序列化成 Python 对象
'''
#在 Python 中，如果要将字典处理成 JSON 格式（以字符串形式存在），可以使用json模块的dumps函数，代码如下所示：
import json
from pathlib import Path
script_dir=Path(__file__).parent

my_dict = {
    'name': '张书涵',
    'age': 21,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))

#如果要将字典处理成 JSON 格式并写入文本文件，只需要将dumps函数换成dump函数并传入文件对象即可
with open(script_dir/'data.json', 'w') as file:
    json.dump(my_dict, file)

with open(script_dir/'data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)

#print(json.loads(json.dumps(my_dict)))

