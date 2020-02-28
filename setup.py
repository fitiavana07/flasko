# -*- coding: utf-8 -*-
import re

from setuptools import find_packages, setup

with open("README.rst", encoding="utf-8") as f:
    _readme = f.read()

with open("src/flasko/__init__.py", encoding="utf-8") as f:
    _version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="Flasko",
    version=_version,
    url="https://github.com/fitiavana07/flasko",
    project_urls={
        "Documentation": "https://github.com/fitiavana07/flasko",
        "Code": "https://github.com/fitiavana07/flasko",
        "Issue tracker": "https://github.com/fitiavana07/flasko/issues",
    },
    license="MIT",
    author="Fitiavana Ramanandafy",
    author_email="fitiavana.ramanandafy@gmail.com",
    description="A Flask Boilerplate",
    long_description=_readme,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        "Flask>=1.1.1",
        "Flask-JSON>=0.3.4",
        "Flask-Login>=0.5.0",
        "flask-mongoengine>=0.9.5",
        "mongoengine>=0.19.1",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-sugar",
            "mongomock",
            "coverage",
            "pre-commit",
        ]
    },
)
