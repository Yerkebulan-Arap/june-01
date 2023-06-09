def get_sum(num1, num2, num3):
    try:
        n1 = int(num1)
        n2 = int(num2)
        n3 = int(num3)
    except ValueError:
        print("Ошибка! Вы должны ввести число")
    else:
        return (n1*100)+(n2*10)+n3
        
    
print(get_sum(5, "ad", 7))
    
