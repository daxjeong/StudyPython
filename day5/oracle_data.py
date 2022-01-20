# Oracle_data
# cx_oracle 설치 : pip install cx_oracle

import cx_Oracle as ora

# makedsn('호스트명/ip주소', portnum, '서비스명')
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 오라클 주소
# connect(user, password, dsn, encoding)
conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8') # 오라클 접속

# DB접속이 성공하면 Connection부터 Cursor() 메서드를 호출하여 객체를 가져옴
cur = conn.cursor() # 실행결과 데이터를 담을 메모리 객체(튜플 형태)

try:
    # for row in cur.execute('SELECT * FROM emp;'):
    #     print(row)
    # cur.execute('SELECT COUNT(*), \'sample\' FROM emp')
    cur.execute('SELECT COUNT(*) FROM emp')
    result = cur.fetchone()
    print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 15번라인 확인요 : {e}')
finally:
    cur.close() # 커서부터 닫기
    conn.close() # DB접속 닫기