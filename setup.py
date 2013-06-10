from setuptools import setup
from subcommander import find_tasks

setup(
    name='subcommander',
    version='0.1',
    author='Nick Sloan',
    author_email='me@nicksloan.org',
    packages=['subcommander'],
    install_requires=[
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'subcommander = subcommander:main',
        ],
        'subcommander.tasks': find_tasks('subcommander.sample'),
    }
)
