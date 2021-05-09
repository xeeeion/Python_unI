def ask_password():
    password = "password"

    for i in range(3):
        data = input()
        if data == password:
            print("Пароль принят")
            return
    print("В доступе отказано")
