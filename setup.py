from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='wikiparser',
    version='0.1.0',
    description='German Wiktionary Parser',
    long_description=long_description,
    url='https://github.com/nmarincic/wordProject',
    author='Nikola Marincic',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='wiktionary parser',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'wikiparser=wikiparser.__main__:main',
        ],
    },
)