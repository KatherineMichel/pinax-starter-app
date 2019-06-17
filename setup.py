from setuptools import find_packages, setup

VERSION = "0.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-{{ app_name }}.svg
    :target: https://pypi.python.org/pypi/pinax-{{ app_name }}/

=========
Pinax App
=========

.. image:: https://img.shields.io/pypi/v/pinax-{{ app_name }}.svg
    :target: https://pypi.python.org/pypi/pinax-{{ app_name }}/

\ 

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-{{ app_name }}.svg
    :target: https://circleci.com/gh/pinax/pinax-{{ app_name }}
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-{{ app_name }}.svg
    :target: https://codecov.io/gh/pinax/pinax-{{ app_name }}
.. image:: https://img.shields.io/github/contributors/pinax/pinax-{{ app_name }}.svg
    :target: https://github.com/pinax/pinax-{{ app_name }}/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-{{ app_name }}.svg
    :target: https://github.com/pinax/pinax-{{ app_name }}/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-{{ app_name }}.svg
    :target: https://github.com/pinax/pinax-{{ app_name }}/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\ 

``pinax-{{ app_name }}`` is a useful app for the Django web framework.
 
``pinax-{{ app_name }}`` does this and that.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+
| Django / Python | 3.5 | 3.6 | 3.7 |
+=================+=====+=====+=====+
|  2.1            |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
|  2.2            |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="<project description> for the Django web framework",
    name="pinax-{{ app_name }}",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-{{ app_name }}/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "{{ app_name }}": []
    },
    install_requires=[
        "Django>=2.0"
    ],
    tests_require=[
    ],
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
