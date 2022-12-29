# -----------------------------------------------------------------------------------------------
# 상속(Inheritance) - 재사용 및 기능 확장
# -----------------------------------------------------------------------------------------------
 
# -----------------------------------------------------------------------------------------------
# Point 데이터 타입 => 클래스
# - 클래스명
# Point2D
# - 속성/필드 
# 좌표 (x, y)
# - 기능/역할
# 점 찍기
# -----------------------------------------------------------------------------------------------
class Point2D:
    # 클래스 속성

    # 인스턴스 속성
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # 인스턴스 메서드
    def Pointing(self):
        print(f'({self.x}, {self.y})에 점 찍기')

    def Circle(self, color):
        print(f'({self.x}, {self.y})에 {color}색 동그라미 그리기')

    def Star(self,action):
        print(f'({self.x}, {self.y})에 {action} 별 그리기')

# 인스턴스 생성
P1=Point2D(8,8)
P1.Circle('red')
P1.Star('깜빡이는')

# -----------------------------------------------------------------------------------------------
# 3D 공간에 Point 데이터 타입 => 클래스
# - 클래스명
# Point3D
# - 속성/필드 
# 좌표 (x, y, z)
# - 기능/역할
# 점 찍기
# -----------------------------------------------------------------------------------------------

# class Point3D:  #상속 안받은거

#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

#     # 인스턴스 메서드
#     def Pointing(self):
#         print(f'({self.x}, {self.y}, {self.z})에 점 찍기')

#     def Circle(self, color):
#         print(f'({self.x}, {self.y}, {self.z})에 {color}색 동그라미 그리기')

#     def Star(self,action):
#         print(f'({self.x}, {self.y}, {self.z})에 {action} 별 그리기')

# PP1=Point3D(8,8,8)
# PP1.Circle('blue')
# PP1.Star('반짝이는')

# -----------------------------------------------------------------------------------------------
# Point2D 클래스 상속 받음 
# 부모클래스/슈퍼클래스 : Point2D
# 자식클래스/서브클래스 : Point3D
# 상속 관계 사용되는 키워드 : super
# -----------------------------------------------------------------------------------------------
class Point3D(Point2D):  

    # 인스턴스 생성 및 속성 초기화
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z

    # 부모 클래스한테 상속받은 메서드 구현 부분을 변경 => 오버라이딩(overriding)
    # 메서드명, 매개변수 => 동일
    # 기능 구현 코드 => 변경
    def Pointing(self):
        print(f'({self.x}, {self.y}, {self.z})에 점 찍기')

    def Circle(self, color):
        print(f'({self.x}, {self.y}, {self.z})에 {color}색 동그라미 그리기')

    def Star(self,action):
        print(f'({self.x}, {self.y}, {self.z})에 {action} 별 그리기')

PP1=Point3D(8,8,8)
PP1.Pointing()
PP1.Star('깜빡이는')

