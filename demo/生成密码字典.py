import itertools as its

words = "1234568790"
num = 2
print("开始生成")
# while(num <= 64):
#     r =its.product(words,repeat=num)
#     dic = open("pass.txt","a")
#     for i in r:
#         dic.write("".join(i))
#         dic.write("".join("\n"))
#     num+=1
r = its.product(words, repeat=num)
dic = open("pass_n{}.txt".format(num), "a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
print("生成结束")
