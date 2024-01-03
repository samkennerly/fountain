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

Fountain objects generalize this problem such that Fizz and Buzz multiples can be any integers, and the interval "1 to 100" can be any finite [range] or infinite [count].

[range]: https://docs.python.org/3/library/stdtypes.html?highlight=range#range
[count]: https://docs.python.org/3/library/itertools.html#itertools.count

The [fountain.py] module also demonstrates some other Python tricks:

- make objects [callable]
- run a module [as a script]
- run automated tests with [doctest]
- use [slots] to declare class attributes
- use [generators] to do [lazy evaluation]
- parse command-line arguments with [argparse]

[fountain.py]: fountain.py
[callable]: https://docs.python.org/3/reference/datamodel.html#object.__call__
[as a script]: https://docs.python.org/3/library/__main__.html#idiomatic-usage
[doctest]: https://docs.python.org/3/library/doctest.html
[slots]: https://wiki.python.org/moin/UsingSlots
[generators]: https://docs.python.org/3/howto/functional.html#generators
[lazy evaluation]: https://en.wikipedia.org/wiki/Lazy_evaluation
[argparse]: https://docs.python.org/3/library/argparse.html#argumentparser-objects


## basics

To run [fountain.py] as a script, open a terminal and type
```sh
python3 fountain.py
```

To see the help menu and command-line arguments, run `python3 fountain.py --help`.
```text
usage: fountain.py [-h] [--fizz FIZZ] [--buzz BUZZ] [start] [stop] [step]

Print numbers from [start] to [stop], in steps of size [step], but for multiples of 3
print 'Fizz' instead of the number, and for the multiples of 5 print 'Buzz'. For
numbers which are multiples of both 3 and 5 print 'FizzBuzz'.

positional arguments:
  start
  stop
  step

optional arguments:
  -h, --help   show this help message and exit
  --fizz FIZZ  Fizz multiplier (default is 3)
  --buzz BUZZ  Buzz multiplier (default is 5)
```

The `Fountain` class can also be imported into Python code:
```python
from fountain import Fountain

fizzbuzz = Fountain(fizz=3, buzz=5)
```

Call a `Fountain` to return a generator:
```python
for x in fizzbuzz(start=1, stop=10, step=1):
  print(x)
```

Call it again to generate new values with the same `fizz` and `buzz` multiples:
```python
for x in fizzbuzz(1, 101, 1):
  print(x)
```


## contents

[fountain.py] is a 1-page Python [module].

[fountain.py]: fountain.py
[module]: https://docs.python.org/3/tutorial/modules.html


## dependencies

- Python 3

Tested with Python versions 3.5.9, 3.6.9, 3.7.5, 3.8.0.


## examples

Create a new `Fountain` object.
```
>>> soda = Fountain(fizz=2, buzz=3)
>>> soda
Fountain(fizz=2, buzz=3)
>>> soda.shape
(2, 3)
```

`Fountain` is almost a `Sequence`, but with one big difference:
```
>>> len(soda)
Traceback (most recent call last):
...
ZeroDivisionError: FizzBuzz forever
```

Get values one at a time with square brackets.
```
>>> soda[12]
'FizzBuzz'
>>> soda[-3]
'Buzz'
>>> soda[6_000_000_000_000_000]
'FizzBuzz'
>>> soda[6_000_000_000_000_001]
'6000000000000001'
```

Slicing with a valid endpoint returns a tuple of strings.
```
>>> soda[ :6]
('FizzBuzz', '1', 'Fizz', 'Buzz', 'Fizz', '5')
>>> soda[-6 : 0]
('FizzBuzz', '-5', 'Fizz', 'Buzz', 'Fizz', '-1')
>>> soda[100 : 0 : -13]
('Fizz', 'Buzz', 'Fizz', '61', 'FizzBuzz', '35', 'Fizz', 'Buzz')
>>> soda[int(1e12) + 1 : int(6e12) : int(1e12)]
('1000000000001', 'Buzz', '3000000000001', '4000000000001', 'Buzz')
```

Slicing with no endpoint is an error.
```
>>> soda[1:]
Traceback (most recent call last):
...
ValueError: endless slice
```

Calling a `Fountain` returns a generator.
```
>>> afew = soda(start=10,stop=2,step=-1)
>>> type(afew)
<class 'generator'>
>>> ' '.join(afew)
'Fizz Buzz Fizz 7 FizzBuzz 5 Fizz Buzz'
>>> ' '.join(afew)
''
```

Calling with stop=None returns an endless generator.
```
>>> forever = soda(start=1,stop=None)
>>> next(forever)
'1'
>>> [ next(forever) for x in range(5) ]
['Fizz', 'Buzz', 'Fizz', '5', 'FizzBuzz']
```

Beware of infinite loops when iterating over a Fountain.
Converting a `Fountain` to a `list`, `set`, `tuple`, etc. takes forever.
This example is slower than calling soda[9001], but it is safe:
```
>>> for i,x in enumerate(soda):
...     if i > 9000:
...         break
>>> x
'9001'
```

## faq

### Why is the docstring so long?

The long [docstring] includes information [doctest] needs to run tests.

[docstring]: https://peps.python.org/pep-0257/
[doctest]: https://docs.python.org/3/library/doctest.html

### What do the double underscores like `__call__` mean?

Methods with double-underscore names are Python [special methods].

[special methods]: https://docs.python.org/3/reference/datamodel.html#special-method-names
