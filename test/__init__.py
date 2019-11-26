"""
Repackage 1-line test for compatibility with various testing frameworks.
"""
import doctest

import fountain

def test_fountain():
    """ None: Raise error if any doctests failed. """
    assert not doctest.testmod(module).failed
    print("OK fountain")
