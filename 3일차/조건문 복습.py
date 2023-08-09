#a = float(input('숫자를 입력해주세요.'))
#b = float(input('숫자를 입력해주세요.'))
#c = a/b**2
#if c < 18.5:
#    print('저체중')
#elif 18.5 <= c < 22.9:
#    print('정상')
#elif 24.9 > c >= 23:
#    print('과체중')
#elif 29.9 > c >= 25:
#    print('비만')
#else:
#    print('고도비만') 
 















import random
print("++++ 가위 바위 보 게임 ++++")
user = input("가위 바위 보 중에서 하나를 입력하세요 :")
com=random.randrange(1,4)
if com== 1:
    if user == '가위':
        print("User : %s vs Com : 가위 "%user)
        print("비겼습니다.")
    elif user == '바위':
        print("User : %s vs Com : 가위 "%user)
        print("이겼습니다")
    if user == '보':
        print("User : %s vs Com : 가위 "%user)
        print("졌습니다")
elif com== 2:
    if user == '가위':
        print("User : %s vs Com : 가위 "%user)
        print("비겼습니다.")
    elif user == '바위':
        print("User : %s vs Com : 가위 "%user)
        print("이겼습니다")
    if user == '보':
        print("User : %s vs Com : 가위 "%user)
        print("졌습니다")
elif com== 3:
    if user == '가위':
        print("User : %s vs Com : 가위 "%user)
        print("비겼습니다.")
    elif user == '바위':
        print("User : %s vs Com : 가위 "%user)
        print("이겼습니다")
    if user == '보':
        print("User : %s vs Com : 가위 "%user)
        print("졌습니다")
        