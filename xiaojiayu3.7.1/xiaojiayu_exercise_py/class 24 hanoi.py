def hanoi(n,x,y,z):       #x起始轴，y中间过渡轴，z终点轴，n起始轴上的盘子数
    if n == 1:
        print(x ,'-->',z)#起始轴只有一个盘子，直接放到终点轴
    else:
        hanoi(n-1,x,z,y) #将起始轴最上面的n-1个盘子放到过渡轴上
        hanoi(1,x,y,z)   #将起始轴最底下的一个盘子放到终点轴上
        hanoi(n-1,y,x,z) #将过渡轴上的n-1个盘子放到终点轴上

hanoi(3,1,2,3)

# n = 3 时的运算过程如下：
# 第一步 判断if不符合，进入else
# 第二步 计算hanoi(n-1,x,z,y)，带入数据是hanoi(2,1,3,2),以下省略hanoi，进一步带入计算得：
# 1,1,2,3  1 --> 3  执行if==1时的语句，print(x ,'-->',z)，即1 --> 3，以下同上
# 1,1,3,2  1 --> 2
# 1,3,1,2  3 --> 2
# 第三步 计算hanoi(1,x,y,z)，即：
# 1,1,2,3  1 --> 3
# 第四部 计算hanoi(n-1,y,x,z)，带入数据是hanoi(2,2,1,3),以下省略hanoi，进一步带入计算得：
# 1,2,3,1  2 --> 1
# 1,2,1,3  2 --> 3
# 2,1,2,3  1 --> 3

