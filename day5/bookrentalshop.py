# bookrentalshop
# divtbl, membertbl
from __future__ import division
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

# divtbl에서 데이터 조회
def getAllDataFromDivtbl(conn):
    cur = conn.cursor()
    query = "SELECT * FROM divtbl"
    for row in cur.execute(query):
        print(row)

# divtbl에 새로운 데이터 입력
def setDataIntoDivtbl(conn, tup):
    cur = conn.cursor()
    query = '''INSERT INTO divtbl (division, names) 
                VALUES (:1, :2) '''
    cur.execute(query, tup)
    cur.close() # 없어도 가능
    conn.commit() # COMMIT 필수
    # conn.rollback #ROLLBACK;

# membertbl에서 일부데이터 가져오기
def getSomeDataFromMembertbl(conn):
    cur = conn.cursor()
    query = '''SELECT names, levels, addr, mobile, email 
                FROM membertbl
                WHERE addr LIKE '서울%'
                AND UPPER(email) LIKE '%@NAVER.COM'
                ORDER BY idx DESC'''
    for row in cur.execute(query):
        print(row)
    
    cur.close()

# membertbl에 신규회원 입력하기
def SetNewMemberIntoMembertbl(conn, tup):
    cur = conn.cursor()
    query = '''SELECT ROWNUM, idx
                FROM (
                    SELECT idx FROM membertbl
                    ORDER BY idx DESC  
                        ) 
                WHERE ROWNUM = 1''' # 서브쿼리 생성
    cur.execute(query)
    idx = cur.fetchone() 
    if idx is None: # 예외사항 - 데이터가 없는 경우의 에러 방지
        idx = 0
    else:
        idx = idx[1]

    intup = (idx+1, tup[0], tup[1], tup[2], tup[3])

    query = '''INSERT INTO membertbl 
                        (idx, names, levels, userid, password) 
                VALUES(:1, :2, :3, :4, :5)''' #idx는 자동으로 생성되는 값
    cur.execute(query, intup)
    conn.commit()

# membertbl에 새 데이터를 수정
def SetChangeMemberFromMembertbl(conn, tup):
    cur = conn.cursor()
    query = '''UPDATE membertbl
                  SET addr = :1
                    , mobile = :2
                    , email = :3
                WHERE idx = :4'''
    cur.execute(query, tup)
    cur.close()
    conn.commit()

# divtbl에 임의 데이터 삭제
def deleteDivision(conn, division):
    cur = conn.cursor()
    query = '''DELETE FROM divtbl WHERE division = :1'''
    # 데이터가 하나면 튜플로 변경 ,를 반드시 넣어줘야함!!!
    cur.execute(query, (division,)) 
    conn.commit()

if __name__ == '__main__':
    print('책 대여점 프로그램 시작')
    # 1. divtbl에서 데이터 조회
    print('책 장르 정보 조회')
    scott_con = myconn() #DB접속
    getAllDataFromDivtbl(scott_con)

    # 2. divtbl에 새로운 데이터 입력
    print('책 장르 정보 입력')
    division = input('구분코드를 입력 : ')
    names = input('장르명 입력 : ')
    tup = (division, names)
    setDataIntoDivtbl(scott_con, tup)
    print('정보 입력 성공')
   
    # 3. membertbl에서 데이터 조회
    getSomeDataFromMembertbl(scott_con)
   
    # 4. membertbl에 새로운 데이터 입력
    print('신규 회원 입력')
    names = input('이름 입력 : ')
    levels = input('레벨 입력(A~D) : ')
    userid = input('아이디 입력(최대20자) : ')
    password = input('패스워드 입력(최대20자) : ')
    tup = (names, levels, userid, password)
    SetNewMemberIntoMembertbl(scott_con, tup)
    print('신규회원 저장성공')
    
    # 5. membertbl에 새 데이터를 수정
    print('기존회원 수정')
    idx = input('변경회원번호 : ')
    addr = input('주소입력 : ')
    mobile = input('폰번호입력(-포함) : ')
    email = input('이메일입력 : ')
    tup = (addr, mobile, email, idx) # idx가 마지막에 들어가는 이유?
    SetChangeMemberFromMembertbl(scott_con, tup)
    print('기존회원 수정완료')

    # 6. divtbl에 임의 데이터 삭제
    print('책 장르정보 삭제')
    division = input('삭제 할 장르코드 입력 : ')
    deleteDivision(scott_con, division)
    print('책 장르정보 삭제성공')