# Pak Bot

[![Travis](https://travis-ci.org/pakit/pak_bot.svg?branch=master)](https://travis-ci.org/pakit/pak_bot)
[![Coveralls](https://coveralls.io/repos/pakit/pak_bot/badge.svg?branch=master&service=github)](https://coveralls.io/github/pakit/pak_bot?branch=master)
[![Stories in Ready](https://badge.waffle.io/pakit/pak_bot.svg?label=ready&title=Ready)](http://waffle.io/pakit/pak_bot)

## Features Needed

I believe for now I'll make a simple recipe automation system.

Features Needed:

- [ ] Inspect recipes and generate test code containing pytests installing/verifying recipes.
  - [ ] Test every recipe and every possible configurable repo.
  - [ ] Make allowance for "unstable" repos to fail, optional?
- [ ] Test the generation **itself** using pytest.
- [ ] Create standard method for easy integration into recipe repos.
- [ ] Update recipe repositories will execute tests with pytest.
