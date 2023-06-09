# pyllm

A very simple Large Language Model (LLM) API. It uses the OpenAI `gpt-3.5-turbo` model.

## Install

```
pip install git+https://github.com/ivandustin/pyllm.git
```

### Poetry

```
poetry add git+https://github.com/ivandustin/pyllm.git
```

## Examples

> **Note:** Make sure to set the `OPENAI_API_KEY` environment variable. You can get it [here](https://platform.openai.com/account/api-keys).

### Basic Usage

```python
from pyllm import llm

response = llm("Hello, world!")
print(response)
```

Output

```
Hello there! How can I assist you today?
```

### Coding

```python
from pyllm import llm

prompt = """task: code
language: python
problem: add two numbers from stdin
result:
"""

response = llm(prompt)
print(response)
```

Output

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
```

### Word Definition

```python
from pyllm import llm

prompt = """task: define succinctly
features: etymology, grammar, description
word: απεχουσι
"""

response = llm(prompt)
print(response)
```

Output

```
απεχουσι is a Greek verb in the present tense, third person plural form. Its etymology comes from 
the prefix απο- meaning "away from" and the verb εχω meaning "to have". Together, απεχουσι means 
"they are away from" or "they have abstained from".
```

## Stringified Dictionary

Surprisingly, the LLM can also understand a stringified dictionary.

### Coding

```python
from pyllm import llm

prompt = {
    "task": "code",
    "language": "python",
    "problem": "add two numbers from stdin",
    "code": ""
}

response = llm(str(prompt))
print(response)
```

> **Note:** The empty `code` entry is needed so that the model will produce a pure source code.

Output

```python
a = int(input())
b = int(input())
print(a + b)
```

### Word Definition

```python
from pyllm import llm

prompt = {
    "task": ["define succinctly"],
    "features": ["etymology", "grammar", "description"],
    "word": "απεχουσι"
}

response = llm(str(prompt))
print(response)
```

Output

```
The word "απεχουσι" is a Greek verb that means "they are far away" or "they keep away". Its 
etymology comes from the prefix "απο-" meaning "away from" and the verb "εχω" meaning "to have". 
In terms of grammar, it is a present tense verb in the third person plural.
```

## Additional Parameters

You can pass [additional parameters](https://platform.openai.com/docs/api-reference/chat) in the `kwargs` of the `llm(prompt, **kwargs)` function.
