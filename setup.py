from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="enhanced-proxy",
    version="1.0.0",
    author="Tsutomu",
    author_email="your.email@example.com",
    description="A powerful and flexible proxy management library for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsutomu-n/enhanced_proxy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=1.10.7",
        "aiohttp>=3.8.4",
        "aiohttp-socks>=0.7.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.1",
            "pytest-asyncio>=0.21.0",
            "black>=23.3.0",
            "mypy>=1.2.0",
        ],
    },
)