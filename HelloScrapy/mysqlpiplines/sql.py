import pymysql

MYSQL_HOSTS='118.24.62.141'
MYSQL_USER='pei'
MYSQL_PASSWORD='123456'
MYSQL_DB='dingdian'
# 打开数据库连接
db = pymysql.connect(MYSQL_HOSTS, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
db.set_charset('utf8')   #防止中文乱码
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

class Sql:
    @classmethod
    def insert_book(cls,title,author,link,collect):
        sql = "insert into book ( title,author,link,collect) values('%s', '%s', '%s', '%d' )" % (title, author, link, collect)
        cursor.execute(sql)
        db.commit()
    @classmethod
    def select_book_title(cls,title):
        sql="select exists( select 1 from book where title='%s')"% (title)
        cursor.execute(sql)
        return cursor.fetchall()[0]