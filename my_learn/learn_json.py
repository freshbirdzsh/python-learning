import json
from pathlib import Path
# 模拟大模型返回的 JSON 字符串
llm_response = '{"model": "gpt-4o", "choices": [{"text": "Hello"}]}'

# 1. 解析：把字符串变成 Python 字典 (loads)
# load string：从字符串加载 JSON。把JSON字符串解析成Python对象（字典/列表等）
data = json.loads(llm_response)
print(data["choices"][0]["text"])

# 2. 存盘：把 AI 的中间结果保存到本地 json 文件 (dump)
result_file=Path(__file__).resolve().parent/"result.json"
ai_result = {"user_id": 123, "status": "completed", "tokens_used": 450}
with open(result_file, "w", encoding="utf-8") as f:
    # ensure_ascii=False 保证中文不乱码，indent=4 让打印出来的格式漂亮
    # dump file：把 Python 数据写入文件。
    json.dump(ai_result, f, ensure_ascii=False, indent=4)