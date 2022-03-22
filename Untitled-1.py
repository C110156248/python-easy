#宣告變數
#a = 0 ; b = 1 
#x = y = z = 20 
#age, name = 2, "xaxaz"
#str = "xaxaz"
#N1 = True

#print(a,b)
#print(x,y,z)
#print(age,name) # 註解


#資料型別
#print(type(name))
#print(type(age))
#print(type(str))
#print(type(N1))
# nums = 34 + Ture = 34 + 1
# str2 = """
# xaxaz
# haha
# """
# name2 = 'Alex\'s iphene'
# numtype = 20 + int("76")

# #輸出
# print("高科大")
#print(100, "NKUST",70,sep="0")#sep開頭  end結尾
# print(100, "NKUST",80,sep="0",end="@")# @會串接下一段字串
# print(100, "NKUST",80,sep="%")

# #print 參數格式化
# print("%s的成績是%d分" % ("班代",90)) # %S插入字串   %d插入數字
# print("%5s的成績是%4d分" % ("班代",90))#正數靠右
# print("%-5s的成績是%-4d分" % ("班代",90))#負數靠左
# print("我的BMI%f" % (18)) # %f 插入浮點數
# print("我的BMI%.2f" % (18))# 取兩位小數，四捨五入
# print("我的BMI%6.2f" % (18))# 代表有6位數(3位整數，1個小數點，2位小數)

# #print 參數格式化
# print("{}成績是{}".format("班代",90))#另類寫法
# print("{1}成績是{0}".format("班代",90))#結果 90成績是班代
# print("{0:5s}成績是{1:.2f}".format("班代",90.765))#結果 班代   成績是90.77(四捨五入)
#print("{0:5s}成績是{1:.2f}".format("班代",90.765))
# print("{0}成績是{1:.2f}".format("班代",90.765))
# print("{}成績是{}{}".format("班代",90,70))#結果 班代成績是9070
# #(f) 另類寫法
# name1 = "xa"
# s = 90
# print(f"{name1}的成績是{s}")

# print("%s%5s%5s%5s%5s" % ("姓名","座號","國文","數學","英文"))
# print("%s%5s%7s%7s%7s" % ("林大明","1","100","87","79"))
# print("%s%5s%7s%7s%7s" % ("陳阿中","2","74","88","100"))
# print("%s%5s%7s%7s%7s" % ("張小英","11","82","65","8"))
# print("%s%5s%5s%5s" % ("年度","所得稅","營業稅","證交稅"))
# print("{0:7s}{1:8s}{2:8s}{3:s}" .format ("2017","98.34","90.20","104.7"))
# print("{0:7s}{1:7s}{2:9s}{3:s}" .format ("2016","83.00","110.50","82.45"))
# print("{0:7s}{1:8s}{2:7s}{3:s}" .format ("2015","98.00","79.32","102.00"))


#輸入input命令
#由input()所收到的值是字串

"""
算數:+-* %(取餘數)//(取商)**(指數)
"""
#字串運算
"""
 e= "0123456789"
print(e*2) #複製字串
print(e[0])#輸出第一個字
print(e[-1])#輸出最後一個字
print(e[:])#輸出全部

print(e[1:5])#輸出1234
print(e[2:])#23456789
print(e[:2])#01

print(e[-2:])#89
print(e[:-2])#01234567
print(e[-4:-2])#67
print(e[5:-2])#567

print(e[2:10:2])#2468
print(e[::-1])#9876543210


#綜合運算
x1="3"
y1=3
a=x1*y1
print(a)#333

x2=6
y2=3
b= x2**y2
print(b)#216

x3 = 5
y3 = 2 
c = x3/y3 
print(c)#2.5

x4 = 7
y4 = 5
d = x4 < y4
print(d) #f

#練習
Q1 = input("請輸入一個字串abvba")
print(Q1)
a1= (Q1[::-1])
a1 == Q1 # print("迴文結果為",Q1)
"""
 # IF 條件式 : 
"""
語法
if 判斷式:
    結果1
else:
    結果2
"""
#範例1
# score = int(input("請輸入分數"))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")
# #範例2
# pw=input("輸入密碼")
# if pw == "1234")
#     print("正確")
# else)
#     print("錯誤")    
# rain = input("會下雨嗎")
# if (rain=="Y" or "y" "會"):
#     print("帶雨具")
# else:
#     print("不用帶")

#練習
# b1 = int(input("請輸入購買金額"))
# if b1 >= 2000:
#     print(b1*0.9)
# else:
#     print(b1)
# Q2 = input("請輸入一個整數")
# A2 = int(Q2)%2
# if  A2 == 0:
#     print(str(Q2)+"為偶數")
# else:
#     print(str(Q2)+"為奇數")

# t1 =int(input("請輸入三角形邊長a"))
# t2 =int(input("請輸入三角形邊長b"))
# t3 =int(input("請輸入三角形邊長c"))
# if (t1+t2>t3 and  t3+t2>t1 and t1+t3>t2):
#     print("可構成三角形")
# else :
#     print("不可構成三角形")

"""
多項式if
if條件1
    程式區塊
elif條件2
    程式區塊
else:
    程式區塊    
"""
#範例1
# s1 = int(input("輸入分數"))
# if s1>=90:
#     print("甲等")
# elif s1>=80:
#     print("乙等")
# elif s1>=70:
#     print("丙等")
# elif s1>=60:
#     print("丁等")
# else:
#     print("不及格")


# #練習
# x= int(input("請輸入物品重量"))
# if x > 20:
#     print("超過20公斤無法寄送")
# elif x>15 and x<=20:
#     print("所需郵資為110元")
# elif x>10 and x<=15:
#     print("所需郵資為90元")
# elif x>5 and x<=10:
#     print("所需郵資為70元")
# else:
#     print("所需郵資為50元")



# KG = int(input("請輸入體重"))
# M = float(input("請輸入身高(公尺)"))
# BMI =KG/ (M ** 2)
# print("BMI為"+str(BMI))
# if BMI>=27:
#     print("體重肥胖")
# elif   27>BMI>=24:
#     print("體重過重")
# elif   24>BMI>=18:
#     print("體重正常")
# else:
#     print("體重過輕")


# mon = int(input("請輸入購物金額:"))

# if mon>=100000:
#     print(str(mon*0.8)+"元")
# elif 100000>mon>=50000:
#     print(str(mon*0.85)+"元")
# elif 50000>mon>=30000:
#     print(str(mon*0.9)+"元")
# elif 30000>mon>=10000:
#     print(str(mon*0.95)+"元")
# else:
#     print(str(mon)+"元")


# a =int(input("請輸入數值"))
# b =int(input("請輸入數值"))
# c =int(input("請輸入數值"))
# if a>b and a>c:
#     print("最大值為"+str(a))
# elif b>a and b>c:
#     print("最大值為"+str(b))
# elif c>a and c>b:
#     print("最大值為"+str(c))
         

# M=int(input("請輸入月份"))
# if 3>=M>=1:
#     print(str(M)+"月是春天")
# elif  6>=M>=4:
#     print(str(M)+"月是夏天")
# elif  9>=M>=7:
#     print(str(M)+"月是秋天")
# elif  12>=M>=10:
#     print(str(M)+"月是冬天")
# elif M>12:
#     print(str(M)+"月份不在範圍內")

# mon2 =int(input("請輸入今年收入淨額"))
# if mon2>2000000:
#     t =mon2*0.3
#     print("付稅金額"+str(t))
# elif 2000000>mon2 and mon2>=1000000:
#     t =mon2*0.21
#     print("付稅金額"+str(t))
# elif 1000000>mon2 and mon2>=600000:
#     t=mon2*0.13
#     print("付稅金額"+str(t))
# elif 600000>mon2 and mon2>=300000:
#     t=mon2*0.06
#     print("付稅金額"+str(t))
# else:
#     print("免稅")


# x1=float(input("請輸入該點的X座標"))
# y1 =float(input("請輸入該點的Y座標"))
# if x1>0 and y1>0:
#     print("該點在第一象限")
# elif x1<0 and y1>0:
#     print("該點在第二象限")
# elif x1<0 and y1<0:
#     print("該點在第三象限")
# elif x1>0 and y1<0:
#     print("該點在第四象限")
# elif x1==0 and y1!=0:
#     print("該點在y軸上")
# elif x1!=0 and y1==0:
#     print("該點在x軸上")

# b =float(input("請輸入體溫?"))
# if b>=39:
#     print("體溫很燒")
# elif 39>b>=38:
#     print("體溫有點燒")    
# elif 38>b>35:
#     print("體溫正常")
# elif 35>b:
#     print("體溫過低")

# range()整串數列
# range(起始值,終止值,間隔值)
# list1=range(5)
# print(list(list1))
# # 結果0,1,2,3,4
# list2=range(3,8)
# print(list(list2))
# # 結果3,4,5,6,7
# list3=range(3,8,2)
# print(list(list3))
# # 結果3,5,7
# list4 = range( 3, 8, -1)
# print(list(list4))
# # 結果[]
# list5=range(-2,4)
# print(list(list5))
# # 結果-2,-1,0,1,2,3

# l1=range(0,10)
# print(list(l1))

# l2=range(1,10)
# print(list(l2))

# l3=range(1,10,2)
# print(list(l3))

# l4=range(10,1,-2)
# print(list(l4))

"""
for迴圈
for 變數 in 串列
    程式區塊
"""
# list6=["蘋果","橘子","香蕉"]
# for s in list6:
#     print(s)

# sum=0
# for i in range(1,11):
#     sum += i
# print(sum)

# q1=int(input("請輸入正整數"))
# a1=range(1,q1+1)
# sum=0
# for i in a1:
#     sum+=1
#     print(sum)

# q2=int(input("請輸入正整數"))
# a2=range(1,q2+1)
# s=0
# for i in a2:
#     s+=i
# print(s)

# t1=int(input("請輸入起始值"))
# t2=int(input("請輸入終止值"))
# t3=int(input("增減值"))
# a3=range(t1,t2+1,t3)
# s1=0
# for i in a3:
#     s1+=i
#     print(s1)
# 巢狀
# for i in range(1,10):
#     for j in range(1,10):
#         p=i*j
#         print("{0}x{1}={2:2} ".format(i,j,p),end="")
#     print()

# q1=int(input("請輸入正整數"))
# t1=""
# for i in range(1,q1+1):
#     t1=t1+str(i)
#     print(t1)

# q2=int(input("請輸入正整數"))
# for a in range(q2,0,-1):
#     for j in range(a,0,-1):
#         print("*",end="")
#     print()

# break
# for i in range(1,11):
#     if(i==4):
#         break
#     print(i,end="")
# print("ending")

# continue
# for i in range(1,11):
#     if(i==4):
#         continue
#     print(i,end="")

# in 
# a=(1,2,3,4)
# if 1 in a:
#     print("a包含1")
# else:
#     print("1不在a的範圍")

# b=list("fsfefesbv")
# if "f" in b:
#     print("f在串列b裡")
# else:
#     print("不在")

# 字典
# word1={"早安":"Good monring","謝謝":"Thank you"}
# if "謝謝" in word1:
#     print(word1["謝謝"])
# else:
#     print("並沒有")
# c=set("tiger")
# if "t" in c:
#     print("包含t")
# else:
#     print("不包含t")
# te=""
# for i in range(1,22):
#     if (i/5==0):
#         continue
#     print(i,end=" ")

"""
While條件式
    程式區塊
"""
# t=n=0
# while(n<10):
#     n+=1
#     t+=n
# print(t)

# t=i=1
# n=int(input("輸入整數"))
# while(i<=n):
#     t*=i
#     i+=1
# print("%d!=%d" %(n,t))

# t=i=1
# n=int(input("輸入整數"))
# for i in range(1,n+1,1):
#     t*=i
#     i+=1
# print("%d!=%d" %(n,t))


# from _typeshed import SupportsRead
# from typing import List


# c1=float(input("請輸入第一邊長"))
# c2=float(input("請輸入第二邊長"))
# c3=float(input("請輸入第三邊長"))
# while (c1!="q" or c2!="q" or c3!="q"):
#     if c1>c2 and c1>c3:
#         b=c1
#         s1=c2
#         s2=c3
#     elif c2>c1 and c2>c3:
#         b=c2
#         s1=c1
#         s2=c3       
#     else:
#         b=c3
#         s1=c2
#         s2=c1
#     if b**2==s1**2+s2**2:
#         print("直角三角形")
#     elif b**2>s1**2+s2**2:
#         print("鈍角三角形")
#     elif b**2<s1**2+s2**2:
#         print("銳角三角形")
#     c1=float(input("請輸入第一邊長"))
#     c2=float(input("請輸入第二邊長"))
#     c3=float(input("請輸入第三邊長"))


# m1=m2=1
# q=int(input("請輸入一個數字"))
# while(q>m2):
#     m1+=1
#     m2*=m1  
# print("%i階層為%i大於%i"%(m1,m2,q))

"""
q2=int(input("輸入一個數"))
m1=0
m2=1
m3=21
r=1
while(q2>m1):
    m1+=2
while(q2>m2):
    m2+=2
while(q2>m3):
    m3=m3*r
    r+=1
a1=m1
a2=m2-2
a3=m3
if a1>a2 and a1>a3:
    print(a1)
    if a2>a3:
        print(a2)
        print(a3) 
    else:
        print(a3)
        print(a2)
elif a2>a1 and a2>a3:
    print(a2)
    if a1>a3:
        print(a1)
        print(a3) 
    else:
        print(a3)
        print(a1)
elif a3>a1 and a3>a2:
    print(a3)
    if a1>a2:
        print(a1)
        print(a2) 
    else:
        print(a2)
        print(a1)

x=int(input("請輸入帳號"))
y=int(input("請輸入密碼"))
while(x!=y):
    print("密碼錯誤")
    y=int(input("請輸入密碼"))
print("密碼正確")
"""
# n=int(input("輸入一個數"))
# i=1
# d=0
# ans=""
# while(n>i):
#     if n%i==0:
#         d+=1
#         ans=ans+str(i)+" "
#     i+=1

# if d==2:
#     print("%i是質數"%(n))
#     print("%i的因數有%s"%(n,ans))
# else:
#     print("%i不是質數"%(n))
#     print("%i的因數有%s"%(n,ans))

# tuple 不可改變內元素的陣列
# t1=1,2,3
# print(t1[0])

# t2=(1,2,3)
# a,b,c=t2    #a=1 b=2 c=3

# a=10
# b=20
# a,b=b,a
# list1=[1,2,3,4]

# t3=tuple(list1)
# print(t3)
# t4=(1,2,3,4)
# t5=(t4,5,6)
# print(t5)
# print(t5[1])    #結果為5
# print(t5[1][0]) #不正確
# t6=["xaxaz",] #沒有逗號會變成字串(單一資料)

# List2=[1,2,3,4,5]
# list3=["蘋果","草莓","香蕉"]
# #print(list[2])=print(list2[-1])
# list4=[("apex","1234")("peko","abcd")]
# # print  [0][0] [0][1]  [1][0] [1][1]

# list5=["班代","副班代","學藝"]
# #同型別
# for s in list5:
#     print(s,end=" ")
# #不同型別
# items=[12,"HAHA",True]
# i=1
# for item in items:
#     print(item)

# #成績對應
# s1=["國文","英文","數學"]
# s2=[90,80,100]
# for i in range(len(s2)):
#     print("%s成績:%d分" % (s1[i],s2[i]))
# i1=s1.index("英文")#=1
# s1=["國文","英文","數學","數學"]
# n=s1.count("數學")
# s3=["90","80","100"]
# s3[0]="100"
# #新增元素
# s4=["牛奶","咖啡豆","西瓜","鳳梨"]
# #1.append
# s4.append("加麵包")
# #2.insert
# s4.insert(3,"加蘋果")
# s4.insert(20,"蘋果")#放在最後面

# #索引值為負值
# l6=[1,2,3,4]
# l6.insert(-1,"-1")
# print(l6)

#範例
# s=[]
# t=ins=0
# while(ins!=-1):
#     ins=int(input("請輸入學生成績:"))
#     if(ins!=-1):
#         s.append(ins)
# print("共有%d學生"% (len(s)))
# for i in s:
#     t+=i
# average=t/(len(s))
# print("本班總成績:%d分，平均成績:%5.2f"% (t,average))
"""
#                                             刪除元素
#1 remove
s2=["蘋果","香蕉","西瓜","鳳梨"]
s2.remove("香蕉")
#2 pop(位置)
s2.pop(-1)
#3 del
del s2[0]
print(s2)

#範例
colors=["紅","橙","黃","綠","藍"]
while True:
    print("顏色有",colors)
    color = input("請輸入要刪掉的顏色")
    if(color==""):
        break
    n=colors.count(color)
    if(n>0):
        colors.remove(color)
    else:
        print(color,"不在串列中")
"""
#                                               排序
#sort()由小排到大
# list1=[3,8,10,9]
# list1.sort()
# print(list1)
# list3=sorted(list1,reverse=false)
# print(list3)
# #大到小
# #1         reverse()
# list1.reverse()
# print(list1)
# #2         
# list2=sorted(list1,reverse=True)
# print(list2)
# print(list1)

#                                              其他工具
#1 分隔字串split
# s1="你不好,我不好,他不好"
# list1=s1.split("不")
# print(list1)
# #2 join連結字串
# s2="AA".join(list1)
# print(s2)
# #3 replace
# s2=s1.replace("不","超")
# print(s2)
# #4 find()
# print(s1.find("你"))
# print(s1.find("你你"))
# #5 startwith(開始字串)
# str1="mmd"
# print(str1.startswith("m"))
# print(str1.startswith("n"))
# # # endwith(結尾字串)
# print(str1.endswith("d"))
# print(str1.endswith("t"))

# #範例
# n1=input("請輸入圖片名稱")
# if n1.endswith(".jpg") or n1.endswith(".JPG"):
#     print("是jpg圖檔")
# else:
#     print("不是jpg圖檔")

#                                            list和tuple互相轉換
# tuple1=(1,2,3,4)
# list1=list(tuple1)
# list1.append(8)

# list2=[1,2,3,4,5]
# tuple2=tuple(list2)
# tuple2.append(8)#不可行

#                                             字典(dict)
"""
#1字典名稱={1:v1,k2,v2}
dict1={}
dict2={"高科大":"nkust","高義大":"KMU"}
print(dict2)

#2字典名稱=dict([[k1,v1],[k2,v2],[k3,v3]...)
dict3=dict([["高科大","nkust"],["高義大","KMU"]])

#3字典名稱=dict(k1=v1,k2=v2...) k不能是數字
dict4=dict(高科大="nkust",高義大="KMU")

dict5= {"侯先生":900,"張小姐":300}
t1=list(dict5)
t2=list(dict5.items())
print(t1)#['侯先生', '張小姐']
print(t2)#[('侯先生', 900), ('張小姐', 300)]

print(dict5["侯先生"])#900
print(dict5["李小姐"])# 錯誤(keyError)
print(dict5.get("李小姐"))# none
print(dict5.get("李小姐","不存在"))#不存在

#修改
dict5["侯先生"]=650
dict5["猴先"]=1000 # 新增新的詞彙

# 刪除字典
# 1.指定特定元素 //語法:del 字典名稱[key]

lang = {"好":"Good","哈囉":"Hello"}
# del lang["哈囉"]

# 2.刪除字典所有元素 // 字典名稱.clear()
lang.clear()
print(lang)
# 3.刪除整個字典(不存在) // del 字典名稱
del lang
"""

# x1={"高雄市":9,"新北市":5,"台北市":4,"台南市":8,"台中市":6,"桃園市":7}
# city=input("輸入要查詢的六都名稱:")
# pm=x1.get(city)
# if pm==None:
#     print("六都中沒有"+str(city)+"城市!")
# else:
#     print(str(city)+"今天的PM2.5值為:"+str(x1[city]))

# dict1 = {"侯先生":900,"張小姐":800,"林小弟":30,"王小妹":30}
# print(dict1["侯先生"])
# print(dict1["侯小弟"])沒有這個東西

#                          get // key 不存在時，不會產生錯誤。回傳None
# print(dict1.get("侯小弟"))
# print(dict1.get("侯小弟","不在字典中"))

# 範例 (天氣)
# dict2 = {"春":"暖","夏":"熱","秋":"涼","冬":"冷"}
# name = input("輸入季節(春夏秋冬):")
# feeling = dict2.get(name)
# if feeling == None:
#     print("沒有"+name+"季節")
# else:
#     print(name+"天氣為:"+str(dict2[name]))


# 合併字典 // update
# lang1 = {"您好":"Hello"}
# lang2 = {"早安":"Good  Morning"}
# lang1.update(lang2)#會顯示在後面
# print(lang1)

#複製
#指向同一個字典物件
# lang3={"您好":"Hello"}
# lang4=lang3
# lang4["您好"]="Hi"
# print(lang4)    #結果{'您好': 'Hi'}
# copy()指向不同字典物件   結果同上
# lang3={"您好":"Hello"}
# lang4=lang3.copy()
# lang4["您好"]="Hi"

# keys & values
# dict3 = {"春":"暖","夏":"熱","秋":"涼","冬":"冷"}
# keys1 = dict3.keys()
# print(keys1)   dict_keys(['春', '夏', '秋', '冬'])
# print(keys1[0])

# keys2 = list(keys1)
# print(keys2[0])

# values1 = dict3.values()
# print(values1)
# print(values1[0])

# values2 = list(values1)
# print(values2[2])

# # items()
# lang1 = {"早安":"Good Morning","您好":"Hello"}
# lang2 = lang1.items()
# for ch, en in lang1.items():
#     print("中文為",ch,"英文為",en)

# # set 集合 // {}或set
# s = {1,2,3,4}

# s = set(('a',1,'b',2))

# s = set(['apple',1,'banana',2])

# s = set({"早安":"Good Morning","您好":"Hello"})


# #add and remove
# s = set("NKUST")
# s.add("z")
# s.remove("N")

# # set 運算
# a = set("NKUST")
# b = set("KMU")
# print(a|b)#聯集
# print(a&b)#交集
# print(a-b)#差集
# print(a^b)#互斥或

# a = set("123456")
# b = set("123")
# print(a|b)#聯集
# print(a&b)#交集
# print(a-b)#差集
# print(a^b)#互斥或


# # 集合的比較
# s1 = set("NKUST")
# s2 = set("NKUSTs")
# print(s1<s2)#真子集合
# print(s1<=s2)#子集合
# print(s1>=s2)#超集合
# print(s1>s2)#真超集合

"""
語法                                       副程式
def 函式名稱(參數1,參數2...)
    程式區塊
    [return回傳1,回傳2..]
"""
# def sayhello():
#     print("歡迎光臨")


# def min(a,b):
#     if a>b:
#         return b
#     else:
#         return a

# def area(width,height):
#     area = width*height
#     return area
# print(area(5,12))#60
# def area(width,height=12):
#     area = width*height
#     return area
# print(area(5))#同上
# def area(width=12,height):不可以放前面
#                                                全域變數 區域變數
# def s():
#     var1= 1
#     print(var1,var2) # 1 20 
# var1=10
# var2=20
# print(var1,var2) # 10 20

# def g():
#     global var1
#     var1=1
#     var2=2
#     print(var1,var2)# 1 2
# var1=10
# var2=20
# g()
# print(var1,var2)# 1 20 

# g=5
# def f1():   語法錯誤
#     print(g)
#     g=10

# def f1():       可以這樣寫
#     g=10
#     print(g)

# import 模組
# 1
#import random
#random.randint(參數) 可以有整數亂數

# 2
# from random import *
# randint(參數)

# 3
# import random as r  #幫他取名字
# r.randint(參數)
"""
import random as r
for i in range(6):
    print(r.randint(0,10),end="")#整數亂數
for i in range(6):
    print(r.randrange(0,12,2),end=" ")#偶數亂數

for i in range(6):
    print(r.choice[0,12,2,4,7],end=" ")#陣列內的亂數

for i in range(6):
    print(r.sample["abcdefg",8],end="")#隨機8個括號內的字

import guess1 #可以用別的檔案的副程式
c=guess1.f()
print(c)
import  guess1 as gs

import sys #顯示路徑
for path in sys.path:
    print(path)    
"""
#                                     檔案處理

content="""
 哭阿吸奶
 甚麼水平
"""
#開啟文檔
f=open("file2.text","w",encoding="UTF-8")# windiw中文字s大部分都是cp950 python內是用UTF-8
f.write(content)
f.close()
#讀取文檔
f=open("file2.text","r",encoding="UTF-8")
for line in f:
    print(line,end="")
f.close()
#寫入文檔
f=open("file2.text","a",encoding="UTF-8")
f.write(content)
f.close()
# 讀取另類寫法
with open("file2.txt","r",encoding="UTF-8") as f:
    contents=f.readlines()
    print(contents)
