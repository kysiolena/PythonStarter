day_of_the_week = input('Enter day of the week: ')

match day_of_the_week.lower().capitalize():
    case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
        print('Сьогодні на роботу')
    case 'Saturday' | 'Sunday':
        print('Сьогодні вихідний')
    case _:
        print('Такого дня не існує')
