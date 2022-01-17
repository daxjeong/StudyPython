# 자료형
print(None)
print(type(None))

print(0 == None)
a = None
print(a)
print(type(a))

# 숫자형
금액 = 12_345_666
print(금액)

# 문자열형
bruce_eckel = 'Life is Short, You need python'
print(bruce_eckel)

bruce_eckel = '''Life is Short.
You need python
ㅎㅇㅎㅇㅎㅇ'''
print(bruce_eckel)

# 불형
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 999)
# print(val_sum = 10)

bl_true = True
print(bl_true) 
print(type(bl_true))
print(bl_true == True) # True
print(bl_true is True) # True

print(a is None) # True
print(val_sum is 1000) # True

# 의미가 있는 bool
print(bool(1)) # True
print(bool(0)) # False

# list
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)

b = [i for i in range(50, 101)]
print(b)

arr2 = ['Life', 'is', 'Short', 'U', 'need', 'Python', 3]
print(arr2)

arr3 = [[1,2,3], [4,5,6]] #2차원 배열
print(arr3)

arr4 = list() #빈리스트 != Noon
print(arr4)

# 튜플
Tuple1 = (1, 2, 3, 4, 5)
print(Tuple1)

# 딕셔너리
spiderman = { 'name' : '피터 파커', 'age' :  18, 
              'weapon' : '웹슈터' }
print(spiderman)

# 집합
set_int = set([1, 2, 3, 4, 5, 6, 7, 1, 2, 2])
print(set_int) # 중복값 배제
