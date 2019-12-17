import cmath
from decimal import Decimal


def is_perfect_square(num, **kwargs):
    # Handle complex numbers
    if 'complex' in kwargs:
        sq_root = cmath.sqrt(num)
        return sq_root.real.is_integer() and sq_root.imag.is_integer()
    # Deal with added kwargs that do not set 'complex'
    if len(kwargs) > 0:
        raise TypeError
    # All negative non-complex numbers are False
    if num < 0:
        return False
    elif type(num) == int or type(num) == float or type(num) == Decimal:
        sq_root = Decimal(num).sqrt()
        return int(sq_root) ** 2 == num
    else:
        raise TypeError("Wrong type of value to check for perfect square!  Need INT or FLOAT!")

