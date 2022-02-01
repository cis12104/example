
def momentum(mass, velocity):
    '''
    :param mass: mass of object in kg - float
    :param velocity: velocity of object in m/s - float
    :return: momentum of object in kg*m/s
    '''
    return (mass * velocity)

def kinetic_energy(mass, velocity):
    '''
    :param mass: mass of object in kg - float
    :param velocity: velocity of object in m/s - float
    :return: kinetic energy of object in
    '''
    return True

def main():
    mass = float(input('Enter the mass: '))
    velocity = float(input('Enter the velocity: '))
    print(f'Momentum is {momentum(mass, velocity)} UNITS')
    # .. similar for KE

main()