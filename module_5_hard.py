import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hash(password)
        user = None
        for u in self.users:
            if u.nickname == nickname and u.password == hashed_password:
                user = u
                break
        if user:
            self.current_user = user
        else:
            print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for u in self.users:
            if u.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("Ни один пользователь не вошел в систему.")

    def add(self, *videos):
        for video in videos:
            exists = False
            for v in self.videos:
                if v.title == video.title:
                    exists = True
                    break
            if not exists:
                self.videos.append(video)
            else:
                print(f"Видео с названием '{video.title}' уже существует.")

    def get_videos(self, search_term):
        result = []
        for video in self.videos:
            if search_term.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = None
        for v in self.videos:
            if v.title == title:
                video = v
                break
        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Вы смотрите '{video.title}'")
        for second in range(video.time_now, video.duration):
            video.time_now = second + 1
            print(f"Секунда {video.time_now}")
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


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
