# 함수 선언 및 사용

# 더하기 함수 선언
def add(a ,b):
    res = a + b

    return res

# 함수 사용
print(add(12345, 23455))

mid_val = add(3, 5)
print(mid_val * 3)

# 함수종류
# 1. 매개변수(입력값)이 없는 형태
def say_hello():
    return 'Hello!'

print(say_hello())
print(say_hello(), 'my friend')

val = say_hello()
print(val.replace('o!', '')) # replace 대체하기

#2. 결과값이 없는 형태
def say_hello(name):
    print(f'Hello~ {name}')
    # return None
    
say_hello('뇽안') # print 할 필요 없음. def 자체에 print가 있기 때문에.

#3. 둘 다 없는 형태
def say_goodbye():
    print('Bye bye~')

say_goodbye()

#4. 매개변수를 지정하는 경우
def multi(a, b):
    return a * b

print(multi(2, 9))
print(multi(7, 8))

# 5. 매개변수 개수가 가변적일 때
def plus(*args):
    res = 0
    for i in args:
        res += i

    return res
print(plus(1))
print(plus(1, 2, 3))
print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 6. 리턴 값이 두개 이상
def mul_and_div(x, y):
    mul = x * y
    div = x / y

    return (mul, div) # 튜플

(res1, res2) = mul_and_div(7, 8)
print(res1, res2)

def 사칙연산(x, y):
    return (x+y, x-y, x*y, x/y)

res1, res2, res3, res4 = 사칙연산(9, 5)
print(res1, res2, res3, res4)
print(type(사칙연산(1, 2)))