# importing necessary libraries
import mysql.connector as ms
import pandas as pd

# connecting to sql
db = ms.connect(host="localhost", user="root",
                password="Kewal@123", database='bcx')
cursor = db.cursor()


def getData():
    sql = "SELECT * FROM card;"
    cursor.execute(sql)
    list = cursor.fetchall()
    # print("list", list)
    df = pd.read_sql(sql, con=db)
    # print(df)
    return list


# inserting into mysql the required columns
def insert_data(details):
    # print(details)
    sql = "insert into card (name, mobno, email, url, area, city, state, pincode, company_name, designation)values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (details['name'], details['mobno'], details['email'], details['url'], details['address'], details['city'], details['state'], details['pincode'], details['company'], details['desig'])
    # print(sql)
    cursor.execute(sql, values)
    db.commit()


# to update the data as per the user input
def update_data(id, name, mobno, email, url, address, city, state, pincode, company, desig):
    
    sql = "UPDATE card SET name = %s, mobno = %s, email = %s, url=%s, area=%s, city=%s, state=%s, pincode=%s, company_name=%s, designation=%s WHERE  id=%s"
    print("sql", name)
    values = (name, mobno, email, url, address, city, state, pincode, company, desig, id)
    cursor.execute(sql, values)
    db.commit()


# for deleting the required records from the db
def delete_record(id):
    sql = "DELETE from card where id = %s"
    cursor.execute(sql, (int(id), ))
    db.commit()
