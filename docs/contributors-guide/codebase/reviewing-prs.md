## Reviewing PRs

Reviewing PRs is an extremely important task in collaborative
development. In fact, it is probably the task that requires the most
time in the development, and it can be stressful for both the reviewer
and the author. Remember that, as a PR Reviewer, you are guaranteeing
that the changes work and integrate well with the rest of the
repository, hence **you are responsible for the quality of the
repository and its next version release**. If they don't integrate
well, later PR reviewers might have to ask for broader changes than
expected.

There are many best practices to review code online, for
instance [this medium blog post](https://medium.com/an-idea/the-code-review-guide-9e793edcd683), but
here are some good rules of thumbs that we need to follow while
reviewing PRs:

- Be **respectful** to the PR authors and be clear in what you are
  asking/suggesting - remember that, like you, they are contributing
  their spare time and doing their best job!

- If there is a *Draft PR*, you can comment on its development in the
  message board or making "Comment" reviews. Don't ask for changes,
  and especially, **don't approve the PR**

- If the PR graduated *from Draft to full PR*, check that it follows the
  sections [Pull requests](#pull-requests) and [Style Guide](#style-guide) of these
  guidelines. If not, invite the author to do so before starting a
  review.
- **Don't limit your review to the parts that are changed**. Look at
  the entire file, see if the changes fit well in it, and see if the
  changes are properly addressed everywhere in the code - in the
  documentation, in the tests, and in other functions. Sometimes the
  differences reported don't show the full impact of the PR in the
  repository!
- If your want to make Pull Requests an educational process, invite
  the author of the PR to make changes before actually doing them
  yourself. Request changes via comments or in the message board or by
  checking out the PR locally, making changes and then submitting a PR
  to the author's branch.
- If you decide to use the suggestion tool in reviews, or to start a
  PR to the branch under review, please alert the Project Manager.
  Bots might automatically assign you contribution types that will
  have to be removed (remember, your contribution in this case is
  "Reviewer"). Instead of starting a PR to the branch under review,
  think about opening a new PR with those modifications (unless they
  are needed to pass tests), and alert the Main Reviewer. In any case
  **don't commit directly to the branch under review**!
- If you're reviewing documentation, build it locally with [`sphinx-build`](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) command.
- If you're asking for changes, **don't approve the PR**. Approve it
  only after everything was sufficiently addressed. Someone else might
  merge the PR in taking your word for granted.
- If you are the main reviewer, and the last reviewer required to
  approve the PR, merge the PR!

Before approving and/or merging PRs, be sure that:

- All the tests in CircleCI/Azure pass without errors.
- Prefereably, codecov checks pass as well. If they don't, discuss
  what to do.
- The title describes the content of the PR clearly enough to be
  meaningful on its own - remember that it will appear in the version
  changelog!
- The PR has the appropriate labels to trigger the appropriate version
  release and update the contributors table.

### Main reviewer

At `physiopy` we use the *Assignees* section of a PR to mark the
**main reviewer** for that PR. The main reviewer is the primary person
responsible **for the quality of the repository and its next version release**,
 as well as **for the behaviour of the other reviewers**.

***The main reviewer takes care of the reviewing process of the PR, in particular:***

- Invites the reviewers to finish their review in a relatively
  short time.

- Checks that all elements of this document were respected,
  especially the part about [Pull Requests](#pull-requests).

- Invites other Reviewers to respect this document, especially
  the part about [reviews](#reviewing-prs), helps them in doing
  so, and checks that they do.

- If a Reviewer keeps not respecting this document, flags them
  to the project manager.

- Decides what to do in case of a coverage decrease (in
  *codecov/patch*).

***In case of missing tests or updates to user documentation:***

- Asks for more documentation or tests before approving the
  PR, *or*

- Checks that the appropriate issues have been opened to
  address the lack of documentation or tests (1 issue per item), *or*

- Double-checks that the title is clear and the labels are correct to
  trigger an appropriate `auto` release - feel free to change them.

- Main reviewer **Is the one that is going to merge the PR.**

***After the PR has been merged and a new release has been triggered, checks that:***

- The documentation was updated correctly (if changed).
- The Pypi version of the repository coincides with the new release (if changed).
- New contributors or forms of contributions were correctly added in the README (if changed).