from time import sleep
# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。

myD = {1: 'a', 2: 'b'}
for (key,value) in dict.items(myD):
    print(key,value)
    sleep(1)  # 暂停 1 秒
#如果是import time ，需要time.sleep(1)