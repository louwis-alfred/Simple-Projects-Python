name = 'You name'
height_m = 1.7
weight_kg = 80

bmi = weight_kg / (height_m ** 2)

if bmi < 25:
    print('Not overweight')
else:
    print('Overweight')
