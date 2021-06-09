# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup

# with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding='utf-8') as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="drf-api-history",
    version="1.0.0",
    packages=[
        "track_actions",
        "track_actions.migrations",
    ],
    description="drf api 访问历史记录 从api角度出发记录操作历史.",
    long_description='drf api 访问历史记录 从api角度出发记录操作历史 ',
    long_description_content_type='text/markdown',
    keywords="djangorestframework drf history django audit tracking",
    author="blackjack0v0",
    author_email="yihongwy1@163.com",
    install_requires=[
        'pyyaml',
    ],
    url="",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: BSD License",
    ],
)
