#!/usr/bin/env python3

from itertools import count


class Fountain:
    """
    Sliceable infinite sequence of FizzBuzz values.
    A harmless toy. Might be useful for teaching.

    Create a new Fountain object.

    >>> soda = Fountain(fizz=2, buzz=3)
    >>> soda
    Fountain(fizz=2, buzz=3)
    >>> soda.shape
    (2, 3)

    Fountain is almost a Sequence, but with one big difference:

    >>> len(soda)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: FizzBuzz forever

    Get values one at a time with square brackets.

    >>> soda[12]
    'FizzBuzz'
    >>> soda[-3]
    'Buzz'
    >>> soda[6000000000000000]
    'FizzBuzz'
    >>> soda[6000000000000001]
    '6000000000000001'

    Slicing with a valid endpoint returns a tuple of strings.

    >>> soda[ :6]
    ('FizzBuzz', '1', 'Fizz', 'Buzz', 'Fizz', '5')
    >>> soda[-6 : 0]
    ('FizzBuzz', '-5', 'Fizz', 'Buzz', 'Fizz', '-1')
    >>> soda[100 : 0 : -13]
    ('Fizz', 'Buzz', 'Fizz', '61', 'FizzBuzz', '35', 'Fizz', 'Buzz')
    >>> soda[int(1e12) + 1 : int(6e12) : int(1e12)]
    ('1000000000001', 'Buzz', '3000000000001', '4000000000001', 'Buzz')

    Slicing with no endpoint is an error.

    >>> soda[1:]
    Traceback (most recent call last):
    ...
    ValueError: endless slice

    Calling a Fountain returns a generator.

    >>> afew = soda(start=10,stop=2,step=-1)
    >>> type(afew)
    <class 'generator'>
    >>> ' '.join(afew)
    'Fizz Buzz Fizz 7 FizzBuzz 5 Fizz Buzz'
    >>> ' '.join(afew)
    ''

    Calling with stop=None returns an endless generator.

    >>> forever = soda(start=1,stop=None)
    >>> next(forever)
    '1'
    >>> [ next(forever) for x in range(5) ]
    ['Fizz', 'Buzz', 'Fizz', '5', 'FizzBuzz']

    Beware of infinite loops when iterating over a Fountain.
    Converting a Fountain to a list, set, tuple, etc. takes forever.
    This example is slower than calling soda[9001], but it is safe:

    >>> for i,x in enumerate(soda):
    ...     if i > 9000:
    ...         break
    >>> x
    '9001'
    """

    __slots__ = ("fizz", "buzz")

    def __init__(self, fizz=3, buzz=5):
        self.fizz = int(fizz)
        self.buzz = int(buzz)

    shape = property(lambda self: (self.fizz, self.buzz))

    def __bool__(self):
        """ bool: Prevent bool() from calling __len__ and crashing. """
        return True

    def __call__(self, start=1, stop=101, step=1):
        """ Iterator[str]: Generate values for selected range. """
        fizz, buzz = self.fizz, self.buzz

        ints = count(start, step) if (stop is None) else range(start, stop, step)
        for i in ints:
            yield ("Fizz" * (not i % fizz) + "Buzz" * (not i % buzz)) or str(i)

    def __getitem__(self, i):
        """ str or Tuple[str,...]: Value(s) at selected index or slice. """

        if not isinstance(i, slice):
            return next(self(i, None, 1))

        start, stop, step = i.start or 0, i.stop, i.step or 1
        if stop is None:
            raise ValueError("endless slice")

        return tuple(self(start, stop, step))

    def __iter__(self):
        """ Iterator[str]: Values from 0 to forever. """
        return self(0, None, 1)

    def __len__(self):
        """ None: Raise error because math.inf is not an int. """
        raise ZeroDivisionError("FizzBuzz forever")

    def __repr__(self):
        """ str: Reproducible representation. """
        return "{}(fizz={}, buzz={})".format(type(self).__name__, *self.shape)

    def __reversed__(self):
        """ Iterator[str]: Values from 0 to minus forever. """
        return self(0, None, -1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
