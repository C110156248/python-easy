# while True:
#     a=input("請輸入檢測的字元(end結束)")
#     if a!="end":
#         b=input("檢測單一字元")
#         c=input("取代字元與取代次數")
#         print("字元%s出現%d次"%(b,a.count(b)))
#         print("取代後字串為%s"%(a.replace(b,c[0],int(c[1]))))
#     else:
#         print("檢測結束")
#         break


# q=input("處理方式1字典2串列")
# a=input("金")
# b=input("銀")
# c=input("銅")
# d=input("優")
# if q=="1":
#     ans={"金":a,"銀":b,"銅":c,"優":d}
#     for x,y in ans.items():
#         print("%s牌得到%s面"%(x,y))
# elif q=="2":
#     ans=["金",a,"銀",b,"銅",c,"優",d]
#     for i in range(0,8,2):
#         print("%s牌得到%s面"%(ans[i],ans[i+1]))


# a=[]
# for i in range(10):
#     b=int(input("請輸入第"+str(i+1)+"個數字"))
#     a.append(b)
# a.reverse()
# print("最大的數字是%s,%s,%s"%(a[0],a[1],a[2]))
# print("最小的數字是%s,%s,%s"%(a[9],a[8],a[7]))


# q=["red","blue","red","green"]

# t=10
# for i in range(10):
#     n=""
#     a=input("依序輸入4個字串(中間以空白鑑分開)")
#     b=a.split()
#     for j in range(4):
#         if q[j]==b[j]:
#             n+="1"
#         elif b[j] in q:
#             n+="2"
#         else:
#             n+="3"
#     if n!="1111":
#         t-=1
#         print(n)
#         print("共10次機會，還有%s機會"%(t))
#     else:
#         print("挑戰成功")
#         break
# if i ==9:
#     print("挑戰失敗")
