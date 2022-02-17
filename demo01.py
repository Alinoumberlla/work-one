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
name = str(input("请输入姓名:"))
age = int(input("请输入年龄:"))
sex = str(input("请输入性别:"))
a = {"name":name,"age":age,"sex":sex}
print(a)


