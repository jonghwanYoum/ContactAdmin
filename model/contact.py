"""
"""

class Contact(object):
    def __init__(self,name,hpnum,email,age):
        self.name = name
        self.hpnum = hpnum
        self.email = email
        self.age = age

    def to_string_(self):
        return  self.name + ";" + self.hpnum + ";" \
                + self.email + ";" + str(self.age)

if __name__ == "__main__":
    print("실행 모듈이 아닙니다")