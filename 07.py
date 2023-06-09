def get_show_seconds(hours, minutes, seconds):
    try:
        h = int(hours)
        m = int(minutes)
        s = int(seconds)
    except ValueError:
        print("Ошибка! Вы должны ввести число")
    else:
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            return h*60*60+m*60+s
        else:
            print("Неправильный ввод данных")
            
seconds = get_show_seconds(12, "as", 45)
print("Сколько секундов: ", seconds)   
