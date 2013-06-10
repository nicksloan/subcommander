from setuptools import setup
from happytasks import find_tasks

setup(
    name='happytasks',
    version='0.1',
    author='Nick Sloan',
    author_email='me@nicksloan.org',
    packages=['happytasks'],
    install_requires=[
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'happytasks = happytasks:main',
        ],
        'happytasks.tasks': find_tasks('happytasks.sample'),
    }
)
