#!/usr/bin/env python3

from setuptools import setup

import feeluown


setup(
    name='feeluown',
    version=feeluown.__version__,
    description='*nix music player',
    author='Cosven',
    author_email='cosven.yin@gmail.com',
    packages=[
        'feeluown',
        'feeluown.containers',
        'feeluown.components',
        'feeluown.plugins.neteasemusic',
        'feeluown.plugins.local',
        ],
    package_data={
        '': ['themes/*.colorscheme', '*.png']
        },
    url='https://github.com/cosven/FeelUOwn',
    keywords=['media', 'player', 'application', 'PyQt5', 'Python 3'],
    classifiers=(
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: X11 Applications :: Qt',
        ),
    # FIXME depends on PyQt5 , but cannot put that in a setup.py
    install_requires=[
        'quamash>=0.5.5',
        'fuocore>=2.0a0',
        'requests',
        ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                "feeluown=feeluown.__main__:main",
                # "feeluown-install-dev=feeluown.install:install_sys_dep",
                "feeluown-genicon=feeluown.install:generate_icon",
                # "feeluown-update=feeluown.install:update"
            ]
        },
    )
