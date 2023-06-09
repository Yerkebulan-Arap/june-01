def get_vol_tank(d, h):
    try:
        volume = h * 3.14 * d/4
        return volume*1000
    except TypeError:
        print("Ошибка! Функция принимает только числовые аргументы")
    
result = get_vol_tank(15, 16)
print("Объем бака ", result, "литр")