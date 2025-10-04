# setup.py

from setuptools import setup, find_packages

setup(
    name="eliza",
    version="1.0.0",
    author="Giuseppe Compagnone",
    author_email="compagnonegiuseppe04@gmail.com",
    description="A Python implementation of the original ELIZA chatbot",
    packages=find_packages(where="src"),  
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "eliza=cli.terminal:main",  
        ]
    },
)
