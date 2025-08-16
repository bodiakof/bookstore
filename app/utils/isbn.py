from random import randint


def generate_fake_isbn():
    '''Generate a random 13-digit string that looks like ISBN.'''
    return ''.join(str(randint(0, 9)) for _ in range(13))
