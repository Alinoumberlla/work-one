# """print("hello world!")# 字符串
# print(2333)# 整数
# print(2.333)# 小数
# print(True)# 布尔值 True False
# print(())# 元组
# print([])# 数组
# print({})# 字典
# """
# """
# 多行注释
# 多行注释

# print("哈哈",2333,2.333)
# print("哈哈"+"嘻嘻")# 字符串的拼接(只能相同的类型进行操作)
# print("哈哈哈"*100)
# print(((1+2)*100-99)/2)# 用来做数学运算
# print(((1+2)*100-9.9)/2)    
# print(2>3)
# """
# a = input("请输入:")
# print("input获取的内容:",a)

# 数据格式的转化 
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# print(type(None))
# a = int("2333")
# print(a)
# a = str("2333")
# print(type(a))
# a = str(input("请输入:"))
# b = str(input("请输入:"))
# print(a+b)
# a = float(1.1)
# b = float(2.21)
# print(a+b)
# a = "ikjiijiuio huiohaduihuiohad io ioadhoi"
# print(len(a)) #len()获取字符串长度
# a = "dhnihidhauihuiui hdiawuhidaiohdaowdih"
# b = "wdbnujbhauidbhuiawbgdiuagbrfiugbaui hwuiahgruigha iwurgaiurgui"
# print(len(a)+len(b)) #通过代码获取两段内容，并且计算他们两段长度之和
# a = len(input("请输入:"))
# b = len(input("请输入:"))
# print(a+b)

# #一维元组
# a = (1,2,3,4,5,4,5,4,5,"哈哈","xixi",True,False)
# # print(a[5])
# print(a.index(5)) #元组里获取查询内容的下标 (只能操作一维元组)
# print(a.count(4)) #元组里统计查询内容的数量 (只能操作一维元组)

#二维元组
# a = (1,2,3,4,5,4,5,4,5,"哈哈","xixi",True,False)
# b = (a,1,2,3,4,4,5,"哈哈","xixi",False)
# print(a.count(b[0][5]))
# print(b[:8])
# print(b[8:]) #切片 左闭右开

#数组 元组写好后不可修改，数组写好后可以修改
# a = [1,2,3,4,5,4,5,4,5,"哈哈","xixi",True,False]
# print(a)
# a.append("添加数据到最末尾")
# print(a)
# a.insert(3,"插入数据到下标位置")
# print(a)
# b = a.pop(9)
# b = a.pop(6)
# print(a)
# print(b)
# a.append("nihao")
# print(a)
# HH = ["nihao","很好"]
# a.extend(HH)
# print(a)
# a.remove(1)
# print(a)

#字典
# a = {"name":"张三",0:"哈哈","age":22}
# print(len(a))
# # 取值
# print(a["name"])
# b = a.get("name")
# print(b)
# print(a.get("name"))
# # 新增
# a ["hight"] = "175m"
# print(a)
# a.update(name = 2333)
# print(a)
# a.update(xueli = "大专")
# print(a)
# # 修改
# a ["name"] = "李四"
# print(a)
# a.update(name = 3333)
# print(a)
# #剪切
# b = a.pop("age")
# print(b)
# print(a)
# #删除 (数组和字典删除，元组不能修改)
# del (a["name"])
# print(a)
#数组同样使用del命令 如 del a[0]

#练习：获取用户输入的个人信息，并且存储到字典中。个人信息包括：name,age,sex
# x = str(input("请输入姓名:"))
# y = int(input("请输入年龄:"))
# z = str(input("请输入性别:"))
# a = {"name":x,"age":y,"sex":z}
# print(a)

# a = {"name":"x","age":"y","sex":"z"}
# a.update(name = str(input("请输入name:")))
# a.update(age = int(input("请输入age:")))
# a.update(sex = str(input("请输入sex:")))
# print(a)

#判断
# a = 1
# b = 2
# if a > b:
#     print(a)
# else:
#     print(b)

# age = int(input("请输入你的年龄:"))
# if age > 60:
#     print("你应该退休啦!")
# elif 30 < age <= 60:
#     print("你的责任很重吧!")
# elif 20 <= age <= 30:
#     print("要好好规划自己的未来呀!")
# else:
#     print("要好好学习呀!")

# a = 2
# b = 2.0
# print(id(a))
# print(id(b))
# print( a is not b)
# print(a==b)

# a = 1
# b = [1,2,3,4,5]
# c = [2,3,4,5,6]
# print(a in b)
# print(a not in b)
# print(a not in c)
# print(a in c)

# a = input("请输入:")
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄!")
#     exit()
# if a >= 5:
#     print("大")
# else:
#     print("小")

# a = 2.0
# if type(a) is str:
#     print("是字符串")
# elif type(a) is int:
#     print("是整形")
# else:
#     print("其他")

#循环 while
# a = 1
# while a < 10:
#     print("hahaha")
#     a = a + 1

#练习
"""
现在有10个学生成绩需要录入系统,
10个学生名字分别为张三,李四,王麻子,浪静,流云,嘻嘻,小梁,二狗,成平安,猪猪,亚索
并且名字和成绩需要对应上,而且大于60分和小于60分的需要分开存放。
"""

# a = {}
# b = {}
# c = ["张三","李四","王麻子","浪静","流云","嘻嘻","小梁","二狗","成平安","猪猪","亚索"]
# x = 0
# while x < 11:
#     score = int(input("请输入"+c[x]+"的成绩:"))
#     if score >= 60:
#         a[c[x]] = score
#     else:
#         b[c[x]] = score
#     x = x + 1
# print(a)
# print(b)
#想了一个小时的结果本来是只能循环不断更改a,b字典里面的值，不能新增。后来照着代码对着修改最终的结果。
#下面是老师写的代码

# highscore = {}
# lowscore = {}
# studentlist = ["张三","李四","王麻子","浪静","流云","嘻嘻","小梁","二狗","成平安","猪猪","亚索"]
# a = 0
# while a < len(studentlist):
#     score = int(input("请输入"+studentlist[a]+"的成绩:"))
#     if score >=60:
#         highscore[studentlist[a]] = score
#     else:
#         lowscore[studentlist[a]] = score
#     a = a + 1
# print("大于60的:",highscore)
# print("小于60的:",lowscore)

# highscore = {}
# lowscore = {}
# studentlist = ["张三","李四","王麻子","浪静","流云","嘻嘻","小梁","二狗","成平安","猪猪","亚索"]
# for i in studentlist:
#     score = int(input("请输入"+i+"的成绩:"))
#     if score >=60:
#         highscore[i] = score
#     else:
#         lowscore[i] = score
# print("大于60的:",highscore)
# print("小于60的:",lowscore)

# for循环  (遍历)
# a = ["张三","李四","王麻子","浪静","流云","嘻嘻","小梁","二狗","成平安","猪猪","亚索"]
# for i in a:
#     print(i)

# b = list(range(0,100)) #左闭右开
# print(b)
   
# b = range(50,60,2)
# for i in b:
#     print(i)

#练习 打印一个九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j,end="   ")
#     print()
        
#练习 通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
# a = range(30,0,-1)
# b = range(35,0,-1)
# c = range(3,0,-1)
# x = 0
# while x == 0:
#     for i in a:
#         print("红灯还有"+str(i)+"秒")
#     for j in b:
#         print("绿灯还有"+str(j)+"秒")
#     for k in c:
#         print("黄灯还有"+str(k)+"秒")

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i+"还有"+str(light[i]-j)+"秒")



#练习 使用代码实现一个注册的功能。用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
#     储存到字典中，{username ： password}

# while True:
#     username = input("请输入账号:")
#     if len(username) < 5 or len(username) > 8:
#             print("账号长度为5-8位,请重新输入")
#     else:
#         print("账号可用")
#         while True:
#                 password = input("请输入密码:")
#                 if len(password) < 6 or len(password) > 12:
#                     print("密码的长度为6-12位,请重新输入")
#                 else:
#                     print("密码可用")   
#                     print({username:password})
#                     exit()

# username = input("请输入账号:")
# password = input("请输入密码:")
# if len(username) >=5 and len(username) <=8:
#     if username[0] in "abcdefghijklmnopqrstuvwxyz":
#         if len(password)>=6 and len(password)<=12:
#             print("密码可用")
#             print({username:password})
#         else:
#             print("密码的长度为6-12位,请重新输入")
#     else:
#         print("账号首字母必须小写")    
# else:
#     print("账号长度为5-8位,请重新输入")

# for i in range(10):
#     if i ==4:
#         continue
#     print(i)
# #continue 越过某一次循环

# for i in range(10):
#     if i == 4:
#         break
#     print(i)
#break 直接跳过4后的循环

# #函数的定义
# def checkname(username):
#     if len(username) >=5 and len(username) <=8:
#         if username[0] in "abcdefghijklmnopqrstuvwxyz":
#             print("密码可用")
#         else:
#             print("账号首字母必须小写")    
#     else:
#         print("账号长度为5-8位,请重新输入")

# checkname("aihuih")

def jiafa():
    a = int(input("请输入第一个数字:"))
    b = int(input("请输入第二个数字:"))
    print(a+b)
jiafa()