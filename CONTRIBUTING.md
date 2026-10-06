# Contributing to ContribRadar

Thank you for contributing to ContribRadar!

## Before contributing

- Read the README.
- Search existing issues before opening a new one.
- Keep pull requests focused.
- Add or update tests when changing behavior.
- Update documentation when necessary.

## Development setup

Install the project:

```bash
python -m pip install -e .

## Install pytest:

bash
python -m pip install pytest

run test
pytest -q

contribradar scan . --json


You don't paste the Bash commands into GitHub files. The bash label I showed was only indicating that those lines are meant to be run in a terminal.

Since you're building this on your Android phone, you can skip them for now.

If you want to run them later
You need a terminal on a computer/phone where Python is installed. For example:

python -m pip install pytest
then:

pytest -q
But do not paste these into CONTRIBUTING.md as commands to execute now—they are already correctly written there as instructions for contributors.

For you right now
Continue with:

GitHub → Add file → Create new file → CONTRIBUTING.md

Paste the CONTRIBUTING.md content I gave you, then Commit changes.

You don't need to install Python or pytest yet.


Check

I checked it. ⚠️ The CONTRIBUTING.md file is incomplete.

It currently ends here:

Clone the repository and install it locally:

python -m pip install -e .
So the rest of the content wasn't saved.

Fix it
Open CONTRIBUTING.md on GitHub → Edit ✏️ → replace the entire file with this complete version:

# Contributing to ContribRadar

Thank you for your interest in contributing to ContribRadar!

ContribRadar is an open-source project focused on helping developers discover meaningful opportunities to improve software projects.

## Before contributing

Please:

1. Read the README.
2. Search existing issues before opening a new one.
3. For larger changes, open an issue first to discuss the idea.
4. Keep pull requests focused on one clear improvement.
5. Add or update tests when changing behavior.
6. Update documentation when necessary.

## Development setup

Clone the repository and install it locally:

```bash
python -m pip install -e .
Install the test dependency:

python -m pip install pytest
Run the test suite:

pytest -q
Run ContribRadar:

contribradar scan .
For machine-readable output:

contribradar scan . --json
Good first contributions
Some useful areas include:

improving documentation

adding tests

improving repository analyzers

supporting additional programming languages

improving report formats

fixing bugs

improving error handling

improving the command-line interface

Pull requests
Please explain:

what you changed

why the change is useful

how you tested it

Keep pull requests focused and avoid unrelated changes.

AI-assisted contributions
AI-assisted development is welcome.

However, contributors are responsible for understanding, reviewing, testing, and maintaining the code they submit.

Code of conduct
Please treat other contributors respectfully and follow the project's Code of Conduct.

Thank you for helping make ContribRadar better.


Then **Commit changes**.

After that, tell me **“Check”** again. I'll verify the whole file before we continue.

Check now 

I checked again. ⚠️ It is still incomplete.

It currently ends after:

contribradar scan . --json
The remaining sections (Good first contributions, Pull requests, AI-assisted contributions, and Code of conduct) were not saved.

Easiest fix
Since the important setup commands are already there, let's keep the file simple rather than fighting the mobile editor.

Open CONTRIBUTING.md → Edit → replace everything with this shorter complete version:

# Contributing to ContribRadar

Thank you for contributing to ContribRadar!

## Before contributing

- Read the README.
- Search existing issues before opening a new one.
- Keep pull requests focused.
- Add or update tests when changing behavior.
- Update documentation when necessary.

## Development setup

Install the project:

```bash
python -m pip install -e .
Install pytest:

python -m pip install pytest
Run tests:

pytest -q
Run ContribRadar:

contribradar scan .
JSON output:

contribradar scan . --json

Good first contributions
Documentation improvements

Tests

Bug fixes

New repository analyzers

Additional programming-language support

CLI improvements

Better report formats

Pull requests
Please explain:

What changed

Why it is useful

How you tested it

Keep pull requests focused and avoid unrelated changes.

AI-assisted contributions
AI-assisted contributions are welcome.

Contributors are responsible for reviewing, understanding, and testing the code they submit.

Thank you for helping improve ContribRadar!


**Important:** Make sure you paste all the way to the final line `Thank you for helping improve ContribRadar!` before committing.

Then say **Check** again.
