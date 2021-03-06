#!/usr/bin/env python
import os
import sys

import django


def runtests(*test_args):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pinax.{{ app_name }}.tests.settings")
    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    from django.core import checks

    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        if not test_args:
            test_args = ["pinax.{{ app_name }}.tests"]
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        test_args = ["tests"]

    checks = checks.run_checks()
    if checks:
        sys.exit(checks)
    failures = runner_class(verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == "__main__":
    runtests(*sys.argv[1:])
