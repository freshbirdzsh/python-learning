
'''
dataclass 和 typing 合在一起，
能把 AI 程序中松散、容易出错的字典数据，变成清晰、可约束、可维护的数据结构。
一句话理解：
typing：描述“数据应该长什么样”。
dataclass：把这种数据结构真正做成好用的 Python 类。
'''
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ChatMessage:
    role: str                       # 'user' 或 'assistant'
    content: str                    # 对话内容
    tokens: int = 0                 # 默认值为 0
    images: Optional[List[str]] = None  # 可选的图片路径列表，C++ 中的 std::optional

# 实例化极其干净，自动生成 __init__ 和 __repr__
msg = ChatMessage(role="user", content="帮我写个点灯程序")
print(msg)  # ChatMessage(role='user', content='帮我写个点灯程序', tokens=0, images=None)
print(msg.role)  # user
print(msg.content)  # 帮我写个点灯程序