# ------------------------------------------------------------------------------------------------
# 계산기 프로그램 
# 기능
# - 입력, 더하기, 빼기, 곱하기, 나누기, 히스토리, = 입력시 종료
# ------------------------------------------------------------------------------------------------
#
# 계산기 시작시 디폴트값은 0으로 원하는 숫자 입력 or 디폴트값에 바로 연산가능
# 입력창에 +1 , -1 , *10 , /10 등 바로 입력
#
# ------------------------------------------------------------------------------------------------

class Calc:
    def __init__(self,result=0):
        self.result=result
        print(f'--- [ 계 산 기 ] ---')
        FILE_NAME='.myCalc.txt'
        fp=open(FILE_NAME, mode='w',encoding='utf-8') #히스토리 리셋 계속 추가하고 싶으면 mode='a'
        fp.close()

    def put(self,입력=0):
        print(f'결과 : {입력}')


        while True:
            FILE_NAME='.myCalc.txt'
            fp=open(FILE_NAME, mode='a',encoding='utf-8')
            입력=input('입력 : ')
            if 입력[0].isdigit():
                self.result=float(입력)
                if self.result==int(self.result): self.result=int(self.result)
                print(f'결과 : {self.result}')
                if self.result==int(self.result): self.result=int(self.result)
                fp.write(f'{self.result}\n')

            elif 입력[0]=='+' or 입력[0]=='-':
                if isinstance(float(입력[1:]),float):
                    if self.result==int(self.result): self.result=int(self.result)
                    fp.write(f'{self.result} {입력} ')
                    print(f'결과 : {self.__add__(float(입력))}')
                    if self.result==int(self.result): self.result=int(self.result)
                    fp.write(f'= {self.result}\n')
                else: print('잘못된 입력입니다. 다시 입력해주세요.')

            elif 입력[0]=='*':
                if isinstance(float(입력[1:]),float):
                    if self.result==int(self.result): self.result=int(self.result)
                    fp.write(f'{self.result} {입력} ')
                    print(f'결과 : {self.__mul__(float(입력[1:]))}')
                    if self.result==int(self.result): self.result=int(self.result)
                    fp.write(f'= {self.result}\n')
                else: print('잘못된 입력입니다. 다시 입력해주세요.')

            elif 입력[0]=='/':
                if isinstance(float(입력[1:]),float):
                    if 입력[1]=='0':
                        self.result=0
                        print('-- [ error ] --\n새로 입력해주세요')
                        fp.write(f'-- [ error ] --\n새로 입력해주세요\n0\n')
                    else:
                        if self.result==int(self.result): self.result=int(self.result)
                        fp.write(f'{self.result} {입력} ')
                        print(f'결과 : {self.__div__(float(입력[1:]))}')
                        if self.result==int(self.result): self.result=int(self.result)
                        fp.write(f'= {self.result}\n')
                else: print('잘못된 입력입니다. 다시 입력해주세요.')

            elif 입력=='=':
                fp.close()
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
        self.result /= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result

ex=Calc()
ex.put()