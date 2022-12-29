# -----------------------------------------------------------------------------------------------
# 다중 상속 
# -----------------------------------------------------------------------------------------------

class A:

    def __init__(self,aa):
        print('A.__init__() ')
        self.aa=aa

    def play(self):
        print(f'A.play() - {self.aa}하며 놀고 있다.')


class B:

    def __init__(self,bb,num):
        print('B.__init__() ')
        self.bb=bb
        self.num=num

    def play(self):
        print(f'B.play() - {self.bb} 신나 신나.')

# 자식 클래스
class C(A,B):
    pass
    #def play()
c1=C('게임')
c1.play()
                        # 부모 클래스 중에 앞에 있는거부터 받음
class D(B,A):
    pass
d1=D('TV',1)
d1.play()

class E(C):
    pass
e1=E('홀덤')
e1.play()