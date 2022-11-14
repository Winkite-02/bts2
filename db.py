import sqlite3

# 연결
def dbcon():
    return sqlite3.connect('mydb.db')

# 데이터 삽입
def insert_data(name, email, phone, message):
    # Cursor 객체 생성
    conn = dbcon()
    c = conn.cursor()
    c.execute(f"INSERT INTO contact VALUES ('{name}', '{email}', '{phone}', '{message}')")
    conn.commit()
    conn.close()

# 데이터 불러 와서 출력
def select_data():
    contact_list = []
    conn = dbcon()
    c = conn.cursor()
    for row in c.execute('SELECT * FROM contact'):
        #print(row)
        contact_list.append(row)
    conn.close()
    return contact_list

#select_data()

# 테이블 생성
#c.execute("CREATE TABLE contact (name varchar(50), email varchar(50), phone varchar(50), message varchar(500))")

# 데이터 삽입
#c.execute("INSERT INTO contact VALUES ('우엉차', 'a@a.com', '010-1234-5678', '안녕하세요')")

# execute 에 db 에 적용
#conn.commit()

# 데이터 불러 와서 출력
#for row in c.execute('SELECT * FROM contact'):
#    print(row)

# 접속한 db 닫기
#conn.close()
