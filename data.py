# if
if 3 > 1 :
    print("3은 1보다 큽니다.")
    print("연산을 종료합니다.")
print("-"*30)
print("저는 들여쓰기를 하지 않은 라인입니다.")

# if와 elif
a = "정세림"
b = "b"

if a == b :
    print("두 사람의 이름은 같습니다.")
elif a != b :
    print("두 사람의 이름은 다릅니다.")

# '안녕하세요'를 입력할 경우 '반갑습니다'가 출력
text = input('부디 안녕하세요 입력해주세요 : ')

if text == '안녕하세요' :
    print('반갑습니다.')

# 크기 비교
num_1 = 10
num_2 = 3

if num_1 < num_2 :
    print('num_1 은 nim_2 보다 크기가 작습니다.')

elif num_1 == num_2 :
    print('num_1 은 nim_2 보다 크기가 같습니다.')

elif num_1 > num_2 :
    print('num_1 은 nim_2 보다 크기가 큽니다.')

# 정수 변환
num = int(input("임의의 숫자를 입력하세요."))
print(num, type(num), )

# if와 else
x = 4
if 5 < x < 10 :
    print(x)

else :
    print('NO')

# and, or
apple = '사과'
banana = '바나나'

if apple == '사과' or banana == '바나나' :
    print("문자열이 모두 정확합니다.")

# 리스트 안에 있는 값 조회 /if (리스트, 딕셔너리) in (조회할 값) : /
var = [1, 2, 3]

if 3 in var :
    print("YES")