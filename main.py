"""
main executable Moduel
"""
from model.contact import  Contact
import service.contact_service_db as svc

"""
def _init_contact():
    f = open("contact.dat","w")
    f.close()
"""

import sqlite3

def main():

    contact = Contact('han','011-3333-2222','han@daum.net',25)
    #svc.regist_contact(contact)
    #print('등록 완료')
    a_list = svc.search_contcat('han')
    print(a_list)

""""
    create_table_query = 'create table contact(name text, hpnum text, email text, age int);'
    insert_query = "insert into contact values(?,?,?,?)"
    con = sqlite3.connect('conntact.db')

    cur = con.cursor()
    #cur.execute(create_table_query)
    #cur.execute(insert_query,('kim','010-3333-4444','kim@daum.net',41))
    cur.execute('select * from contact')
    a_record = cur.fetchone()
    print(a_record[0])
    print(a_record)

    #print('insert ok..')
    #con.commit()

    con.close()
"""




if __name__  == "__main__":
    main()

