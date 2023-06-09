def compare_numbers(num1, num2):
    try:
        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1
        else:
            return 0
    except TypeError:
        print("Ошибка: функция принимает только числовые аргументы")
        
result = compare_numbers("2", 2)
print(result)