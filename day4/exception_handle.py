
# ** 예외처리(Exception handling) **
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    res = a / b
    return res

print('사칙연산 시작')
a, b = 4, 1 
numbers = [3, 6, 9] # 리스트 생성
# 예외 처리 안하면 곱하기로는 넘어가지 못하고 중간에 비정상적으로 프로그램이 끝남
# try에는 예외가 발생할 코드를 except에는 예외가 발생했을 때 처리하는 코드를 넣음

try:
    print(f'나누기 결과 : {divide(a, b)}')
    res = int(numbers[1]) * 8
    num = int(input('수를 입력하세요'))
    
except ZeroDivisionError as e: # except : 예외처리
    print(f'나누기 예외. 추가처리1 {e}')
except IndexError as e:
    print(f'인덱스 예외. 추가처리2 {e}')
except ValueError as e:
    print(f'숫자만 넣기! {e}')
except Exception as e:
    print(f'알 수 없는 예외. 추가처리5 {e}')
finally: # 예외발생 상관없이 항상 수행되는 finally
    print(f'곱하기 결과 : {multi(a, b)}')
    print(f'  빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')

print('사칙연산 종료')


# ** <디버깅> **
# breakpoint(중단점) : 해당 라인 이전까지만 실행 = 빨간색 점으로 표시한 라인 전까지 코드가 실행되기를 원함
# F10: 프로시저 단위로 실행(한 라인씩 진행)
# F11: 한 단계씩 코드 실행(메서드 안으로 진행)
# F9 : 중단점 설정/해제
# F5 : 디버깅 시작 / 중단점까지 계속 진행하기
# Shift + F5 : 디버깅 중지
