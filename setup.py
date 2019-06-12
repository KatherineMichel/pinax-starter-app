from setuptools import find_packages, setup


setup(
    author="",
    author_email="",
    description="",
    name="pinax-{{ app_name }}",
    version="0.1",
    url="http://github.com/pinax/pinax-{{ app_name }}/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "{{ app_name }}": []
    },
    test_suite="runtests.runtests",
    install_requires=[
        "Django>=1.8"
    ],
    tests_require=[
    ],
    extras_require={
        "pytest": ["pytest", "pytest-django"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
