# Pakit Tests

[![Travis](https://travis-ci.org/pakit/pakit_tests.svg?branch=master)](https://travis-ci.org/pakit/pakit_tests)
[![Coveralls](https://coveralls.io/repos/pakit/pakit_tests/badge.svg?branch=master&service=github)](https://coveralls.io/github/pakit/pakit_tests?branch=master)
[![Stories in Ready](https://badge.waffle.io/pakit/pakit_tests.svg?label=ready&title=Ready)](http://waffle.io/pakit/pakit_tests)

## Overview

The `pakit_tests.py` script analyzes a folder with pakit recipes
and then generates a valid py.test file. For every repository available for
a recipe a test will be created. 

If a recipe depends on other recipes, those recipes will also be
built during the test. Dependencies will always build from 'stable'.

If you wish, you may take advantage of xdist to overlap the tests.
Care has been taken to ensure they execute independentantly.

IMPORTANT: Do **NOT** execute `py.test`in the root of the recipes dir.
Due to local imports in some library code, there may be import colisions.
I suggest you execute in the in the directory holding the test file.

## Example Usage

Assuming pakit recipes exist at `/tmp/recipes`.

```bash 
pakit_tests.py /tmp/recipes
cd /tmp/recipes/tests
py.test
```

If you wish to use xdist, use `py.test -n auto`.

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
