# fountain

[FizzBuzz](https://blog.codinghorror.com/why-cant-programmers-program/) forever.

## abstract

Fountain is a toy example of:

- using [generators](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions) as
[lazy](https://en.wikipedia.org/wiki/Lazy_evaluation) lists
- using [itertools](https://docs.python.org/3/library/itertools.html) for performance
- [streaming](https://en.wikipedia.org/wiki/Stream_(computing)) infinite sequences
- testing with [doctest](https://docs.python.org/3/library/doctest.html)
- [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)

## basics

[fountain.py](src/fountain.py) is a 1-page Python [module](https://docs.python.org/3/tutorial/modules.html).
It can be imported or run as a script.

## contents

## dependencies

## examples

## faq

### What do the `__underscores__` mean?

The methods with double-underscore names are Python
[special methods](https://docs.python.org/3/reference/datamodel.html#special-method-names).

Special methods are also known as <q>magic methods</q> or <q>dunders</q>.

### Are all those <q>dunders</q> necessary?

No. The `Fountain` class is
[overengineered](https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/)
to demonstrate
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)
methods.
