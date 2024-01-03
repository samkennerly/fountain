# fountain

[Pure Python] example of an infinite [FizzBuzz] which can be [sliced].

<img
  alt="The Fountain"
  src="https://raw.githubusercontent.com/samkennerly/posters/master/fountain.jpeg"
  title="Together we will live forever.">

[Pure Python]: https://stackoverflow.com/questions/45976946/what-is-pure-python
[FizzBuzz]: https://blog.codinghorror.com/why-cant-programmers-program/
[sliced]: https://docs.python.org/3/glossary.html#term-slice


## abstract

Fountain is an example of several Python tricks:

- create a [callable] class
- run a module [as a script]
- run automated tests with [doctest]
- use [generators] to do [lazy evaluation]

[callable]: https://docs.python.org/3/reference/datamodel.html#object.__call__
[as a script]: https://docs.python.org/3/library/__main__.html#idiomatic-usage
[doctest]: https://docs.python.org/3/library/doctest.html
[generators]: https://docs.python.org/3/howto/functional.html#generators
[lazy evaluation]: https://en.wikipedia.org/wiki/Lazy_evaluation


# UNDER CONSTRUCTION


## basics

A `Fountain` object acts like a tuple of strings, except...

- `Fountain` objects have no `len()`.
- [Calling] a `Fountain` object returns a generator.
- Slices must have an endpoint. `[1:]` will raise an error.
- Negative-index elements like `[-3]` count backwards from 0.

[Calling]: https://docs.python.org/3/reference/datamodel.html#object.__call__


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
