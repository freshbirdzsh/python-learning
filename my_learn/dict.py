#电子字典
slang_dict={" I/E人":"「I 人 E 人」能快速表達一個人的社交傾向：I 人--偏好獨處或與少數親密的人相處，不擅於表達自己 E 人--樂於社交、享受與他人互動。",
            "破防":"原為遊戲術語，現指被某些話或行為觸及痛點、情緒崩潰，類似於「玻璃心碎了」的感覺"}

#添加新词
slang_dict["芭比 Q 了"]="延伸自烤肉「BBQ」的同音字，用來表示「完蛋了」、「慘了」"

query=input("请输入您要查询的词语：")

if query in slang_dict:
    print("您查询的"+query+"含义如下：")
    print(slang_dict[query])
else:
    print("您查询的词暂未收录")
    print("本词典收录的词语条目数："+str(len(slang_dict))+"条")