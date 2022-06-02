#學會元組(Tuple)
data = (1,2,3,4,5,6)
# # data[1]=2#元組是不能改變
print(data)
print(data[3])
# # del data[0]#TypeError: 'tuple' object doesn't support item deletion
print(len(data))

#學會元組(Tuple)和串列(List)的互換:
g1 = (1,2,3,4)#設元組(Tuple)
data = list(g1)#轉換串列
data.append(5)#加入5裡面
print(data)#列印出[1,2,3,4,5]

#學會串列(List)和元組(Tuple)的互換:
list1 = [1,2,3,4,5]#設串列(List)
data = tuple(list1)#轉換元組(Tuple)
print(data[0])#列印找出卻是1

