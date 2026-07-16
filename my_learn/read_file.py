#f=open("./data.txt","r",encoding="utf-8")
# content = f.read()
# print(content)

#with ... as ... 语句被称为上下文管理器（Context Manager）
# with open("./data.txt","r",encoding="utf-8") as f:
#     content=f.read()
#     print(content)

with open("data.txt", "r", encoding="utf-8") as f:
    # strip() 会把文本末尾的 '\n' 吃掉
    print(f.readline().strip())
    print(f.readline().strip())

    # 既然文本自带了换行，就让 print 闭嘴，不要再额外加换行了
    # print(f.readline(), end="")
    # print(f.readline(), end="")

with open("data.txt", "r", encoding="utf-8") as f:
    #readlines()的返回值是列表
    #print(f.readlines())
    lines=f.readlines()
    for line in lines:
        print(line.strip())


