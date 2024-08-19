# 猜數字遊戲
import random
import pyinputplus as pyip
min = 1
max = 100
count=0
target = random.randint(1, 100)
print("=============猜數字遊戲=================\n")
while True:
    count += 1
    keyin=pyip.inputInt(f"猜數字範圍{min}~{max}:",min=min,max=max)
    if keyin == target:
        print(f"唷呼!猜對了，答案是{keyin}")
        print(f"你猜了{count}次")
        break
    elif keyin>target:
        print(f"再小一點")
        max=keyin-1
    elif keyin<target:
        print(f"再大一點")
        min=keyin+1
    print(f"你已經猜錯了{count}次")

print("再見掰掰，應用程式結束")
