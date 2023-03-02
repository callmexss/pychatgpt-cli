#!/usr/bin/env python
import json
from pathlib import Path

import click
import openai
from rich import print


CUR = Path(__file__).parent
USER_HOME = Path('~').expanduser()


@click.command()
@click.argument("prompt")
def main(prompt):
    try:
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        print(completion.choices[0].message.content)
        with open(CUR / "gptlog.txt", 'a') as f:
            f.write(json.dumps(completion))
    except openai.error.AuthenticationError as err:
        print(err)


if __name__ == '__main__':
    main()