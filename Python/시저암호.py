str_list = list(input()) #문자열 입력 받아서 배열에 문자 하나씩 넣는 곳
key = int(input())   #키값 입력 받는 곳
str_ord = []  # 아스키 코드값 으로 저장하는 변수
str_chr = []  # 문자로 저장하는 곳
for i in str_list:  # 문자를 아스키 값으로 변경하는 반복문
    str_ord.append(ord(i))

for j in range(len(str_ord)):
    if (str_ord[j] >= ord('a') and str_ord[j] <= ord('z')):
        str_ord[j] -= ord('a')
        if(str_ord[j] + key < 0):
            str_ord[j] += 26
        str_ord[j] = (str_ord[j]+key)%26
        str_ord[j] += ord('a')
    if (str_ord[j] >= ord('A') and str_ord[j] <= ord('Z')):
        str_ord[j] -= ord('A')
        if(str_ord[j] + key < 0):
            str_ord[j] += 26
        str_ord[j] = (str_ord[j]+key)%26
        str_ord += ord('A')
for r in str_ord:
    str_chr.append(chr(r))
print(''.join(str_chr))