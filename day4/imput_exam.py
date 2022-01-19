# 입력 테스트
a = input()
print(f'입력값은 {a}')

number = int(input('수를 입력하세요 : '))
print(number * 3)

# Escape Character 탈출문자(특수문자)
print('Life is \"short\". \r\nYou \t\bneed \'python\'.')
print('Life is short. \nYou need python.') #\n 문자열 안에서 줄을 바꿀 때
print('Life is short. \rYou need python.') #\r 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
print('Life is short. \tYou need python.') #\t 문자열 사이에 탭 간격을 줄 때
print('Life is short. \bYou need python.') #\b 백 스페이스
print('Life is short. \tYou need \'python\'.') #\' 작은따옴표(')를 화면에 표현




