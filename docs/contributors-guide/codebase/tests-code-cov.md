
## Automatic Testing

`physiopy` uses Continuous Integration (CI) to make life easier. In
particular, we use the [CircleCI](https://circleci.com/) platform to run
automatic testing! **Automatic tests** are cold, robotic, emotionless,
and opinionless tests that check that the program is doing what it is
expected to. They are written by the developers and run (by CircleCI)
every time they send a Pull Request to `physiopy` repositories. They
complement the warm, human, emotional and opinionated **user tests**, as
they tell us if a piece of code is failing. CircleCI uses
[pytest](https://docs.pytest.org/en/latest/) to run the tests. The great
thing about it is that you can run it in advance on your local version
of the code! We can measure the amount of code that is tested with
[codecov](https://docs.pytest.org/en/latest/), which is an indication of
how reliable our packages are! We try to maintain a 90% code coverage,
and for this reason, PR should contain tests! The four main type of
tests we use are:

1. Unit tests :

        Unit tests check that a minimal piece of code is doing what it
        should be doing. Normally this means calling a function with
        some mock parameters and checking that the output is equal to
        the expected output. For example, to test a function that adds
        two given numbers together (1 and 3), we would call the function
        with those parameters, and check that the output is 4.

2. Breaking tests

        Breaking tests are what you expect - they check that the program
        is breaking when it should. This means calling a function with
        parameters that are expected **not** to work, and check that it
        raises a proper error or warning.

3. Integration tests

        Integration tests check that the code has an expected output,
        being blind to its content. This means that if the program
        should output a new file, the file exists - even if it's empty.
        This type of tests are normally run on real data and call the
        program itself. For instance, documentation PRs should check
        that the documentation page is produced!

4. Functional tests

        If integration tests and unit tests could have babies, those
        would be functional tests. In practice, this kind of tests check
        that an output is produced, and *also* that it contains what it
        should contain. If a function should output a new file or an
        object, this test passes only if the file exists *and* it is
        like we expect it to be. They are run on real or mock data, and
        call the program itself or a function.