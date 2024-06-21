## Labels

The current list of labels are
[here](https://github.com/physiopy/phys2bids/labels). They can be used
for **Issues**, **PRs**, or both. We use
[auto](https://github.com/intuit/auto) to automate our semantic
versioning and Pypi upload, so **it's extremely important to use the
right PR labels**!

### Issue & PR labels

- ![Documentation](https://img.shields.io/badge/-Documentation-1D70CF?style=flat-square) Improvements or additions to documentation. This
  category includes (but is not limited to) docs pages, docstrings,
  and code comments. 

- ![Duplicate](https://img.shields.io/badge/-Duplicate-CFD3D7?style=flat-square) Whatever this is, it exists already! Maybe it's a closed
  Issue/PR, that should be reopened. 

- ![Enhancement](https://img.shields.io/badge/-Enhancement-A2EEEF?style=flat-square) New features added or requested. This normally goes with a `minormod` label for PRs.

- ![Outreach](https://img.shields.io/badge/-Outreach-0E8A16?style=flat-square) As part of the scientific community, we care about outreach. Check the relevant section about it, but know that this
  Issue/PR contains information or tasks about abstracts, talks,
  demonstrations, papers. 

- ![Paused](https://img.shields.io/badge/-Paused-F7C38C?style=flat-square) Issue or PR should not be worked on until the resolution of other issues or PRs.

- ![released](https://img.shields.io/badge/-released-ffffff?style=flat-square) This Issue or PR has been released. 

- ![Testing](https://img.shields.io/badge/-Testing-FFB5B4?style=flat-square) This is for testing features, writing tests or producing testing code. Both user testing and CI testing!

- ![Urgent](https://img.shields.io/badge/-Urgent-FFF200?style=flat-square) If you don't know where to start, start here! This is probably related to a milestone due soon!

### Issue-only labels

- ![BrainHack](https://img.shields.io/badge/-BrainHack-000000?style=flat-square) This issue is suggested for BrainHack participants!

- ![Bug](https://img.shields.io/badge/-Bug-D73A4A?style=flat-square) Something isn't working. It either breaks the code or has an
  unexpected outcome.

- ![Community](https://img.shields.io/badge/-Community-E2C7FC?style=flat-square) This issue contains information about the `physiopy`
  community (e.g. the next developer call)
 
- ![Discussion](https://img.shields.io/badge/-Discussion-1C778C?style=flat-square) Discussion of a concept or implementation. These Issues
  are prone to be open ad infinitum. Jump in the conversation if you
  want!

- ![Good first issue](https://img.shields.io/badge/-Good%20first%20issue-4E2A84?style=flat-square) Good for newcomers. These issues calls for a
  **fairly** easy enhancement, or for a change that helps/requires
  getting to know the code better. They have educational value, and
  for this reason, unless urgent, experts in the topic should refrain
  from closing them - but help newcomers closing them.

- ![Hacktoberfest](https://img.shields.io/badge/-Hacktoberfest-FF7518?style=flat-square) Dedicated to the hacktoberfest event, so that people
  can help and feel good about it (and show it with a T-shirt!).
  **Such commits will not be recognised in the all-contributor table,
  unless otherwise specified**.

- ![Help wanted](https://img.shields.io/badge/-Help%20wanted-57DB1A?style=flat-square) Extra attention is needed here! It's a good place to have a look!

- ![Refactoring](https://img.shields.io/badge/-Refactoring-9494FF?style=flat-square) Improve nonfunctional attributes. Which means rewriting
  the code or the documentation to improve performance or just because
  there's a better way to express those lines. It might create a
  `majormod` PR.

- ![Question](https://img.shields.io/badge/-Question-D876E3?style=flat-square) Further information is requested, from users to
  developers. Try to respond to this!
  
- ![Wontfix](https://img.shields.io/badge/-Wontfix-ffffff?style=flat-square) This will not be worked on, until further notice.

### PR-only labels

#### Labels for semantic release and changelogs

- ![BugFIX](https://img.shields.io/badge/-BugFIX-D73A4A?style=flat-square) These PRs close an issue labelled `Bug`. They also increase
  the semantic versioning for fixes (+0.0.1).

 - ![dependencies](https://img.shields.io/badge/-dependencies-0366D6?style=flat-square) Pull requests that update a dependency file

- ![Documentation](https://img.shields.io/badge/-Documentation-1D70CF?style=flat-square) See above. This PR won't trigger a release, but it will be reported in the changelog.

- ![Majormod](https://img.shields.io/badge/-Majormod-05246D?style=flat-square) These PRs call for a new major release (+1.0.0). This
  means that the PR is breaking backward compatibility.

- ![Minormod](https://img.shields.io/badge/-Minormod-05246D?style=flat-square) This PR generally closes an `Enhancement` issue. It increments the minor version (0.+1.0)

- ![Minormod-breaking](https://img.shields.io/badge/-Minormod&ndash;breaking-05246D?style=flat-square) This label should be used during development stages (<1.0.0) only. These PRs call for a new minor release during development (0.+1.0) that **will** break backward compatibility. 

- ![Internal](https://img.shields.io/badge/-Internal-ffffff?style=flat-square) This PR contains changes to the internal API. It won't
  trigger a release, but it will be reported in the changelog.

- ![Testing](https://img.shields.io/badge/-Testing-FFB5B4?style=flat-square) See above. This PR won't trigger a release, but it will be
  reported in the changelog.

- ![Skip release](https://img.shields.io/badge/-Skip%20release-ffffff?style=flat-square) This PR will **not** trigger a release.

- ![Release](https://img.shields.io/badge/-Release-ffffff?style=flat-square) This PR will force the trigger of a release.

#### Other labels

- ![Invalid](https://img.shields.io/badge/-Invalid-960018?style=flat-square): These PRs don't seem right. They actually seem so not
  right that they won't be further processed. This label invalidates a
  Hacktoberfest contribution. If you think this is wrong, start a
  discussion in the relevant issue (or open one if missing). Reviewers
  are asked to give an explanation for the use of this label.

### Good First Issues

Good First Issues are issues that are either very simple, or that help
the contributor get to know the programs or the languages better. We use
it to help contributors with less experience to learn and familiarise
with Git, GitHub, Python3, and physiology. We invite more expert
contributors to avoid those issues, leave them to beginners and possibly
help them out in the resolution of the issue. However, if the issue is
left unassigned or unattended for long, and it's considered important or
urgent, anyone can tackle it.