age=36
for i in range(3):
    guess=int(input("猜测的年龄:"))
    if(guess>age):
        print("猜大了")
    if(guess<age):
        print("猜小了")
    if(guess==age):
        print("猜对了")