#用%來格式化
print("姓名:國文總分，數學總分，自然總分，體育總分")
print("%s:國文總分%d，數學總分%d，自然總分%d，體育總分%d"%("小明",23,56,72,73))
print("%s:國文總分%d，數學總分%d，自然總分%d，體育總分%d"%("小黑",42,53,74,71))
print("%s:國文總分%d，數學總分%d，自然總分%d，體育總分%d"%("小綠",24,55,77,78))
print("%s:國文總分%d，數學總分%d，自然總分%d，體育總分%d"%("小黃",100,53,73,74))

#用format來格式化
name = "小明"
source = 33
print("{}，但數學分數卻是{}".format(name,source))

#用f格式化
name = "小明"
source = 33
print(f"{name}，但數學分數卻是{source}")

