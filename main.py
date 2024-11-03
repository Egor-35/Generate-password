import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Введите длину пароля: "))

generated_password = ""

for _ in range(password_length):
    generated_password += random.choice(symbols)

print("Сгенерированный пароль:", generated_password)

generated_password = ""

pon=input("Вам понравился пароль Да или Нет: ")


if pon=="Нет":
    for _ in range(password_length):
        generated_password += random.choice(symbols)
    print("Новый сгенерированный пароль:", generated_password)
