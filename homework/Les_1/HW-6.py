"Home work 1-6"

#6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = (int(input("Введите результат первого дня пробежки в км ")))
b = (int(input("Введите желаемый результат в км ")))
result_day = 1
result_km = a
while result_km < b:
    a = a + a * 0.1
    result_day = result_day + 1
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_day)

