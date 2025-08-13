# https://www.rapidtables.com/calc/math/Cos_Calculator.html

import math

degrees = int(input('Enter number of degrees: '))
radians = math.radians(degrees)  # degrees * (math.pi / 180)

radians_available = math.pi
degrees_available = round(radians_available * 180 / math.pi)

if -radians_available <= radians <= radians_available:
    print(3 * radians)
    print('cos(3x) =', math.cos(3 * radians))
else:
    print(
        f'{degrees} is the wrong number! '
        f'Number of degrees must be smaller than or equal to {degrees_available} and greater than or equal to -{degrees_available}'
    )
