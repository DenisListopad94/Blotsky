seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"{hours} часов")
print(f"{minutes} минут")
print(f"{remaining_seconds} секунд")
