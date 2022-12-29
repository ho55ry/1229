# 계산기 ver3

# ------------------------------------------------------------------------------------------------
# 계산기 프로그램 
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
        FILE_NAME='.myCalc.txt'
        fp=open(FILE_NAME, mode='a',encoding='utf-8')
        while True:
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
        if num==0:
            FILE_NAME='.myCalc.txt'
            fp=open(FILE_NAME, mode='a',encoding='utf-8')
            fp.write('-- [ error ] --\n값을 초기화합니다. 새로 입력해주세요.\n')
            fp.close()
            print('infinite!!\n값을 초기화합니다. 새로 입력해주세요.'); self.result=0
        else: self.result /= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result

ex=Calc()
ex.put()