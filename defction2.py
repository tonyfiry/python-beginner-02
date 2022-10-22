##搜尋及取代字串
#find函式
s = "嗨你好喔"
print(s.find("嗨"))#因為從0開始關係，所以就印出0
print(s.find("喔"))#印出3
print(s.find("幹"))#找不到這個字，所以只好印出-1

#replace函式:
str1 = "I love python"
print(str1.replace("python","Java"))#I love Java
print(str1.replace("p","s",1))#I love sython
print(str1.replace("o",""))#I lve pythn

#範例:
date1 = "2022-06-05"
date1 = date1.replace("-","年",1)
date1 = date1.replace("-","月",1)
date1 += "日" 
print(date1)
