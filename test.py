f = open(r"E:\学习资料\Python编程文件\编程Myself\0713\text.txt", "r", encoding="GBK")

j = 0
lis = []
data = f.readlines()
for i in data:
    j += 1
    print(i,type(i))
    lis.append(eval(i))
