#set集合:
# dict1 = {}#空字典
# print(type(dict1))
# set1 = set()#空集合
# print(type(set1))

#例子
# persons = ["林小明","曾山水","鄧美麗"]#建立串列
# s = set(persons)#轉換字典
# print(s)#顯示{'曾山水', '鄧美麗', '林小明'}
# list1=list(s)#再轉成串列
# print(list1)#顯示['曾山水', '鄧美麗', '林小明']
# print(list1[2])#林小明

##集合的操作
#&交集:是兩個不同集合，重點它是重複的集合
# set1 = {1,2,4,10,9}
# set2 = {1,2,3,4,5,6}
# print(set1&set2)

#|聯集:是兩個不同集合，不管是重複還是不同數字，當做所有集合來看
# set1 = {1,2,4,5,7}
# set2 = {1,2,3,4,5,6,7}
# print(set1|set2)#{1, 2, 3, 4, 5, 6, 7}

#-差集:是兩個不同集合，重點它是不重複的集合
# A = {1,2,3,4,6,7,8}
# B = {3,4,5,6}
# print(A-B)
# print(B-A)

#^反差集(對稱差集):跟差集相反，重點它是重複的集合
# A = {1,2,3,4,6,7,8}
# B = {3,4,5,6}
# print(A^B)


##集合的方法
#set(add)方法:
# class01 = {"二年甲班","三年甲班","四年乙班"}
# class01.add("一年甲班")
# print(class01)

#set(clear)方法:
# class01 = {"二年甲班","三年甲班","四年乙班"}
# print(class01.clear())
# print(class01)

#set(copy)方法:
# class01 = {"二年甲班","三年甲班","四年乙班"}
# class02 = class01.copy()
# class02.add("一年甲班")
# print(class01,class02)

##set(discord)方法:
# class01 = {"dive","tony","daia"}
# class01.discard("dive")
# print(class01)

#set(remove)方法:
# class01 = {"dive","tony","daia"}
# class01.remove("dive")
# print(class01)

#set(pop)方法:
# name01 = {"nana","diva","maod","mair"}
# p = name01.pop()
# print(p)#列印nana
# print(name01)#列印{'diva', 'mair', 'maod'}

# #set(update)方法:
# A = {1,2,3,4,5,6}
# B = {2,3,4,5,6,7,8,9}
# A.update(B)
# print(A)#列印{1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(B)#列印{2, 3, 4, 5, 6, 7, 8, 9}

##集合基本函式
#max函式:
# A = {1,2,3,4}
# print(max(A))#最大是4
# #min函式:
# print(min(A))#最小是1
# #sum函式:
# print(sum(A))#總和是10
# #len函式:
# print(len(A))#長度是4
# print(enumerate(A))#enumerate物件

# for item in list(enumerate(A)):
#     print(item)#(0, 1),(1, 2),(2, 3),(3, 4)

# for i,item in enumerate(A):
#     print(i,item)# 0 1 : 1 2 : 2 3 : 3 4 

#frozenset(凍結集合):


A = frozenset({1,2,3,4})
B = frozenset({3,4,5,6})

print(A&B)
print(A|B)
print(A-B)
print(A^B)
print(A in B)
print(A not in B)
print(A != B)
print(A == B)

print(max(A))
print(min(B))



