class Car:
    차량번호 = '33나 7777'
    __제조사 = '현대' # private => 해당 요소가 선언된 클래스에서만 사용 가능. (자기 자신만 접근 가능) = 외부 클래스(mycar)에서 접근하지 못함
    색상 = '흰색'
    연료 = '가솔린'
    출고연도 = 2018

    def __init__(self, 차량번호, 색상) -> None:
        self.차량번호 = 차량번호
        self.색상 = 색상

    def __str__(self) -> str:
        return f'제 차는 {self.출고연도}년에 만들어진 {self.연료}차량입니다.'

    # private (__속성)
    def set제조사(self, 제조사):
        self.__제조사 = 제조사 # private => 함수 안에서만 접근 가능

    def 제조사확인(self):
        print(f'제조사는 {self.__제조사}')

    def 전진한다(self, level):
        print(f"{self.색상}차가 {level}단으로 앞으로 달린다.")
    
    def 후진한다(self):
        print("뒤로 달린다.")

    def 좌회전한다(self):
        print("왼쪽으로 달린다.")

    def 우회전한다(self):
        print("오른쪽으로 달린다.")

    def 멈춘다(self):
        print("멈춘다.")