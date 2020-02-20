#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="json_to_object",
    version="0.0.0",
    license="MIT",
    description="Skeleton for Python projects.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author="Peilonrayz",
    author_email="peilonrayz@gmail.com",
    url="https://peilonrayz.github.io/json_to_object",
    project_urls={
        "Bug Tracker": "https://github.com/Peilonrayz/json_to_object/issues",
        "Documentation": "https://peilonrayz.github.io/json_to_object",
        "Source Code": "https://github.com/Peilonrayz/json_to_object",
    },
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="",
    # entry_points={"console_scripts": ["json_to_object=json_to_object.__main__:main"]},
)
