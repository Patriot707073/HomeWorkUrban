def send_email(message, recipient, sender="university.help@gmail.com"):
    domens = [".com", ".ru", ".net"] # список доменов

    if "@" not in recipient or "@" not in sender:# проверка на наличие "@" в recipient и sender.
        return (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    domain_valid = False
    for i in domens:
        if i in recipient and i in sender: # проверяю в переменных recipient и sender наличие доменов ".com", ".ru", ".net"
            domain_valid = True
            break

    if not domain_valid:
        return (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}: Некорректный домен")

    if recipient.lower() == sender.lower():
        return ("Нельзя отправить письмо самому себе!")

    if  sender == "university.help@gmail.com":
        return (f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return (f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
