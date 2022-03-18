str_list = list(input()) #문자열 입력 받아서 배열에 문자 하나씩 넣는 곳
print("키를 입력 (소문자만)")
key = list(input())   #키값 입력 받는 곳
str_ord = []  # 아스키 코드값 으로 저장하는 배열
key_ord = []  # 키 값을 아스키 코드로 저장 하는 배열
str_chr = []  # 문자로 저장하는 곳
print("1번 암호화 2번 복호화")
select = int(input())

for i in str_list:  # 문자를 아스키 값으로 변경하는 반복문
    str_ord.append(ord(i))
for i in key:  # 키를 아스키 값으로 변경하는 반복문
    key_ord.append(ord(i))
if (select == 1):  # 암호화  (M + key)mod 26
    for j in range(len(str_ord)):
        k = j % len(key)
        if (str_ord[j] >= ord('a') and str_ord[j] <= ord('z')):
            str_ord[j] -= ord('a')
            key_ord[k] -= ord('a')
            if (str_ord[j] + key_ord[k] < 0):
                str_ord[j] += 26
            str_ord[j] = (str_ord[j] + key_ord[k]) % 26
            str_ord[j] += ord('a')
            key_ord[k] += ord('a')
        if (str_ord[j] >= ord('A') and str_ord[j] <= ord('Z')):
            str_ord[j] -= ord('A')
            key_ord[k] -= ord('a')
            if (str_ord[j] + key_ord[k] < 0):
                str_ord[j] += 26
            str_ord[j] = (str_ord[j] + key_ord[k]) % 26
            str_ord[j] += ord('A')
            key_ord[k] += ord('a')
elif (select == 2) : # 복호화
    for j in range(len(str_ord)):
        k = j % len(key)
        if (str_ord[j] >= ord('a') and str_ord[j] <= ord('z')):
            str_ord[j] -= ord('a')
            key_ord[k] -= ord('a')
            if (str_ord[j] - key_ord[k] < 0):
                str_ord[j] += 26
            str_ord[j] = (str_ord[j] - key_ord[k]) % 26
            str_ord[j] += ord('a')
            key_ord[k] += ord('a')
        if (str_ord[j] >= ord('A') and str_ord[j] <= ord('Z')):
            str_ord[j] -= ord('A')
            key_ord[k] -= ord('a')
            if (str_ord[j] - key_ord[k] < 0):
                str_ord[j] += 26
            str_ord[j] = (str_ord[j] - key_ord[k]) % 26
            str_ord[j] += ord('A')
            key_ord[k] += ord('a')
for r in str_ord:
    str_chr.append(chr(r))
print(''.join(str_chr))