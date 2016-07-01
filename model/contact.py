"""
"""

class Contact(object):
    def __init__(self,name,hpnum,email,addr):
        self.name = name
        self.hpnum = hpnum
        self.email = email
        self.addr = addr

    def to_string_(self):
        return  self.name + ";" + self.hpnum + ";" \
                + self.email + ";" + self.addr

if __name__ == "__main__":
    print("실행 모듈이 아닙니다")