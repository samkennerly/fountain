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

    Call a Fountain to return a generator:
    >>> first10 = f(start=0, stop=10, step=1)
    >>> type(first10)
    <class 'generator'>
    >>> list(first10)
    ['FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz']

    Call with step=3 to generate only every 3rd result:
    >>> list(f(start=0, stop=15, step=3))
    ['FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz']

    Call with step < 0 to generate values backwards:
    >>> list(f(0, -10, -1))
    ['FizzBuzz', '-1', '-2', 'Fizz', '-4', 'Buzz', 'Fizz', '-7', '-8', 'Fizz']

    Start, stop, and step can be arbitrarily large integers:
    >>> list(f(1_000_000_000, 6_000_000_000, 1_000_000_000))
    ['Buzz', 'Buzz', 'FizzBuzz', 'Buzz', 'Buzz']

    Call with stop=None to return an infinite generator:
    >>> endless = f(start=0, stop=None, step=1)
    >>> next(endless)
    'FizzBuzz'
    >>> next(endless)
    '1'
    >>> next(endless)
    '2'
    >>> next(endless)
    'Fizz'
    >>> next(endless)
    '4'
    >>> next(endless)
    'Buzz'
    """

    __slots__ = ("fizz", "buzz")

    def __init__(self, fizz=3, buzz=5):
        self.fizz = int(fizz)
        self.buzz = int(buzz)

    @property
    def shape(self):
        """(int, int): Fizz and Buzz intervals."""
        return (self.fizz, self.buzz)

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


if __name__ == "__main__":
    import argparse

    parsed = argparse.ArgumentParser()
    parsed.description = "Print numbers from [start] to [step], \
    in steps of size [step], but for multiples of 3 print 'Fizz' \
    instead of the number, and for the multiples of 5 print 'Buzz'. \
    For numbers which are multiples of both 3 and 5 print 'FizzBuzz'."

    arg = parsed.add_argument
    arg("start", nargs="?", default=1, type=int)
    arg("stop", nargs="?", default=101, type=int)
    arg("step", nargs="?", default=1, type=int)
    arg("--fizz", default=3, type=int, help="'Fizz' multiplier (default is 3)")
    arg("--buzz", default=5, type=int, help="'Buzz' multiplier (default is 5)")
    parsed = parsed.parse_args()

    fountain = Fountain(parsed.fizz, parsed.buzz)
    results = fountain(parsed.start, parsed.stop, parsed.step)
    print(*results)
