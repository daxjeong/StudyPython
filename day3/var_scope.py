# 변수 라이프스코프
a = 10 # 전역변수

def vartest(x): # 지역변수
    x = x + 1
    return x

a = vartest(a)
print(a)
# print(x) : x는 def내에서만 쓸 수 있는 지역변수
