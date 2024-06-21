## Style Guide

Docstrings should follow
[numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
convention. We encourage extensive documentation. The python code itself
should follow [PEP8](https://www.python.org/dev/peps/pep-0008/)
convention whenever possible: there are continuous integration tests
checking that! You can use linters to help you write your code following
style conventions. Linters are add-ons that you can run on the written
script file. We suggest the use of **flake8** for Python 3. Many editors
(Atom, VScode, Sublimetext, \...) support addons for online lintering,
which means you'll see warnings and errors while you write the code -
check out if your does!

Since we adopt [auto](https://intuit.github.io/auto/home.html), the PR
title will be automatically reported as part of the changelog when
updating versions. Try to describe in one (short) sentence what your PR
is about - possibly using the imperative and starting with a capital
letter. For instance, a good PR title could be:
`Implement support for <randomtype> files` or
`Reorder dictionary entries`, rather than `<randomtype> support` or
`reorders keys`.
