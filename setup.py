from setuptools import setup, find_packages

setup(
    name="rhody",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "requests",
    ],
    author="Rhody Exchange Inc.",
    author_email="team@rhodyexchange.org",
    description="Rhody: A trading, AI, and backtesting Python library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rhody-Exchange/rhody",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
