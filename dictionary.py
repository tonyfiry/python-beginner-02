#學會dict(字典)方法
#第一種method(方法):
dict01 = {"apple":1,"banana":2,"orange":3}
print(dict01)
print(dict01[1])#鍵-值錯誤:1
print(dict01["banana"])#2

#第二種method(方法):
dict01 = dict([["apple",1],["banana",2],["orange",3]])
print(dict01["banana"])#2

##第三種method(方法):
dict01 = dict(apple=1,banana=2,orange=3)
print(dict01)#列印出{'apple': 1, 'banana': 2, 'orange': 3}

#例子01:
dict01 = {"A":"內向穩重","B":"外向樂觀","O":"堅強自信","AB":"聰明自然"}
name = input("請選擇的血型:")
booled = dict01.get(name)
if booled == None:
    print(f"沒有+{name}+血型")
else:
    print(f"{name}的血型個性為{dict01[name]}")

dict01 = {"A":"蜜蜂","B":"老鷹","C":"蜘蛛","D":"獅子"}
name = input("請選擇:")#設輸入(請選擇:)
booled = dict01.get(name)#設booled給他名字
if booled != None:
    print(f"是{dict01[name]}")#如果不等於空值的話，它就馬上執行A,B,C,D

else:
    print(f"不是昆蟲，也不是動物")#打錯的話，它就馬上執行說不是昆蟲，也不是動物

#修改字典:
dict1 = {"鳳梨":50,"香蕉":56,"蘋果":30}
dict1["香蕉"] = 60
print(dict1)

#刪除字典:
dict1 = {"鳳梨":50,"香蕉":56,"蘋果":30}
del dict1["蘋果"]
print(dict1)

#用in查詢鍵存不存在:
dict1 = {"鳳梨":50,"香蕉":56,"蘋果":30}
booled = "鳳梨" in dict1#True
booled1 = "草莓" in dict1#False
print(booled1)


#例子2:
dict1 = {"林小明":85,"曾山水":93,"鄭美麗":67}
name = input("輸入學生姓名:")#設輸入
if name in dict1:#判斷這些同學有沒有在裡面
    print(f"{name}的成績為{str(dict1[name])}")#如果有就公布學生成績，沒有的話就新增學生名字
else:
    score = int(input("輸入學生成績:"))#新增新學生名字和成績
    dict1[name] = score#加入到新學生的成績裡面
    print(f"字典內容:"+str(dict1))

#list and dict

#第一種方法
dict01 = {"金牌":26,"銀牌":34,"銅牌":30}
data_key = list(dict01.keys())
key1 = data_key[0]
key2 = data_key[1]
key3 = data_key[2]
data_value = list(dict01.values())
value1 = data_value[0]
value2 = data_value[1] 
value3 = data_value[2]  
print("得到的"+str(key1)+"數目為"+str(value1)+"面")
print("得到的"+str(key2)+"數目為"+str(value2)+"面")
print("得到的"+str(key3)+"數目為"+str(value3)+"面")

#第二種方法
dict01 = {"金牌":26,"銀牌":34,"銅牌":30}
listkeys = list(dict01.keys())
listvalue = list(dict01.values())
for i in range(len(listkeys)):
    print("得到的"+str(listkeys[i])+"數目為"+str(listvalue[i])+"面")

#第三種方法
dict01 = {"金牌":26,"銀牌":34,"銅牌":30}
 
listkeys = list(dict01.keys())
listvalue = list(dict01.values())
n = 0
while n < len(listkeys):
    print("得到的%s數目為%s面"%(str(listkeys[n]),str(listvalue[n])))
    n+=1

#items方法
dict01={"金牌":26,"銀牌":34,"銅牌":30}
clist = list(dict01.items())#轉換成串列
for name,num in clist:#name是獎盃名稱，clist是牌面數字
    print("你得到 %s 數目為 %d 面"%(name,num))

#setdefault方法
dict01={"金牌":26,"銀牌":34,"銅牌":30}
dict02 = dict01.setdefault("銀牌",33)#33
dict03 = dict01.setdefault(33)#None
print(dict02,dict03)



