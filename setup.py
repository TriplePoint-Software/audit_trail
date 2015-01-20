from setuptools import setup

__version__ = "0.0.13"

setup(
    name='audit_trail',
    version=__version__,
    packages=['audit_trail', 'audit_trail.migrations', 'audit_trail.south_migrations'],
    url='https://github.com/TriplePoint-Software/audit_trail',
    license='Apache License, Version 2.0',
    author_email='',
    description='App for tracking django model changes',
    install_requires=["django>=1.7", "jsonfield==1.0.0"],
    tests_require=["django>=1.7", "jsonfield==1.0.0"],
    test_suite='runtests.runtests'
)