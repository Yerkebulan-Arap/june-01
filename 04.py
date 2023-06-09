def get_sqr(width, height=None):
    try:
        data1 = int(width)
        data2 = int(height)
    except TypeError:
        print("Ошибка! Введите число")
    else:
        if data2 == None:
            return data1**2
        else:
            return data1 * data2
        
result = get_sqr(5, "0")
print("Результат: ", result)
            
        