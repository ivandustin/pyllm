# pyllm

`pyllm` is a user-friendly library that allows you to easily work with Large Language Models (LLMs), specifically leveraging OpenAI's `gpt-3.5-turbo` model.

## Example

> **Note:** Make sure to set the `OPENAI_API_KEY` environment variable.

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
