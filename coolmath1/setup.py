# Contents of coolmath/setup.py:

from setuptools import setup, find_packages

setup(
    name="coolmath1",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Asibeh Tenager",
    author_email="asibeh.tenager@gmail.com",
    description="A simple math library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/epythonlab/coolmath",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
