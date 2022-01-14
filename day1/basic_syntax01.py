# 주석
# 문자열 표현방법
print("'Hello, World'")
print("Hello, World")

# 숫자연산 출력
# print() 활용
print(3 + 4)

# 변수사용
a = '안녕하세요.'
b = '반갑습니다!!'
print(a)
print(b)
print(a, b, '정말?')

# 수학연산
print(5 + 6)
print(5 - 6)
print(5 * 6)
print(5 / 3)
print(5 // 3) # 정수로 나누는 것
print(5 % 3) #나머지
print(2 ** 10)

print(int(5 / 3)) #정수형
print(int('10'))
# print(int('ten')) 형변환 안됨

print(float(5))

## type 확인
print(type(10))
print(type(10.0))

## 괄호 (연산자 우선순위)
print( (2 + 3) * 5 )
print( 2 + (3 * 5) )