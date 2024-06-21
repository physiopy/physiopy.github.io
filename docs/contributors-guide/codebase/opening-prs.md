## Pull Requests

To improve understanding pull requests "at a glance" and use the power
of `auto`, we use the labels listed above. Multiple labels can be
assigned to a PR - in fact, all those that you think are relevant. We
strongly advise to keep the changes you're introducing with your PR
limited to your original goal. Adding to the scope of your PR little
style corrections or code refactoring here and there in the code that
you're already modifying is a great help, but when they become too much
(and they are not relevant to your PR) they risk complicating the nature
of the PR and the reviewing process. It is much better to open another
PR with the objective of doing such corrections! Moreover, if you're
tempted to assign more than one label that would trigger a release (e.g.
bug and minormod or bug and majormod, etc.), you might want to split your PR
instead. When opening a pull request, assign it at least one label.

We encourage you to open a PR as soon as possible - even before you
finish working on them. This is useful especially to you - so that you
can receive comments and suggestions early on, rather than having to
process a lot of comments in the final review step! However, if it's an
incomplete PR, please open a **Draft PR**. That helps us process PRs by
knowing which one to have a look first - and how picky to be when doing
so.

Reviewing PRs is a time consuming task and it can be stressful for both
the reviewer and the author. Avoiding wasting time and the need of
little fixes - such as fixing grammar mistakes and typos, styling code,
or adopting conventions - is a good start for a successful (and quick)
review. Before graduating a Draft PR to a PR ready for review, please
check that:

- You did all you wanted to include in your PR. If at a later stage
  you realize something is missing and it's not a minor thing, you
  will need to open a new PR.
- If your contribution contains code or tests, you ran and passed all
  of the tests locally with [pytest](#automatic-testing).
- If you're writing documentation, you built it locally with
  sphinx and the format is what you intended.
- Your code is harmonious with the rest of the code - no repetitions
  of any sort!

Your code respects the [adopted Style](#style-guide), especially if:

- Your code is lintered adequately and respects the [PEP8](https://www.python.org/dev/peps/pep-0008/) convention.
- Your docstrings follow the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) convention.
- There are no typos or grammatical mistakes and the text is fluid.

- The code is sufficiently commented and the comments are clear.

- Your PR title is clear enough to be meaningful when appended to the version changelog.

- You have the correct labels.


### Before merging

To be merged, PRs have to:

1. Pass all the CircleCI tests, and possibly all the codecov checks.
2. Have the necessary amount of approving reviews, even if you're a
   long time contributor.

   Note : You can ask one (or more) contributor to do
   that review, if you think they align more with the content of your
   PR. You need **one** review for documentation, tests, and small
   changes, and **two** reviews for bugs, refactoring and enhancements.
3. Have at least a release-related label (or a `Skip
   release` label).
4. Have a short title that clearly explains in one sentence the aim of
   the PR.
5. Contain at least a unit test for your contribution, if the PR
   contains code (it would be better if it contains an integration or
   function test and all the breaking tests necessary). If you're not
   confident about writing tests, it is possible to refer to an issue
   that asks for the test to be written, or another (Draft) PR that
   contains the tests required.

As we're trying to maintain at least 90% code coverage, you're strongly
encouraged to write all of the tests necessary to keep coverage above
that threshold. If coverage drops too low, you might be asked to add
more tests and/or your PR might be rejected. See the [Automatic testing](#automatic-testing) section.

Don't merge your own pull request! That's a task for the main reviewer
of your PR or the project manager. Remember that the project manager
doesn't have to be a reviewer of your PR!