import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='surgeon',
    version='0.0.1',
    author='Isaac Pérez',
    description='A tool for analysing neural networks',
    url='https://github.com/isaacperez/surgeon',
    keywords='neural networks, convolutional neural networks, deep learning',
    long_description=read('README.md'),
    python_requires='>=3.7, <4',
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    test_suite="tests",
    extras_require={
        'test': ['pytest', 'coverage'],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
)