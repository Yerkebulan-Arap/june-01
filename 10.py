def perfect_num(num):
    try:
        divisors = []
        for i in range(1,num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num
    except TypeError:
        print("Ошибка! Функция принимает только числовые аргументы")
        
def perfect_numbers(min, max):
    try:
        for num in range(min, max + 1):
             if perfect_num(num):
                 print(num)
    except TypeError:
        print("Ошибка! Введите число")
        
print(perfect_numbers())
