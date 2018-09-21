'''Python TDD Playground'''
import os
import subprocess

from setuptools import find_packages, setup

with open('README.rst') as f:
    README = f.read()

META = {}
with open(os.path.join('otajisan', 'samples', 'tdd', 'version.py')) as f:
    exec(f.read(), META)  # pylint: disable=exec-used

with open(os.path.join('requirements.txt')) as f:
    REQUIRED = [l for l in f.read().splitlines() if not l.startswith('#')]

try:
    REV = len(subprocess.check_output('git rev-list HEAD',
                                      shell=True).splitlines())
except subprocess.CalledProcessError:
    REV = 0

VERSION = '%s.%d' % (META['__version__'], REV)

setup(
    name='otajisan.samples.tdd',
    version=VERSION,
    author='otajisan',
    author_email='foo@com',
    maintainer='otajisan',
    maintainer_email='foo@com',
    url='https://github.com/otajisan/tdd-with-python',
    description=__doc__.splitlines()[0],
    long_description=README,
    packages=find_packages(),
    namespace_packages=['otajisan'],
    install_requires=REQUIRED,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
