# Pakit Tests

[![Travis](https://travis-ci.org/pakit/pakit_tests.svg?branch=master)](https://travis-ci.org/pakit/pakit_tests)
[![Coveralls](https://coveralls.io/repos/pakit/pakit_tests/badge.svg?branch=master&service=github)](https://coveralls.io/github/pakit/pakit_tests?branch=master)
[![Stories in Ready](https://badge.waffle.io/pakit/pakit_tests.svg?label=ready&title=Ready)](http://waffle.io/pakit/pakit_tests)

## Features Needed

I believe for now I'll make a simple recipe test automation system.

This script will generate one large test file.
Recipes can then download it, generate tests and then run them.

Features Needed:

- [ ] Inspect recipes and generate test code containing pytests installing/verifying recipes.
  - [x] Test every recipe and every possible configurable repo.
  - [ ] Make allowance for "unstable" repos to fail, optional?
- [x] Test the generation **itself** using pytest.
- [ ] Create standard method for easy integration into recipe repos.
- [ ] Update recipe repositories will execute tests with pytest.
