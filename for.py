#for 迴圈 #適合固定次數使用的
d1 = [1,2,3,4,5]#設定串列d1
for list1 in d1:#在使用for迴圈把串列d1列印出來
    print(list1)#結果列印是1,2,3,4,5

#例子1
n = int(input("請輸入正整數:"))
for i in range(n):
    n+=i
print(f"1到100的整數和為 {n}")

#例子2
sum = 0
n = int(input("請輸入正整數:"))
for i in range(1,n+1):
    sum += i
print("1到%d的整數和為%d"%(n,sum))

##巢狀for迴圈

#例子1
n = 0
for i in range(1,10):
    for j in range(1,10):
        n+=1
print(n)

#例子2
for i in range(1,10):
    for j in range(1,10):
        p = i*j
        print(f"{i}*{j}={p}",end=" ")
    print()

#多加break
for i in range(1,11):
    if i == 6:
        break
    print(i,sep=",",end=" ")#列印1 2 3 4 5 
#多加continue
for i in range(1,11):
    if i == 6:
        continue
    print(i,sep=",",end=" ")#列印1 2 3 4 5 7 8 9 10 

#例子1
n = int(input("請輸入大樓的樓層:"))
print("本大樓具有的樓層:")
if n>=3:
    n += 1
for i in range(1,n+1):
    if i == 4:
        continue
    print(i,end=" ")
    
#例子2
n = int(input("請輸入大於1的整數:"))
if n == 2:
    print("2是質數!")
else:
    for i in range(2,n):
        if n % i == 0:
            print("%d 不是質數"%(n))
            break
    else:
        print("%d 是質數"%(n))