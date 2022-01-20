# 커서에 접근하는 코드를 함수로 작성
import cx_Oracle as ora

def myconn(): # 함수선언은 main함수 위에서 하기
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 오라클에 대한 주소 정보
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8') # 오라클 접속 유저 정보
    return conn

def getAllData(conn): # conn객체를 매개변수 받아서 쿼리를 실행할 함수
    cur = conn.cursor() # 커서(일련의 데이터에 순차적으로 액세스할 때 검색 및 "현재 위치"를 포함하는 데이터 요소) 생성
    query = 'SELECT * FROM emp' # emp 테이블에서 데이터를 모두 가져오기
    for row in cur.execute(query): # emp 테이블의 커서가 위치하면서 모든 데이터를
        print(row) # 한줄씩 출력

def getNameAndJobData(conn):
    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp' #emp 테이블 ename, job
    cur.execute(query) # 실행
    while True: # 13개 돌아가기때문에 while문
        row = cur.fetchone() # 한 row(레코드)를 읽기
        if row is None:
            break
        else:
            print(row)

def getDeptName(conn, tup): 
    cur = conn.cursor()
    #query = f"SELECT * FROM dept WHERE deptno = {tup[0} AND loc = '{tup[1]}'"
    #query = "SELECT * FROM dept WHERE deptno = {0} AND loc = '{1}'".format(tup[0], tup[1])
    query = "SELECT * FROM dept WHERE deptno = :1 AND loc = :2" # DB는 1부터 시작 / 1번 위치에 입력된 숫자 커서
    cur.execute(query, tup)
    row = cur.fetchone() # Fetch : 커서에서 원하는 결과값을 추출하는 것
    print(row)


# __name__ : interpreter가 실행 전에 만들어 둔 글로벌 변수
if __name__ == '__main__': # 여기서부터 프로그램이 실행됨(시작 지점*) # 언더바 2개씩
    print('프로그램 시작')
    # 함수호출
    scott_con = myconn() # dsn, connect() 후 접속객체 conn 리턴
    
    print('emp 테이블 전체 조회(SELECT *)')
    getAllData(scott_con)
    print('emp 2개 컬럼 조회')
    getNameAndJobData(scott_con)

    no = input('1. 부서번호를 입력하세요 :')
    loc = input('2. 지역명을 입력하세요 :').upper()
    tup = (no, loc)
    # print(f'부서번호 : {no}, 지역 : {loc}')
    getDeptName(scott_con, tup)

    print('프로그램 종료')
