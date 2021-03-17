# 인사를 하는 함수 작성
# 1.나이가 10살 미만이면 '안녕'
# 2.나이가 10살에서 20살 사이면 '안녕하세요'
# 3.그 외에는 '안녕하십니까'
def sayHello(name, age):
  if age < 10:
    print("안녕," + name)
  elif age <= 20 and age >= 10:
    print("안녕하세요," + name)
  else:
    print("안녕하십니까," + name)

sayHello("정태", 8)
sayHello("경민", 20)
sayHello("상호", 40)

# 변수
x = 1
y = 2
print(x)
print(y)

z = "안녕 나는 파이썬이야!"
print(z)

# 타입
x = 1
y = 2
z = 1.2

print(x + y)
print(x - y)
print(x * y)
print(x % y)
print(x ** y)
print(x % y)  #mod = x를 y로 나눈후 남는 값

# 문자열
x = "hello"
y = 'bye'

z = """안녕하세요 파이썬
문자열 공부중인 김정태 입니다"""

print(x)
print(y)
print(z)

print(("안녕" + "잘 지내니 ?"))
print("너 혹시 몇살이니? " + str(27)) # 이런함수를 캐스팅이라고 한다

x = 4  # 숫자 타입
y = "4" # 문자 타입

print(str(x) + y) # str 문자타입으로 캐스팅해주면 에러가 나지않는다
print(x + int(y)) # int 정수타입으로 캐스팅해주면 에러가 나지않는다

# 불리안 : boolean

x = True
y = False

print(x)
print(y)

# 조건문

if 2 > 1:
  print("Hello")

if not 1 > 2:
  print("Hello")

if 0 > 0 or 2 > 1:
  print("Hello")

x = 3

if x > 5:
  print("Hello")
elif x == 3:
  print("Bye")
else:
  print("Hi")

# 함수
def chat(name1, name2):
  print("%s: 안녕? 넌 몇 살이니? " % name1)
  print("%s: 나 ? 나는 27살이야 "%name2)

chat("철수", "영희")
chat("경민", "정태")
