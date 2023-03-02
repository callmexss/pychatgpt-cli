from setuptools import setup, find_packages


setup(
    name="pychatgpt-cli",
    version="0.0.3",
    author="callmexss",
    author_email="callmexss@126.com",
    description="A command-line ChatGPT tool using official OpenAI API.",
    long_description_content_type='text/markdown',
    long_description=open("README.md").read(),
    url="https://github.com/callmexss/pychatgpt-cli",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "openai>=0.27.0",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "gcli = cli:main",
        ],
    },
)
