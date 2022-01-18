# if구문 - 흐름제어
# name = '하이'
# name = ['다정', '빠이', '하이'] # 리스트, 튜플 모두 가능
name = ('다정', '하이', '빠이', '념념')

# if name == '다정' or name == '빠이':
if '빠이' in name:
    print('의사를 만나러 갑니다.')
    print('의사썜한테 인사합니다.')
elif name == '하이':
    print('주사실로 갑니다.')
else:
    print('호출할때까지 대기합니다.')

x = 10
if x != 10:
    pass
else:
    pass
