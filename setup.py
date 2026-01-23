#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="odianumerals",
    version="1.0.4",
    author="Srinibash Samal",
    author_email="hola2srini@gmail.com",
    description="A comprehensive library for Odia numeral processing and linguistic conversion.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/srinibashsamal/odianumerals",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    keywords="odia, odianumber, numerals, odia-math, barnabodha, indian-numbering-system",
    license="MIT License",
    project_urls={
        "Bug Tracker": "https://github.com/srinibashsamal/odianumerals/issues",
        "Source Code": "https://github.com/srinibashsamal/odianumerals",
    },
)
