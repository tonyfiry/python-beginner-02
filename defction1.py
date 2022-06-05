#建立自訂函式:
#例子1:
def say(name1,name2,name3):
    name = {name1,name2,name3}
    print(name)
say("tony","drive","dirz")

#例子2:
def GetArea(width,height):
    area = width*height
    return area
rel = GetArea(12,12)
rel2 = GetArea(width=22,height=55)
rel3 = GetArea(height=23,width=22)
print(rel,rel2,rel3)

#有名的範例:攝氏溫度轉華氏溫度
def ctof(c):
    f = c*1.8+32
    return f
inputc = float(input("請輸入攝氏溫度:")) 
print("華氏溫度為%5.1f度"%ctof(inputc))

#參數預測值:
def Getarea(h,w=12):#w是參數預測值
    area = h*w
    return area
print(Getarea(12))
print(Getarea(6,2))

##變數有效範圍
#區域變數(函式內部的變數)和全域變數(函式外部的變數):
def souce():
    var1 = 1#區域變數
    print(var1,var2)

var1 = 10#全域變數
var2 = 10#全域變數
souce()
print(var1,var2)

# #使用global變數(算是全域變數一種，適合用在函式內部)

def souce():
    global A1#設global變數為1
    A1 = 1
    print(A1,A2)
A1 = 10
A2 = 100
souce()
print(A1,A2)


#pow函式:
p = pow(3,2,3)#是3的2次方，所以是9，然後9除於3，餘數是0
print(p)#0


# #divmod函式:
ret = divmod(44,3)
print(ret[0],ret[1])#14 2   ret[0]是商數、ret[1]是餘數
print(ret)#(14, 2)

#round函式:
ret1 =  round(3.5)
ret2 =  round(3.7)
ret3 =  round(5.5)
ret4 =  round(4.3,1)
ret5 =  round(3.2,0)

print(ret1)#4
print(ret2)#4
print(ret3)#6
print(ret4)#4.3
print(ret5)#3.0

#範例:
person = int(input("請輸入人數:")) 
apple = int(input("請輸入蘋果總數:"))
ret = divmod(person,apple)
print("總數人數是%d"%(ret[0]))
print("蘋果數字是%d"%(ret[1]))



##數值函式
#sum、max、min函式:
print(max(1,2,3,4))#4
print(min(1,2,3,4))#1
print(sum([1,2,3,4],5))#15

#sorted函式:
print(sorted([1,2,3,4,5,6]))
print(sorted([1,2,3,4,5,10],reverse=True))

#範例:
innum = 0
list1 = []
while innum != -1:
    innum = int(input("請輸入電費(-1:結束):"))
    list1.append(innum)
list1.pop()
print("共輸入%d 個數"%(len(list1)))
print("最多電費為:%d"%(max(list1)))
print("最少電費為%d"%(min(list1)))
print("電費總和為%d"%(sum(list1)))
print("電費由大到小排序:{}".format(sorted(list1,reverse=True)))


##字串函式
#join函式(連結字串):
list1 = ["tony","king","dord"]
s = " ".join(list1)#" "來連結一個字串
print(s)#tony king dord

#split函式(分割字串):
s = "How are you to?"
ss = s.split(" ")
print(ss)


#startswith函式:
s = "你是白癡嗎?"
print(s.startswith("你"))#True
print(s.startswith("嗎"))#False

#endswithc函式:
s = "How are you to?"
ss = s.endswith("to")
ss1 = s.endswith("to?")
print(ss)#False
print(ss1)#True


#範例(1):
web = input("請輸入網址:")
if web.startswith("https://") or web.startswith("http://"):
    print("就是對的")
else:
    print("就是錯的")
#範例(2):
class1 = input("請輸入班級:")
if class1.startswith("二年甲班") or class1.startswith("二年乙班"):
    print("去教官室找我!!")
else:
    print("那就沒事了!")

#字串排版相關字串(ljust,rjust,center)
#ljust函式:
p = "hello world!!"#設字串
print(p.rjust(8))
print(p.ljust(8))
print(p.ljust(8,"%"))
print(p.ljust(12))

# #rjust函式:
print(p.rjust(12,"#"))
print(p.rjust(8,"##"))
print(p.ljust(12,"4a"))#產生錯誤，不能超過一個填充字元。


#lstrip、rstrip、strip函式:
s = "   I love python   "
a1 = s.lstrip()#移到3個字元右方
a2 = s.rstrip()#移到3個字元左方
a3 = s.strip()#移到中間，讓空出3個字元左方，讓空出3個字元右方
print(s)
print(a1)
print(a2)
print(a3)

#範例:
listname = ["林大明","陳阿中","張小英"]
listchinese = [100,74,82]
listmath = [87,88,65]
listenglish = [79,100,8]
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
    print(listname[i].ljust(5),str(i+1).rjust(3),
    str(listchinese[i]).rjust(5),str(listmath[i]).rjust(5),str(listenglish[i]).rjust(5))