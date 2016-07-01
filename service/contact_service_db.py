"""

"""

import sqlite3

def regist_contact(contact):

    insert_query = "insert into contact values(?,?,?,?)"
    con = sqlite3.connect('conntact.db')

    cur = con.cursor()
    cur.execute(insert_query,('kim','010-3333-4444','kim@daum.net',41))
    con.commit()
    con.close()


def view_all_contact():
    """
    [
      [
        "name" = name,
        "hpnum" = hpnum,
        "email" = email,
        "addr" = addr
      ]
      [
         ..
      ]
    ]
    :return: list
    """

    contact_list = []
    with open('contact.dat', 'r') as f:
        while True:
            line = f.readline()
            if not line: break;
            a_dic = _to_dic(line)
            contact_list.append(a_dic)

    return contact_list


def _to_dic(line):
    line = line[:-1]
    dic = {}
    list = line.split(';')

    dic['name'] = list[0]
    dic['hpnum'] = list[1]
    dic['email'] = list[2]
    dic['addr'] = list[3]
    return dic

def modify_contact(name):
    pass

def remove_contcat(name):
    pass

def search_contcat(name):
    pass



if __name__ == "__main__":
    print("실행 모듈이 아닙니다")