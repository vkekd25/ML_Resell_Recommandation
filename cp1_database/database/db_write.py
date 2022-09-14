import psycopg2
import csv
from tqdm import tqdm

#연동하기
conn = psycopg2.connect(
    host='heffalump.db.elephantsql.com', 
    dbname='hezwfjbb',
    user='hezwfjbb',
    password='bwf3k0irq7kZDzoMrnUV2ZXxRD7fXkhZ',
    port=5432)

#커서 생성
cur=conn.cursor()

#명령 실행

cur.execute("DROP TABLE IF EXISTS Product;")

cur.execute('''CREATE TABLE Product(
    title text,
    price float,
    article text,
    likes integer,
    view integer,
    category text,
    location text,
    time float,
    web_types integer,
    unused integer,
    model text,
    series text,
    size text,
    gps_cell text,
    edition text,
    material text,
    like_views_percentage float,
    quality text,
    average_price float,
    attention float,
    likes_per float,
    view_per float,
    attention_per float);''')

# conn.commit()

with open(r'C:\Users\woals\AI_13\qqq\database\realdf.csv','r', encoding='UTF8') as f:
    reader = csv.reader(f)
    next(reader)

    for row in tqdm(reader):
        cur.execute('''INSERT INTO Product(
            title,
            price,
            article,
            likes,
            view,
            category,
            location,
            time,
            web_types,
            unused,
            model,
            series,
            size,
            gps_cell,
            edition,
            material,
            like_views_percentage,
            quality,
            average_price,
            attention,
            likes_per,
            view_per,
            attention_per) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)''', 
            (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
            row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23]))

#명령 실행
# cur.execute("DROP TABLE IF EXISTS galaxywatch_D;")

# cur.execute('''CREATE TABLE galaxywatch_D(
#     manner_degree float,
#     title text,
#     price float,
#     likes integer,
#     chat integer,
#     view integer,
#     category text,
#     time float,
#     article text,
#     total_area_revised varchar);''')
            
# with open(r'C:\Users\woals\AI_13\qqq\best_used_item_price\Carrot_Galaxywatch.csv','r', encoding='UTF8') as f:
#     reader = csv.reader(f)
#     next(reader)
    
#     for row in tqdm(reader):
#         cur.execute('''INSERT INTO galaxywatch_D(
#              manner_degree,
#             title,
#             price,
#             likes,
#             chat,
#             view,
#             category,
#             time,
#             article,
#             total_area_revised) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
#             (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))


# #명령 실행
# cur.execute("DROP TABLE IF EXISTS applewatch_bun;")

# cur.execute('''CREATE TABLE applewatch_bun(
#     title text,
#     price text,
#     likes integer,
#     view integer,
#     article text,
#     category text,
#     location text,
#     link text);''')
            
# with open(r'C:\Users\woals\AI_13\qqq\best_used_item_price\test_2789.csv','r', encoding='UTF8') as f:
#     reader = csv.reader(f)
#     next(reader)
    
#     for row in tqdm(reader):
#         cur.execute('''INSERT INTO applewatch_bun(
#             title,
#             price,
#             likes,
#             view,
#             article,
#             category,
#             location,
#             link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', 
#             (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

# #데이터 출력
# cur.execute('SELECT * FROM applewatch')
# print(cur.fetchone())

#데이터 변경후 커밋
conn.commit()

#커서 닫기
cur.close()
conn.close()