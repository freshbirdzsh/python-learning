from pathlib import Path

# 1. 极其优雅的路径拼接（用 / 符号！）
base_dir = Path("/Users/zhangshuhan/Projects")
data_file = base_dir / "data.txt"  # 自动处理跨平台的斜杠 (Mac/Windows)

# 2. 常用四大金刚属性
print(data_file.name)      # "data.txt" (文件名)
print(data_file.stem)      # "data"     (文件名，不带后缀)
print(data_file.suffix)    # ".txt"     (后缀名)
print(data_file.parent)    # "/Users/zhangshuhan/Projects" (父目录)

# 3. AI 批量处理：死磕 .glob()（查找所有图片/Markdown）
# 使用当前脚本所在目录作为基准，不受运行时工作目录影响
image_dir = Path(__file__).resolve().parent / "dataset"
# 找出 dataset 目录下所有 png 图片
for img_path in image_dir.glob("*.png"):
    print(img_path)

# 4. 安全创建目录（写 AI 结果保存逻辑时必用）
output_dir = Path("./outputs/predictions")
output_dir.mkdir(parents=True, exist_ok=True) # parents=True 表示即使上级目录不存在也一并创建；exist_ok=True 表示存在了也不报错
