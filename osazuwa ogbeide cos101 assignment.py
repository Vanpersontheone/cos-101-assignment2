print('Name:Osazuwa vanpearson ogbeide')
print('matriculation number:BHU/24/04/09/0007')
print('')
print('a')


def calculate_resistance():
    v = float(input('what is the value for potential differnce'))

    i = float(input('what is the value for current'))

    resistance = v / i

    print('force is', resistance)


calculate_resistance()

print('b')


def calculate_volume():
    length = float(input('what is the value of length '))
    breadth = float(input('what is the value of breadth '))
    height = float(input('what is the value of height'))

    volume = length * breadth * height
    print('volume is ', volume, )


calculate_volume()

print('c : energy')


def calculate_energy():
    power = float(input('what is the value of power'))
    time = float(input('what is the value of time'))
    energy = power * time

    print('energy is', energy)


calculate_energy()

print('d : power')


def calculate_power():
    force = float(input('what is the value of force '))
    area = float(input('what is the value of area '))

    power = force / area

    print('power is ', power)


calculate_power()

print('e: pressure')


def calculate_pressure():
    force = float(input('what is the value of force'))
    area = float(input('what is the value of area'))
    pressure = force / area

    print('work is', pressure, )


calculate_pressure()
