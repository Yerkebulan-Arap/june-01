def get_sum(num):
    try:
        sum = num * (num + 1)//2
        return sum
    except TypeError:
        print("Ошибка!Вы должны ввести число")
        
print(get_sum(7))