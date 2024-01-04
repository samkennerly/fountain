#!/usr/bin/env python3

from itertools import count


class Fountain:
    """
    Infinite version of the FizzBuzz game.

    Create a new Fountain:
    >>> f = Fountain(fizz=3, buzz=5)
    >>> f
    Fountain(fizz=3, buzz=5)
    >>> f.shape
    (3, 5)

    Call to return a generator:
    >>> first10 = f(start=0, stop=10, step=1)
    >>> type(first10)
    <class 'generator'>

    Make a list from the generated values:
    >>> list(first10)
    ['FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz']

    The generator is done generating elements, but...
    >>> list(first10)
    []

    calling the same object again returns a new generator:
    >>> second10 = f(start=10, stop=20, step=1)
    >>> list(second10)
    ['Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19']

    Arguments can be input with or without keywords:
    >>> third10 = f(20, 30, 1)
    >>> list(third10)
    ['Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29']

    Call with step=3 to generate every 3rd result:
    >>> list(f(start=0, stop=20, step=3))
    ['FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'FizzBuzz', 'Fizz']

    Call with negative start, stop, and/or step to generate backwards:
    >>> list(f(-1, -10, -1))
    ['-1', '-2', 'Fizz', '-4', 'Buzz', 'Fizz', '-7', '-8', 'Fizz']

    Call with very large arguments:
    >>> list(f(1_000_000_001, 10_000_000_000, 2_000_000_000))
    ['1000000001', '3000000001', 'Fizz', '7000000001', '9000000001']

    Call with `stop=None` to return an infinite generator:
    >>> gigafizzbuzz = f(1_000_000_000, stop=None, step=1)
    >>> next(gigafizzbuzz)
    'Buzz'
    >>> next(gigafizzbuzz)
    '1000000001'
    >>> next(gigafizzbuzz)
    'Fizz'
    >>> next(gigafizzbuzz)
    '1000000003'
    >>> next(gigafizzbuzz)
    '1000000004'
    >>> next(gigafizzbuzz)
    'FizzBuzz'
    """

    __slots__ = ("fizz", "buzz")

    def __init__(self, fizz=3, buzz=5):
        self.fizz = int(fizz)
        self.buzz = int(buzz)

    def __call__(self, start=1, stop=101, step=1):
        """Generator[str]: FizzBuzz values for selected range."""
        fizz = self.fizz
        buzz = self.buzz

        if stop is None:
            steps = count(start, step)
        else:
            steps = range(start, stop, step)

        for n in steps:
            yield ("Fizz" * (not n % fizz) + "Buzz" * (not n % buzz)) or str(n)

    def __repr__(self):
        """str: Reproducible representation."""
        return f"{type(self).__name__}(fizz={self.fizz}, buzz={self.buzz})"

    @property
    def shape(self):
        """(int, int): Fizz and Buzz intervals."""
        return (self.fizz, self.buzz)


if __name__ == "__main__":
    import argparse

    parsed = argparse.ArgumentParser()
    parsed.description = "Print numbers from [start] to [stop], \
    in steps of size [step], but for multiples of 3 print 'Fizz' \
    instead of the number, and for the multiples of 5 print 'Buzz'. \
    For numbers which are multiples of both 3 and 5 print 'FizzBuzz'."

    arg = parsed.add_argument
    arg("start", nargs="?", default=1, type=int)
    arg("stop", nargs="?", default=101, type=int)
    arg("step", nargs="?", default=1, type=int)
    arg("--fizz", default=3, type=int, help="Fizz multiplier (default is 3)")
    arg("--buzz", default=5, type=int, help="Buzz multiplier (default is 5)")
    parsed = parsed.parse_args()

    fountain = Fountain(parsed.fizz, parsed.buzz)
    results = fountain(parsed.start, parsed.stop, parsed.step)
    print(*results)
