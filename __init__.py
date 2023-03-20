import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KairoGraph",
    version="1.0",
    author="Nathan Vilane",
    author_email="learnfastwithnathan@gmail.com",
    description="Python package for creating and analyzing plot graphs and tables, as well as generating grids and shapes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/<Afrinteli>/<repository>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
