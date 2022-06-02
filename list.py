#串列(list)或是陣列(Array)
# data1 = [1,2,3,4,5]#int型態
# data2 = ["小明","小蘭","小綠"]#字串型態
# data3 = ["drive",True,123]#也可以用不同型態
# print(data1,data2,data3,sep="\n")
# print(f"數字:{data1}")
# print(f"名字:{data2}")
# print(f"綜合:{data3}")

# #例子1
# d = [85,75,66]
# print("國文 %d 分"%(d[0]))
# print(f"英文 %d 分"%(d[0]))
# print("數學 %d 分"%(d[2]))

# #使用range()函式
# r1 = range(5)
# print(r1) #(range(0,5))
# print(list(range(5))) #[0, 1, 2, 3, 4]
# print(list(range(-6,1))) #[-6, -5, -4, -3, -2, -1, 0]

#學會append，加入元素放在後面。
# clist1 = [1,2,3,4,5,6]
# clist1.append(8)
# # clist1[7] = 9#索引值錯誤，原因範圍過大。
# print(clist1)

#學會insert，將元素加在串列的指定位置。
# clist = [1,2,3,4,5,6]
# clist.insert(2,7)
# clist.insert(3,8)
# clist.sort()
# print(clist)

#例子2
# score = []
# total = inscore = 0
# while inscore != -1:
#     inscore = int(input("請輸入學生的成績:"))
#     score.append(inscore)
# print("共有%d個學生"%(len(score)-1))
# for i in range(0,len(score)-1):
#     total += score[i]
# average = total / (len(score)-1)
# print("本班總成績:%d 分，平均成績:%5.2f分"%(total,average))

#學會extend，差append來於是不能是元素。
#例子3
# list1 = [1,2,3,4,5]
# list1.extend([6,7,8])
# list1.extend(9)#錯誤，不能當作串列元素
# print(list1)

#學會pop，移除最後或是指定位置數字。
# list1 = [1,2,3,4,5]
# list1.pop(2)
# # list1.pop([0])#TypeError: 'list' object cannot be interpreted as an integer
# print(list1)

