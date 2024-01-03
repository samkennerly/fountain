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
    >>> afew = f(start=0, stop=10, step=1)
    >>> type(afew)
    <class 'generator'>
    >>> list(afew)
    ['FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz']

    Call with stop=None to return an endless generator:
    >>> endless = f(start=0, stop=None, step=1)
    >>> next(endless)
    'FizzBuzz'
    >>> [next(endless) for x in range(6)]
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']

    Call with step=3 to print every 3rd result:
    >>> thirds = f(start=0, stop=15, step=3)
    >>> list(thirds)
    ['FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz']

    Call with very large steps:
    >>> gigafizzbuzz = f(0, 5_000_000_000, 1_000_000_000)
    >>> list(gigafizzbuzz)
    ['FizzBuzz', 'Buzz', 'Buzz', 'FizzBuzz', 'Buzz']
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
        """ Generator[str]: FizzBuzz values for selected range. """
        fizz = self.fizz
        buzz = self.buzz

        if stop is None:
            steps = count(start, step)
        else:
            steps = range(start, stop, step)

        for n in steps:
            yield ("Fizz" * (not n % fizz) + "Buzz" * (not n % buzz)) or str(n)

    def __repr__(self):
        """ str: Reproducible representation. """
        return f"{type(self).__name__}(fizz={self.fizz}, buzz={self.buzz})"


if __name__ == "__main__":

    import argparse

    parsed = argparse.ArgumentParser()
    parsed.description = "Print results of the FizzBuzz game."
    arg = parsed.add_argument
    arg("start", nargs="?", default=1, type=int, help="start at this number")
    arg("stop", nargs="?", default=101, type=int, help="stop before this number")
    arg("step", nargs="?", default=1, type=int, help="slice interval")
    arg("--fizz", default=3, type=int, help="'fizz' interval")
    arg("--buzz", default=5, type=int, help="'buzz' interval")
    parsed = parsed.parse_args()

    fountain = Fountain(parsed.fizz, parsed.buzz)
    print(*fountain(parsed.start, parsed.stop, parsed.step))
