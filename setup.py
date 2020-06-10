from setuptools import setup
import setuptools


def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="siphotonics",
    version = '0.1.1',
    description="Silicon Photonics Development Package",
    long_description=readme(),
    entry_points = {
        'console_scripts': ['siphotonics=siphotonics.command_line:main'],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords="silicon photonics optics waveguide",
    url="https://github.com/aycandv/siphotonics",
    author="Aycan Deniz Vit",
    author_email="avit16@ku.edu.tr",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'h5py',
        'scipy',
    ],
    include_package_data=True,
    zip_safe=False)
