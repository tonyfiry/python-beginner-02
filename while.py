#while (沒有限定次數迴圈)

# total = n = 0

# while n < 10:
#     n+=1
#     total+=n
#     print(total,end =" ")


total = person = source = 0

while (source != -1):
    person += 1
    total += source
    source = eval(input("請輸入第 %d 位學生的成績:"%(person)))
average = total / (source-1)
print("本班總成績: %d 分，平均成績:%5.2f分"%(total,average))