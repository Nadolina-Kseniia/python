import math


def calculate_volume(shape, a, b=0, c=0, precision=2):
    if shape == 'cube':
        volume = a ** 3
    elif shape == 'sphere':
        volume = (4 / 3) * math.pi * a ** 3
    elif shape == 'cylinder':
        volume = math.pi * a ** 2 * b
    elif shape == 'cone':
        volume = (1 / 3) * math.pi * a ** 2 * b
    elif shape == 'torus':
        volume = math.pi * a ** 2 * (b ** 2 + a ** 2)
    elif shape == 'paraboloid':
        volume = math.pi * a ** 2 * b ** 2
    elif shape == 'hyperboloid':
        volume = math.pi * a ** 2 * b ** 2
    elif shape == 'ellipsoid':
        volume = (4 / 3) * math.pi * a * b * c
    elif shape == 'parallelepiped':
        volume = a * b * c
    elif shape == 'trapezoid':
        volume = (a + b) * c / 2
    else:
        return "Неподдерживаемая фигура"

    return round(volume, precision)
