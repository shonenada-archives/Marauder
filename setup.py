import os
from setuptools import setup, find_packages

CURRENT_DIR = dirname(realpath(__file__))


with open(join(CURRENT_DIR, 'README.rst')) as readme:
    long_description = readme.read()


setup(
    name='Marauder',
    version='0.1.0',
    url='https://github.com/shonenada/Marauder',
    author='shonenada',
    author_email='shonenada@gmail.com',
    description='BearyChat in console',
    long_description=long_description,
    zip_safe=True,
    packages=find_packages(),
    playforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Development Status :: 3 - Alpha',
    ]
)
