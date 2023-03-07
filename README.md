# PyChatGPT-CLI

A command-line ChatGPT tool using official OpenAI API.

## Installing

Install and update using `pip`:

```sh
pip install -U pychatgpt-cli
```

## Usage

```sh
# set environment
# for windows
> set OPENAI_API_KEY=your_api_key
# for linux
> export OPENAI_API_KEY="your api key"

> gcli --help
Usage: gcli [OPTIONS] PROMPT

Options:
  --help  Show this message and exit.
```

## Examples

```sh
> gcli "hello world"
Hello! How can I assist you today?

> gcli "write hello world use python" 
print("Hello, World!")

> gcli "how to install pandas?"

As an AI Language model, I do not have the access to your computer to install pandas. However, I can suggest the general steps to install pandas, assuming you use Python:

1. Open the terminal (for macOS/Linux) or Command Prompt/PowerShell (for Windows)
2. Type `pip install pandas` and press Enter
3. Wait for the installation process to complete
4. Verify the installation by importing pandas in Python and checking the version number. Type `python` in the terminal, then `import pandas as pd` and `pd.__version__`.

Note: If you encounter any errors or have issues with the installation, you can refer to the pandas documentation or reach out to the pandas community for support.
```
