# 디비 처리, 연결, 해제, 검색어 가져오기 ,데이터 삽입
import pymysql as my

class DBHelper:
    '''
    멤버변수 : 커넥션
    '''
    conn = None

    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    멤버함수
    '''
    def db_init(self):
        self.conn = my.connect(
            host='localhost',
            user='root',
            password='1234',
            db='pythonDB',
            charset='utf8',
            cursorclass=my.cursors.DictCursor
        )

    def db_free(self):
        if self.conn:
            self.conn.close()

    # 검색 키워드 가져오기 => 웹에서 검색,
    def db_selectKeyword(self):
        # 커서 오픈
        # with => 닫기 처리를 자동으로 처리해 준다 = i/o 많이 사용
        rows = None
        with self.conn.cursor() as cursor:
            # Read a single record
            sql = "select * from tbl_keyword"
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        return rows

    def db_insertCrawlingData(self, title, price, area, contents, keyword):
        with self.conn.cursor() as cursor:
            # Create a new record
            sql = '''
            insert into `tbl_crawlingdata`
            (title, price, area, contents, keyword)
            values (%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (title, price, area, contents, keyword))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.conn.commit()
