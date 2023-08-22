'''
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

def check(x):
    if x % 50 == 0:
        return True
    else:
        return False

# функция на проверку кратности
def add(amount, n, count=0):
    if (check(n)):
        if count == 3:
            count = 0
            total = (amount + n) * 1.03
            print(total)
            return total, count
        else:
            count += 1
            total = amount + n
            print(total)
            return total, count
    else:
        print("Ошибка ввода, вводимая сумма не кратна 50")
        return amount, count

# функция на расчет комиссии
def calc_commission(n):
    if n * 0.015 < 30:
        return 30
    elif n * 0.015 > 600:
        return 600
    else:
        return n * 0.015


def take_off(amount, n, count=0):
    if (check(n) and amount > n):
        if count == 3:
            count = 0
            total = ((amount - n) - calc_commission(n)) * 1.03
            if total < 0:
                print("Ошибка ввода, total < 0")
                return amount, count
            print(f'Комиссия за 3ю операцию {total}')
            return total, count
        else:
            count += 1
            total = (amount - n) - calc_commission(n)
            if total < 0:
                print("Ошибка ввода, total < 0")
                return amount, count
            print(f'Комиссия за 3ю операцию {total}')
            return total, count
    else:
        print("Ошибка ввода, снимаемая сумма не кратна 50 или снимаемая сумма больше суммы на счете")
        return amount, count


amount = 0
count = 0
main_flag = True
while main_flag:
    s = int(input("Введите действие: 1 - добавить; 2 - снять; 3 - выйти: "))
    if s == 1:
        n = int(input("\nВведите сумму добавления, кратную 50: "))
        amount, count = add(amount, n, count)
    elif s == 2:
        n = int(input("\nВведите сумму снятия, кратную 50: "))
        amount, count = take_off(amount, n, count)
    else:
        break

    