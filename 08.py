def get_show_time(seconds):
    try:
        if seconds < 0:
            raise ValueError("Секунды не могут быть отрицательными")
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}" 
    except TypeError:
        print("Ошибка: функция принимает только числовые аргументы")
    
time = get_show_time()
print("Сейчас время: ", time)