import argparse

def main():
    # 1. 创建解析器
    parser = argparse.ArgumentParser(description="AI 批量推理工具")
    
    # 2. 添加你想让用户传入的参数
    parser.add_argument("--model", type=str, default="gpt-4o", help="使用的大模型名称")
    parser.add_argument("--batch_size", type=int, default=4, help="批处理大小")
    parser.add_argument("--verbose", action="store_true", help="是否打印详细日志") # 如果写了 --verbose 就会触发为 True
    
    # 3. 解析参数
    args = parser.parse_args()
    
    # 4. 在代码中使用
    print(f"正在加载模型: {args.model}，当前 Batch Size: {args.batch_size}")
    if args.verbose:
        print("详细日志已开启")

#只有当这个 Python 文件被“直接运行”时，才执行下面的代码
if __name__ == "__main__":
    main()