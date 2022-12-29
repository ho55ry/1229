# 12/29 정리
# open => 모드 1. 읽기 :r
#             2. 쓰기 :w ,x a
#                       write ( ) 줄바꿈x 직접
# read => read, readlines, readline
# close



# ------------------------------------------------------------------------------
# 파일 읽기 살펴보기
# ------------------------------------------------------------------------------
FILE_NAME='happy.txt'

# ------------------------------------------------------------------------------
# read() 파일안에 모든 내용 가져오기
# ------------------------------------------------------------------------------

fp=open(FILE_NAME, mode='r',encoding='utf-8')
allData=fp.read()
fp.close()

print(f'allData type => {type(allData)}\n{allData},{len(allData)} ')


# ------------------------------------------------------------------------------
# readlines() 파일 내용 줄 단위로 가져오기
# ------------------------------------------------------------------------------

fp=open(FILE_NAME, mode='r',encoding='utf-8')
allLines=fp.readlines()
fp.close()

print(f'allLines type => {type(allLines)}\n{allLines} ,{len(allLines)}')


# ------------------------------------------------------------------------------
# readline() 파일 내용 한 줄 가져오기
# ------------------------------------------------------------------------------

fp=open(FILE_NAME, mode='r',encoding='utf-8')
Line=fp.readline()
fp.close()
print(f'Line type => {type(Line)}\n{Line} ,{len(Line)}')

fp=open(FILE_NAME, mode='r',encoding='utf-8')
count=1
while True:
    line=fp.readline()
    if not line: break
    print(f'[line{count}] : {line}')
    count +=1
fp.close()
