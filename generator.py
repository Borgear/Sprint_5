import random

def generate_unique_email(): #Генерирует email по шаблону: имя_фамилия_номер_когорты_3цифры@домен
    
    digits = random.randint(100, 999)
    return f"Dmitry_Baryshev_41_{digits}@yandex.ru"

def generate_random_password(length=8): #Генерирует случайный пароль заданной длины

    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=length))
