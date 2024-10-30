def make_car(manufacturer, model, **car_info):
    """stores info about a car in a dictionary"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model

    return car_info

car_0 = make_car(
    'mitsubishi',
    'galant es',
    color = 'red',
    windows = 'tinted'
)

print(car_0)