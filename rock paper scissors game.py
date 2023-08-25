import random

pc_list = ['가위', '바위', '보']

count_win = 0
count_draw = 0
count_lose = 0

while True:
    random_numbar = random.randint(0, 2)
    pc = pc_list[random_numbar]

    user = input("가위,바위,보 중 하나를 택 하시오.")

    if user not in pc_list:
        print('보기 에서 골라 주세요.')
        continue

    print(f"내가{user}/pc가{pc}")

    if user == '가위':
        if pc == '가위':
            print("비김")
            count_draw = count_draw + 1
        elif pc == '바위':
            print("졌다")
            count_lose = count_lose + 1
        elif pc == '보':
            print("이겼다")
            count_win = count_win + 1

    elif user == '바위':
        if pc == '가위':
            print("이겼다")
            count_win = count_win + 1
        elif pc == '바위':
            print("비김")
            count_draw = count_draw + 1
        elif pc == '보':
            print("졌다")
            count_lose = count_lose + 1

    elif user == '보':
        if pc == '가위':
            print("졌다")
            count_lose = count_lose + 1
        elif pc == '바위':
            print("이겼다")
            count_win = count_win + 1
        elif pc == '보':
            print("비김")
            count_draw = count_draw + 1

    repay_continue = input('게임을 다시 시작하려면 1 아니라면 2 를 써주세요:')

    if repay_continue == '1':
        continue
    elif repay_continue == '2':
        break

print(f'승리 : {count_win} 무승부 : {count_draw} 패배 : {count_lose}')