Not sure what you'd like to contribute? You could consider...

### Contributing with small documentation changes

If you are new to GitHub and just have a small documentation change
recommendation (such as: typos detection, small improvements in the
content, ...), please open an issue in the relative project, and label
it with the "Documentation" label. Chances are those types of changes
are easily doable with GitHub's online editor, which means you can do
them, or ask for help from the developers!

### Contributing with user testing

Another, non-coding friendly way to contribute to `physiopy` is by
testing the packages. There are different kinds of tests, but to
simplify things you can think mainly about automatic tests and user
tests. To know more about **Automatic tests**, you can read the [testing
section](#automatic-testing). **User testing** are warm, human, emotional and
opinionated tests that not only check that the code is doing what it
needs to do, but also whether there's a better way to do it - namely
better reports, clearer screen outputs, warnings and exceptions,
unexpected bugs that have to be corrected. If you want to perform one,
open an issue on GitHub or drop a comment in Gitter, refer to this
[blueprint](https://docs.google.com/document/d/1b6wc7JVDs3vi-2IqGg_Ed_oWKbZ6siboAJHf55nodKo/edit?usp=sharing)
and don't be afraid to ask questions!

### Contributing with test files

At `physiopy` we always try to imagine and support every possible
setting out there. However, our imagination has a limit - but if you
think our packages should process a specific format/setting that you
have, we're more than glad to do so! To make it happen, we need an
example of the file we want to process, so you will have to share it
with us (and the rest of the world)! The contribution can be a full file
of data that you already acquired, a part of that file (pay attention to
what is the minimum you need to share!), or mock data. The file
contribution should come with a json file of the same name that contains
the necessary information to run `phys2bids` on that file contribution.
There is a [json blueprint in
OSF](https://mfr.de-1.osf.io/render?url=https://osf.io/jrnxv/?direct%26mode=render%26action=download%26mode=render),
you can download it and adapt it. Note that the frequency list **has to
be expressed in Hz** as an integer or float. To contribute with a test
file, open an Issue in GitHub and label it with *Test*. We'll help you
add the file in our [OSF](https://osf.io/3txqr/) space. We're extremely
grateful for this type of contribution - so grateful that we asked
allcontributors to add a dedicated category!

### Contributing documentation through GitHub

We use [readthedocs](https://readthedocs.org/) to create our
documentation. Every contribution is welcome and it follows the same
steps as a code contribution, explained below.

### Contributing code through GitHub

This section covers 90% of the contributions a project like `physiopy`
receives - code, documentation and tests. The best way to make this kind
of contribution, in a nutshell, is to: 1. Open an issue with the
intended modifications. 2. Label it, discuss it, (self-)assign it. 3.
Open a Pull Request (PR) to resolve the issue and label it. 4. Wait for
a review, discuss it or comply, repeat until ready. Issues and PR chats
are great to maintain track of the conversation on the contribution.
They are based upon GitHub-flavoured
[Markdown](https://daringfireball.net/projects/markdown). GitHub has a
helpful page on [getting started with writing and formatting Markdown on
GitHub](https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github).

### Contributing with Pull Requests Reviews

A big challenge of software development is merging code accurately
without having to wait too much time. For this reason, Reviewers for PRs
are more than welcome! It is a task that requires some experience, but
it's very necessary! Read the [related section below](#reviewing-prs) to
start!