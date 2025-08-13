# Не змогла реалiзувати побудову трикутника з рандомними висотою та шириною
triangle_width = 15
triangle_height = 8

for row in range(triangle_height):
    print(' ' * (triangle_height - 1 - row) + '*' * (1 + row * 2))
