# Chapter 5: Debugging

## Raising Exceptions

In addition to handling Python exceptions with `try` and `except` statements, you can also raise your own exceptions in your code with `raise` statement

- The `raise` keyword
- A call to the `Exception()` function
- A string with a helpful error message passed to the `Exception()` function

Raising an exception is a way of saying, "Stop running this code, and move the program execution to the `except` statement”

For example, in the interactive shell, you enter: `raise Exception('This is the error message.')`. Since no `try` and `except` statements cover the `raise` statement, the program crashes and displays the exception’s error message. See a more detailed example in [boxPrint.py](boxPrint.py)

## Assertions

An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. We perform these sanity checks with `assert` statements. If the sanity check fails, the code raises an `AssertionError` exception

- The `assert` keyword
- A condition (that is, an expression that evaluates to `True` or `False`)
- A comma
- A string to display when the condition is `False`

In plain English, an assert statement says, “I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program”

Example #1

```python
>>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
>>> ages.sort()
>>> ages
[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
>>> assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age
```

Example #2

```python
>>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
>>> ages.reverse()
>>> ages
[73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
>>> assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
AssertionError
```

Unlike exceptions, your code should not handle `assert` statements with `try` and `except`; if an `assert` fails, your program should crash (failing fast)

Assertions are for **programmer errors**, not user errors. Assertions should fail only while the program is under development; a user should never see an assertion error in a finished program. For errors that your program can encounter as a normal part of its operation (such as a file not being found or the user entering invalid data), raise an exception instead of detecting it with an `assert` statement

## Logging

Logging is a great way to understand what’s happening in your program and in what order it’s happening. Python’s `logging` module makes it easy to create a record of custom messages that you write

Example: [factorialLog.py](factorialLog.py)

## Debugger

Find more in [Debugging and Profiling](https://docs.python.org/3/library/debug.html)