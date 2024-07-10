# 연습문제 6
text = input('단어를 입력하세요 : ')
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

if text in fruit :
    print(fruit.values())

else :
    print("오답입니다.")