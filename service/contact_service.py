"""

"""

def regist_contact(contact):
    """
   contact.dat 로 주소록을 관리한다
    """
    # contact 객채를 스트링으로 변환
    # kim;010-1234-5678;kim@naver.com;seoul 형대로 변환해서 contact.dat로 저장한다
    contact_str = contact.to_string_()
    with open('contact.dat', 'a') as f:
        f.write(contact_str + '\n')



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