import time

class Urtube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.user = None

    def log_in(self,nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if hash(password) == self.users:
                    self.user = user
                    print('Авторизация успешна!')
                    return
            else:
                print('Не верный пароль!')
                return
        print('Не найден пользователь!')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.user = new_user
        print(f'Пользователь {nickname} зарегистрирован!')


    def log_out(self):
        self.user = None
        print('Вы вышли из системы')

    def add(self,*args):
        for i in args:
            self.videos.append(i)

    def get_videos(self,word):
        result_list = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                result_list.append(video.title)
        return result_list

    def watch_video(self, title):
        if self.user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.adult_mode and int(self.user.age) < 18:
                print('Доступ запрещён: это видео предназначено для пользователей старше 18 лет.')
                return
            if video.title == title:
                print(f'Начинается просмотр видео: {video.title}')
                video.show_info()
                return
        print(f'Видео с названием "{title} не найдено."')

class Video:
    def __init__(self,title,duration,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def show_info(self):
        for i in range(self.duration + 1):
            time.sleep(0.3)
            print(i)

class User:
    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

ur = Urtube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.user.nickname)
# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')