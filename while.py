#while 迴圈(適合沒有次數)
# sum = n = 0
# while n < 10:
#     n += 1
#     sum += n
#     print(sum)

#例子1:
# total = person = source = 0 #total是總分，person是學生人數，source是學生分數
# while source != -1:#假設學生分數是-1的時候，它就會停止
#     person += 1#將學生人數增加
#     total += source#總分和學生分數跟著增加
#     source = int(input("請輸入第 %d 位學生的成績:"%(person)))#請輸入學生分數
# average = total/(person-1)#算平均數(全班總分除全班人數-1)
# print("本班總成績:%d 分，平均成績:%5.2f分"%(total,average))