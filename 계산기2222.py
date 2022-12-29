# ------------------------------------------------------------------------------------------------
# 계산기 프로그램 
# ------------------------------------------------------------------------------------------------

class Calc:
    def __init__(self,result=0):
        self.result=result

    def put(self,입력=0):
        print(f'결과 : {입력}')
        while True:
            입력=input('입력 : ')
            if 입력[0].isdigit():
                self.result=float(입력)
                if self.result==int(self.result): self.result=int(self.result)
                print(f'결과 : {self.result}')
            elif 입력[0]=='+' or 입력[0]=='-':
                if isinstance(float(입력[1:]),float):
                    print(f'결과 : {self.__add__(float(입력))}')
                else: print('잘못된 입력입니다. 다시 입력해주세요.')
            elif 입력[0]=='*':
                if isinstance(float(입력[1:]),float):
                    print(f'결과 : {self.__mul__(float(입력[1:]))}')
                else: print('잘못된 입력입니다. 다시 입력해주세요.')
            elif 입력[0]=='/':
                if isinstance(float(입력[1:]),float):
                    print(f'결과 : {self.__div__(float(입력[1:]))}')
                else: print('잘못된 입력입니다. 다시 입력해주세요.')
            elif 입력=='=':
                break
            else: print('잘못된 입력입니다. 다시 입력해주세요.')

    def __add__(self,num):
        self.result += num
        if self.result==int(self.result): return int(self.result)
        else: return self.result
    
    def __sub__(self,num):
        self.result -= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result
    
    def __mul__(self,num):
        self.result *= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result
   
    def __div__(self,num):
        if num==0:
            print(f'infinite!!\n값을 초기화합니다. 새로 입력해주세요.'); self.result=0
        else: self.result /= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result

ex=Calc()
ex.put()