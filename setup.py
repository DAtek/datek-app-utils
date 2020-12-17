from pathlib import Path

from setuptools import setup

version_file = Path(__file__).resolve().parent / ".version"

NAME = "app_utils"


setup(
    name=NAME,
    author="Attila Dudas",
    author_email="dudasa7@gmail.com",
    version=version_file.read_text(),
    description="Utilities for building applications",
    url="https://gitlab.com/DAtek/app-utils",
    packages=[
        NAME
    ],
    python_requires='>=3.8',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
