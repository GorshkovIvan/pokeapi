from setuptools import setup, find_packages

setup(
    name="pokeapi-sdk",
    version="0.1.0",
    description="A Python SDK for the PokeAPI",
    author="Ivan Gorshkov",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["py.typed", "__init__.py"]},
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=2.0.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 