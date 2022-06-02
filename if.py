#學會判斷式(if...eliif...else)

#1.單向判斷式(if)
possword = input("請輸入密碼:")
if possword == "1234":
    print("歡迎光臨")

# #2.雙向判斷式(if...else)
possword = input("請輸入密碼:")

if possword == "1234":
    print("歡迎光臨")
else:
    print("密碼打錯了")

#多向判斷式(if...eliif...else)
source = int(input("請輸入成績:"))
if source == 100:
    print("優等")
elif source >= 90:
    print("甲等")
elif source >= 80:
    print("乙等")
elif source >= 70:
    print("丙等")
elif source >= 60:
    print("丁等")
else:
    print("不及格")

#巢狀判斷式
money = int(input("請輸入金額:"))

if money >= 10000:
    if money >= 10000:
        print(money*0.8,end="元\n")
    elif money >= 50000:
        print(money*0.85,end="元\n")
    elif money >= 30000:
        print(money*0.9,end="元\n")
    else:
        print(money*0.95,end="元\n")
else:
    print(money,end="元\n")



