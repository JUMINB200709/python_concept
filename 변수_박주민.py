# 2023.05.12
'''
a=float(input("a를 입력하세요:"))
b=int(input("b를 입력하세요:"))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
'''
'''
a=float(input("a를 입력하세요:"))
b=int(input("b를 입력하세요:"))

print("a=%d 입니다, b=%d입니다"%(11,12))
'''

name="파이썬"
age=15
height=170
print("안녕하세요 %s입니다.\n 나이는 %d, 키는 %d." %(age,name,height))

hope=int(input("희망하는 키를 쓰시오:"))
print("제이름은 %s입니다.\n 나이는 %d, 희망키는 %d" %(name,age,hope))
print("제이름은 {}입니다.\n 나이는 {}, 희망키는 {}" .format(name,age,hope))

tmp=hope-height

print("그럼 앞으로 %d 만큼 커야겠네요" %(hope-height))
print("그럼 앞으로 "+str(tmp)+"만큼 커야겠네요")
