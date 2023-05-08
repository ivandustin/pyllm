# pyllm

## Examples

> **Note:** Set `OPENAI_API_KEY` environment variable.

```python
from pyllm import llm

llm("Hello, world!")
```

```
Hello there! How can I assist you today?
```

```python
from pyllm import llm

prompt = """task: code
language: python
problem: add two numbers from stdin
result:
"""
llm(prompt)
```

```
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
```
