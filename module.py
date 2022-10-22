#import 模組(三種方法)

#第一種方法(import random)

#第二種方法(from random import *)

#第三種方法(import random as rd)


#choice函式:
# str1 = "hellowoeld"
# rd=r.choice(str1)#設字串的隨機變數
# print(rd)#w

#randint函式:
# for i in range(1,10):
#     print(r.randint(3,8))#隨機從3到8

#randrange函式:
# for i in range(1,10):
#     print(r.randrange(1,10,2))#隨機從1到10，但遞增多2個


#random函式:
# s = r.random()#隨機浮點數
# print(s)#隨機數字出來

#uniform函式:
#print(r.uniform(1,3))#隨機浮點數

#範例:
import random as r

while True:#把迴圈打開
    inkey = input("按任意鍵再按[Enter]鍵擲格子，直接按[Enter]鍵結束:")
    if len(inkey) > 0:
        num = r.randint(1,10)#設隨機整數
        print("你擲格子的點數為:"+str(num))
    else:
        print("遊戲結束!")
        break   

 