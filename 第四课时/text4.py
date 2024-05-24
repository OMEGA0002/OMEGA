d1={'哈哈':'代表开心',
    '呜呜':'代表难过',
    '呃呃': '代表无语'}
while True:
    print("1.请输入你想了解的网络流行语：")
    print(2.当前收录的流行语总数)
    print("3.添加新的流行语")
    print("4.退出程序")
    choice=input("请选择操作选项(1-3):")
    if choice=='1':
        user=input("输入你要查询的词:")
    if user in d1:
    print("你查询的"+user+"含义如下")
    print(d1[user])
else:
    print("你查询的单词不在字典里")
