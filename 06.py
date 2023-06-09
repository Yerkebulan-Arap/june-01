def show_time_hour(hours, minutes=0, seconds=0):
    try:
        h = hours
        m = minutes
        s = seconds
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            return f"{h:02d}:{m:02d}:{s:02d}"
        else:
            print("Неправильные данные")
    except TypeError:
        print("Ошибка! Функция принимает только числовые аргументы")
        
time = show_time_hour(12, 59, 61)
print("Сейчас время: ", time)