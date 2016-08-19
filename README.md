# Django Katas

This repository contains some exercises ([katas](https://en.wikipedia.org/wiki/Kata)) to help you understand some features of Django's ORM.

There are three important files:

 * `django_katas/models.py`
   * This file defines three related models: `Artist`, `Album`, and `Track`.
 * `django_katas/managers.py`
   * This file defines managers for each of the three models.
   * Each manager defines a number of methods that can be used to retrieve models from the database.
   * Each method has an explanatory docstring, and a link to some relevant documentation.
 * `django_katas/tests.py`
   * There is a test for each manager method, which tests that the manager method returns correct results.

To run the tests, run:

    ./manage.py test --failfast

This will run the tests in tests.py, halting as soon as the first test fails.
