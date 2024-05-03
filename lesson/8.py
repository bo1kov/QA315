sales = [int(input()), int(input()), int(input())]
premia = 200
for i in sales:
    if 0 <= i <= 500:
        manager = 200 + i * 0.03
    elif 500 < i <= 1000:
        manager = 200 + i * 0.05
    elif i > 1000:
        manager = 200 + i * 0.08

    best_manager = max(sales)
    best_manager_index = sales[best_manager]

print(rating[0], rating[1], rating[2]+200)

# sales1 = float(input("Введите уровень продаж первого: $"))
# sales2 = float(input("Введите уровень продаж второго: $"))
# sales3 = float(input("Введите уровень продаж третьего: $"))
# base_salary = 200
# if sales1 < 500:
#     salary1 = base_salary + (sales1 * 0.03)
# elif sales1 < 1000:
#     salary1 = base_salary + (sales1 * 0.05)
# else:
#     salary1 = base_salary + (sales1 * 0.08)
#
# if sales2 < 500:
#     salary2 = base_salary + (sales2 * 0.03)
# elif sales2 < 1000:
#     salary2 = base_salary + (sales2 * 0.05)
# else:
#     salary2 = base_salary + (sales2 * 0.08)
#
# if sales3 < 500:
#     salary3 = base_salary + (sales3 * 0.03)
# elif sales3 < 1000:
#     salary3 = base_salary + (sales3 * 0.05)
# else:
#     salary3 = base_salary + (sales3 * 0.08)
#
# salaries = [salary1, salary2, salary3]    # создаём переменную и присваеваем ей список
# best_salary = max(salaries)    # вычисляем максимальное значение и присваеваем его переменной
# best_index = salaries.index(best_salary)    # вычисляем индекс максимального значения
# prize = 200    # премия
# salaries[best_index] += prize
#
# print(f'Итоговая зарплата первого менеджера: ${salary1}')
# print(f'Итоговая зарплата второго менеджера: ${salary2}')
# print(f'Итоговая зарплата третьего менеджера: ${salary3}')
# print(f'Лучшему менеджеру начислена премия в $200: Менеджер {best_index +1}')

# sales = sorted([sales1, sales2, sales3])
# print(f"Лучший продавец продал на ${sales[-1]}, ему полагается премия $200")
# print(f"Продавец продавший на ${sales[0]}, получает )
# print(sales[1])


# НАДО ЗАКОНЧИТЬ!

