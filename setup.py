from setuptools import find_packages, setup

setup(
    name="repka",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.10.0",
        "requests==2.27.1",
        "termcolor==1.1.0",
    ],
    python_requires='>=3.9'
)
