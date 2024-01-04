# fountain

[Pure Python] example of an infinite [FizzBuzz] generator.

<img
  alt="The Fountain"
  src="https://raw.githubusercontent.com/samkennerly/posters/master/fountain.jpeg"
  title="Together we will live forever.">

[Pure Python]: https://stackoverflow.com/questions/45976946/what-is-pure-python
[FizzBuzz]: https://blog.codinghorror.com/why-cant-programmers-program/


## abstract

The [classic FizzBuzz] problem is:
<blockquote>
Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
</blockquote>

[classic FizzBuzz]: https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/

Fountain objects generalize this problem: Fizz and Buzz multiples can be any nonzero integers, and "from 1 to 100" can be replaced by any finite [range] or infinite [count].

[range]: https://docs.python.org/3/library/stdtypes.html?highlight=range#range
[count]: https://docs.python.org/3/library/itertools.html#itertools.count

The [fountain.py] module also demonstrates some popular Python tricks:

- make objects [callable]
- run a [module] as a [script]
- run automated tests with [doctest]
- use [slots] to declare class attributes
- use [generators] to do [lazy evaluation]
- parse command-line arguments with [argparse]

[fountain.py]: fountain.py
[callable]: https://docs.python.org/3/reference/datamodel.html#object.__call__
[module]: https://docs.python.org/3/tutorial/modules.html
[script]: https://docs.python.org/3/library/__main__.html#idiomatic-usage
[doctest]: https://docs.python.org/3/library/doctest.html
[slots]: https://wiki.python.org/moin/UsingSlots
[generators]: https://docs.python.org/3/howto/functional.html#generators
[lazy evaluation]: https://en.wikipedia.org/wiki/Lazy_evaluation
[argparse]: https://docs.python.org/3/library/argparse.html#argumentparser-objects


## basics

### run as a script

Open a terminal and enter:
```sh
python3 fountain.py
```
[fountain.py]: fountain.py

To see the help menu and command-line arguments, run:
```sh
python3 fountain.py --help
```

### use as a class

Import the `Fountain` class and construct a new object:
```python
from fountain import Fountain

fizzbuzz = Fountain(fizz=3, buzz=5)
```

Call the object with `start`, `stop`, and/or `step` inputs to return a generator:
```python
for x in fizzbuzz(start=1, stop=10, step=1):
  print(x)
```

Call it again to return a new generator with the same `fizz` and `buzz` multiples:
```python
for x in fizzbuzz(start=10, stop=100, step=2):
  print(x)
```


### run all tests

Open a terminal and enter:
```sh
python3 -m doctest fountain.py
```

To see all test results, run `doctest` with the `--verbose` option:
```sh
python3 -m doctest -v fountain.py
```


## contents

[fountain.py] is a single-page module.

[fountain.py]: fountain.py


## dependencies

- Python 3.9.1+


## examples

Create a new Fountain:
```python
>>> f = Fountain(fizz=3, buzz=5)
>>> f
Fountain(fizz=3, buzz=5)
>>> f.shape
(3, 5)
```

Call it to return a generator:
```python
>>> first10 = f(start=0, stop=10, step=1)
>>> type(first10)
<class 'generator'>
```

Make a list from the generated values:
```python
>>> list(first10)
['FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz']
```

The generator is done generating elements, but...
```python
>>> list(first10)
[]
```

Calling the same object again returns a new generator:
```python
>>> second10 = f(start=10, stop=20, step=1)
>>> list(second10)
['Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19']
```

Arguments can be input with or without keywords:
```python
>>> third10 = f(20, 30, 1)
>>> list(third10)
['Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29']
```

Call with `step=3` to generate every 3rd result:
```python
>>> list(f(start=0, stop=20, step=3))
['FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'FizzBuzz', 'Fizz']
```

Call with negative `start`, `stop`, and/or `step` to generate backwards:
```python
>>> list(f(-1, -10, -1))
['-1', '-2', 'Fizz', '-4', 'Buzz', 'Fizz', '-7', '-8', 'Fizz']
```

Call with very large arguments:
```python
>>> list(f(1_000_000_001, 10_000_000_000, 2_000_000_000))
['1000000001', '3000000001', 'Fizz', '7000000001', '9000000001']
```

Call with `stop=None` to return an infinite generator:
```python
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
```

## faq

### Why is the docstring so long?

The long [docstring] includes information [doctest] needs to run tests.

[docstring]: https://peps.python.org/pep-0257/
[doctest]: https://docs.python.org/3/library/doctest.html

### What do the double underscores like `__call__` mean?

Methods with double-underscore names are Python [special methods].

[special methods]: https://docs.python.org/3/reference/datamodel.html#special-method-names
