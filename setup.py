#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="webway",
    version="0.1.0",
    description="Webway API backend",
    author="pranjal-upadhyaya",
    author_email="rktpranjal@gmail.com",
    packages=find_packages(),
    
    include_package_data=True,
    python_requires=">=3.12",
    install_requires=[
        "flask>=3.1.0",
        "flask-sqlalchemy>=3.1.1",
        "flask-migrate>=4.1.0",
        "python-dotenv>=1.1.0",
        "jinja2>=3.1.6",
        "alembic>=1.15.2",
        "sqlalchemy>=2.0.40",
        "fastapi>=0.115.12",
        "pydantic>=2.11.2",
        "uvicorn>=0.34.0",
        "pydantic-settings>=2.8.1",
        "requests>=2.32.3",
        "injector>=0.22.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
)
