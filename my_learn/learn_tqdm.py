from tqdm import tqdm

#最基础的用法：把原本循环的可迭代对象包起来。
texts = ["你好", "Python", "LLM", "Embedding"]
for text in tqdm(texts,desc="生成 Embedding"):
    #调用模型，处理文本...
    pass
