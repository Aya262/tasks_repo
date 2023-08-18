import psycopg2

try:
    con=psycopg2.connect(user="aya",password="aya",
                         host="127.0.0.1",port="5432",
                         database="odoo16")
    cursor=con.cursor()
    cursor.execute("select name from product_template;")
    result=cursor.fetchall()
    for record in result:
        print(record)


except Exception as e :
    print("Exception : ",e)