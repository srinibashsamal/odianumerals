from setuptools import find_packages, setup

setup(
    name="odianumerals",
    version="1.0.3",
    author="Srinibash Samal",
    author_email="hola2srini@gmail.com",
    description="A comprehensive library for Odia numeral processing and linguistic conversion.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/srinibashsamal/odianumerals",  # Update this after uploading to GitHub
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    keywords="odia, odianumber, numerals, odia-math, barnabodha, indian-numbering-system",
)
