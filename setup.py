# setup.py
# This file contains the configuration for packaging the trading_simulation project

from setuptools import setup, find_packages

setup(
    name='trading_simulation',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'run-simulation=scripts.run_simulation:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Monte Carlo simulation for analyzing the probability of passing a prop firm trading test with trailing stops and profit targets.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/trading_simulation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
