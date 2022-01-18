# 기본 for문
arr = range(1, 100)
for i in arr:
    print(f'{i:2.1f}')

# 튜플로 for문
arr2 = ('me', 'my', 'friend', 'jane')
for item in arr2:
    print(f'{item:>10}') # 우측 정렬

# for 합계
numbers = list(range(1, 21, 2)) # 1~20까지 홀수
# print(numbers) # 확인하기
res = 0
for item in numbers:
    res += item

print(f'{numbers[-1]} 까지의 총 합은 {res} 입니다.')

# 홀수짝수 구분
numbers = list(range(1, 21)) # 1~20까지 

for item in numbers:
    # if item % 2 == 0: # 짝수
    if item % 2 != 0: # 홀수    
        print(f'{item}은 홀수')
    

# 13이면 탈출break 또는 계속continue
numbers = list(range(1, 21)) # 1~20까지

for item in numbers:
    # if item > 12: 
    #     break # 반복문 끝내기

    if item == 15: # 15는 처리하지 않고 넘어감
        continue # 반복문 건너뛰기

    if item % 2 != 0: # 홀수    
        print(f'{item}은 홀수')
        

## 구구단
print('<구구단 프로그램>')
for i in range (2, 10): # 2 ~ 9
    if i == 8: # 8단 넘어가기
        continue
    print(f'{i}단 시작')
    for j in range(1 ,10): # 1 ~ 9
        print(f'{i} x {j} = {i*j:2d}', end='    ') #2d = 두자리 수 표현
    print() # == print('') # 한 줄 내리기

# inline for문
a = [1, 2, 3, 4]
result = [i * 3 for i in a]
print(result)
# 기존 for문
t = []
for i in a:
    t.append(i * 3)
print(t)