
def perfect_num(num):
    try:
        divisors = []
        for i in range(1,num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num
    except TypeError:
        print("Ошибка! Функция принимает только числовые аргументы")

print(perfect_num(6))