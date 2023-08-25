import random

max_count = 0

while True:
    print(f'최고 시도 횟수는{max_count}')
    random_number_answer = random.randint(1, 100)
    random_number_start = 1
    random_number_last = 100
    print('업 & 다운 게임')
    count = 0
    random_number = random_number_answer

    while True:

        try:
            if count == 10:
                print(f'10번의 기회를 모두 소진 정답은{random_number}입니다.')

            user = int(input('숫자를 적어 주세요.: '))
            count = count + 1
            if user < random_number_start or user > random_number_last:
                print('1~100의 숫자만 입력해 주세요.')

            if random_number_start <= user < random_number:
                print(f':{count}번째 도전')
                print('Up')

            elif random_number < user <= random_number_last:
                print(f':{count}번째 도전')
                print('Down')

            elif user == random_number:
                print(f'축하 합니다!{count}번 만에 정답!')
                if count < max_count:
                    max_count = count

                repay_continue = input('게임을 다시 시작하려면 1 아니라면 2 를 써주세요:')

                if repay_continue == '1':
                    continue
                elif repay_continue == '2':
                    break
        except:
            print('숫자가 맞는지 확인해 주세요.')

