# Person 클래스
class Person:
    name = '무명이' # 아직 이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''

    # 생성자
    def __init__(self, name, age, height, gender) -> None: # -> 리턴값 명세 # 초기화(initialize) 메서드, 클래스 생성시 자동으로 실행되는 메서드
        self.name = name
        self.age = age
        self.height = height
        self.gender= gender

        print('Person이 생성되었습니다.')

    def 소개한다(self) -> None:
        greeting = f'''안녕하세요 저는 {self.name} 입니다.
        {self.gender}이구요. {self.age}살입니다.
        '''
        print(greeting)

    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다.')

    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다.')
        #return None 생략


if __name__ == '__main__':
    # p = Person() # p라는 이름의 Person 객체 생성
    # print(type(p))
    # print(id(p)) # id값

    # p2 = Person() # p2 객체 생성
    # print(type(p2))
    # print(id(p2))e

    cdj = Person('최다정', 26, 164, '여자') # == __init__(self, name, age):
    # cdj.name = '최다정'
    # cdj.age = 26
    cdj.heihgt = 163.7
    # cdj.gender = 'female'
    cdj.feetsize = 235
    cdj.bloodtype = 'A'

    cdj.소개한다()
    cdj.먹는다('크로플')
    cdj.일한다('바닐라라떼')