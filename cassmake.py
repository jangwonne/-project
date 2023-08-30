class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'선암은{self.name} 아이디 는{self.username}입니다.')

    def __repr__(self):
        return f'{self.name}님의 아이디 는{self.username}'


class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f'{self.author}님이 작성하신 {self.title}입니다.'


members = []

member1 = Member('1', '11', '111')
member2 = Member('2', '22', '222')
member3 = Member('3', '33', '333')

members.append(member1)
members.append(member2)
members.append(member3)

posts = []

post1 = post('안녕하세요', '반갑습니다', member1.name)
post2 = post('시행착오를', '격으면서', member1.name)
post3 = post('완성해', '나가가고 있습니다.', member1.name)
posts.append(post1)
posts.append(post2)
posts.append(post3)

post4 = post('제출시간은', '늦었지만', member2.name)
post5 = post('하나하나', '이해하며', member2.name)
post6 = post('완성해', '보는중입니다.', member2.name)
posts.append(post4)
posts.append(post5)
posts.append(post6)

post7 = post('그래도', '열심히', member3.name)
post8 = post('해설강의를', '보며', member3.name)
post9 = post('완성하면', '그것이 경험이겠죠', member3.name)
posts.append(post7)
posts.append(post8)
posts.append(post9)

for post in posts:
    if post.author == 'member1':
        print(post.title)

word = input()
for post in posts:
    if word in post.content:
        print(post.title)


def user():
    my_name = input('이름을 입력해주세요.')
    my_username = input('아이디를 입력해주세요.')
    my_password = input('비밀번호를 입력해주세요.')

    members.append(Member(my_name, my_username, my_password))


def post():
    my_title = input('게시글 제목을 입력해주세요')
    my_content = input('내룔을 입력해주세요.')
    my_name = input('이름을 적어주세요.')
    posts.append(post(my_title, my_content, my_name))


while True:
    print('어서오세요 환영합니다.')
    option = input('회원가입 : 1, 글작성 : 2, 모든글 보기 : 3, 모든 회원보기 : 4 를 눌러주세요:')
    if option == '1':
        user()
    elif option == '2':
        post()
    elif option == '3':
        print(post)
    elif option == '4':
        print(user)
