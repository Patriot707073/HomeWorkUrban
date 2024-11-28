class User:
    def __init__(self, nickname, password, age):
        if isinstance(nickname, str):
            self.nickname = nickname
        else:
            raise ValueError("Nickname должен быть строкой")

        if isinstance(password, str):
            self.password = hash(password)
        else:
            raise ValueError("Password должен быть числом")

        if isinstance(age, int) and age >= 0:
            self.age = age
        else:
            raise ValueError("Age должен быть числом >= 0")

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError("Title должен быть строкой")

        if isinstance(duration, int) and duration >= 0:
            self.duration = duration
        else:
            raise ValueError("Duration должен быть числом >= 0")

        if isinstance(time_now, int) and time_now >= 0:
            self.time_now = time_now
        else:
            raise ValueError("Time_now должен быть числом >= 0")

        if isinstance(adult_mode, bool):
            self.adult_mode = adult_mode
        else:
            raise ValueError("Adult_mode должен быть True или False")

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return
        print("Неверный логин или пароль.")

    def log_out(self):
        if self.current_user:
            self.current_user = None

    def add(self, *videos):
        for video in videos:
            if any(existing_video == video for existing_video in self.videos):
                continue
            self.videos.append(video)

    def get_videos(self, search_term):
        search_term = search_term.lower()
        return [video.title for video in self.videos if search_term in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=" ", flush=True)
                print("Конец видео")
                video.time_now = 0
                return

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
