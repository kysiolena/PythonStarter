from collections import namedtuple

if __name__ == '__main__':
    # «The Healthy Food»
    # ======= QUESTIONS
    # What will You eat for breakfast?
    # What will You eat for lunch?
    # What will You eat for dinner?
    # ======= FOOD
    # 🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🫐🥝🍅🫒🥥
    # 🍦🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯
    # 🍖🍗🍞🍔🍟🍕🥐🥖🫓🥨🥯🥞🧇🧀🥩🥓🌭🥪🌮🌯🫔🥙🧆🥚🍿🍲
    # ======= RESULTS
    # 1. You're fit (30-40).
    # 2. You're getting there (41-60).
    # 3. You can do better (61-90).

    # Food tuple
    # +10 to weight
    fruits = ('🍇', '🍈', '🍉', '🍊', '🍋', '🍌', '🍍', '🥭', '🍎', '🍏', '🍐', '🍑', '🍒', '🍓', '🫐', '🥝', '🍅', '🫒', '🥥')
    # +30 to weight
    sweets = ('🍦', '🍧', '🍨', '🍩', '🍪', '🎂', '🍰', '🧁', '🥧', '🍫', '🍬', '🍭', '🍮', '🍯')
    # +20 to weight
    different = ('🍖', '🍗', '🍞', '🍔', '🍟', '🍕', '🥐', '🥖', '🫓', '🥨', '🥯', '🥞', '🧇', '🧀', '🥩', '🥓', '🌭', '🥪', '🌮', '🌯',
                 '🫔', '🥙', '🧆', '🥚', '🍿', '🍲')

    food = (fruits, sweets, different)

    # Your daily meal
    Daily_meal = namedtuple('DailyMeal', 'breakfast lunch dinner')

    print('Welcome to The Healthy Food game! 👋')

    while True:
        is_ready = input('Are you ready to play? (Yes/No)').lower()

        if is_ready == 'yes':
            print('Let\'s get started!')

            # Game process...

            meals = ('breakfast', 'lunch', 'dinner')
            weights = (10, 30, 20)

            daily_meal = tuple()

            for meal in meals:
                while True:
                    # Food group index
                    food_group = int(input(f'What will You eat for {meal}? (0 - fruits; 1 - sweets; 2 - different)'))

                    if food_group < len(food):
                        # Count of products on the row
                        PRODUCTS_IN_ROW_COUNT = 10

                        # Count of rows
                        rows_count = round(len(food[food_group]) / PRODUCTS_IN_ROW_COUNT)

                        for row in range(rows_count):
                            start_index = row * (PRODUCTS_IN_ROW_COUNT - 1)
                            end_index = start_index + (PRODUCTS_IN_ROW_COUNT - 1)
                            products_in_row = food[food_group][start_index:end_index]

                            products_in_row_str = ''
                            for index, product in enumerate(products_in_row):
                                products_in_row_str += f'| {product} ({start_index + index}) '

                            print(products_in_row_str)

                        while True:
                            # Food product index
                            food_product = int(input('Select a product by its number...'))

                            if food_product < len(food[food_group]):
                                daily_meal += ((weights[food_group], food[food_group][food_product]),)

                                print('Good choice!', food[food_group][food_product], sep=' ')

                                break

                            else:
                                continue

                        break
                    else:
                        continue

            daily_meal_named = Daily_meal(daily_meal[0], daily_meal[1], daily_meal[2])

            print('Your daily meal:')
            print(daily_meal_named.breakfast[1], daily_meal_named.lunch[1], daily_meal_named.dinner[1], sep=' | ')

            result = daily_meal_named.breakfast[0] + daily_meal_named.lunch[0] + daily_meal_named.dinner[0]

            print(f'Your result: {result}')

            if 30 >= result <= 40:
                print('👍 You\'re fit!')
            elif 41 >= result <= 60:
                print('👌 You\'re getting there.')
            else:
                print('👎 You can do better...')

            is_repeat = input('Do you want continue game? (Yes/No)').lower()

            if is_repeat == 'yes':
                continue
            elif is_repeat == 'no':
                print('Ok... Let\'s play another time!')

                # Game end
                break
            else:
                print('Sorry, but I don\'t understand you...')
        elif is_ready == 'no':
            print('Ok... Let\'s play another time!')

            break
        else:
            print('Sorry, but I don\'t understand you...')
    else:
        print('See you again!')
