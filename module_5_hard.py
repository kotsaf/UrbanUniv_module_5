from time import sleep

class User:
    """
    Класс пользователя, содержащий атрибуты: ник, пароль, возраст.
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return self.nickname


class Video:
    """
    Класс видео, содержащий атрибуты: название, продолжительность, возрастное ограничение.
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.videos = {}
        self.users_data = {}
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users_data:
            if hash(password) == self.users_data[nickname].password:
                self.current_user = self.users_data[nickname]
                return
        print('Неправильный логин или пароль')


    def register(self, nickname, password, age):
        if nickname in self.users_data:
            print(f'Пользователь {nickname} уже существует')
            return
        user = User(nickname, password, age)
        self.users_data[nickname] = user
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            self.videos[video.title] = video

    def get_videos(self, search):
        found_videos = []
        for video_title in self.videos.keys():
            if search.lower() in video_title.lower():
                found_videos.append(video_title)
        return found_videos


    def watch_video(self, video_title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        video = self.videos.get(video_title)
        if not video:
            return
        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return
        for sec in range(1, video.duration + 1):
            print(sec, end=' ')
            sleep(1)
        print('Конец видео')


ur = UrTube()
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
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')