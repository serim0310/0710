# 연습문제 8
score = int(input('점수를 입력하세요 : '))

if 81 <= score <= 100 :
    print('A')

elif 61 <= score <= 80 :
    print('B')

elif 41 <= score <= 60 :
    print('C')

elif 21 <= score <= 40 :
    print('D')

elif 0 <= score <= 20 :
    print('E')