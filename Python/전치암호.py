block_size = 4
str = list(input()) # 평문 입력
ckey = [2,3,4,1]  # 암호화키
dkey = [4,1,2,3]  # 복호화키
block_num = 0
count = len(str) # 평문의 길이

if(len(str) % block_size >0): #블록이 딱 맞아 떨어지지 않은 경우 블록크기의 남은 부분을 x로 채움
    block_num = int(len(str) / block_size + 1)
    for i in range(len(str), block_num * block_size):
        str.append('x')
else:
    block_num = int(len(str) / block_size)

c_text = ['' for i in range(len(str))]  #암호문 길이 지정
d_text = ['' for i in range(len(str))]  #복호문 길이 지정

for j in range(block_num): #암호화
    for k in range(block_size):
        c_text[j * block_size + k] = str[j*block_size+(ckey[k]-1)]
print("암호문 : ", end='')
for i in  range(block_size*block_num):
	print(c_text[i], end='')
print('\n')
for j in range(block_num): #복호화
    for k in range(block_size):
        d_text[j * block_size + k] = c_text[j*block_size+(dkey[k]-1)]
print("복호문 : ", end='')
if (len(d_text) == count):
    for i in  range(len(str)):
	    print(d_text[i], end='')
else:
    d_text = d_text[:count]
    for i in range(count):
        print(d_text[i], end='')