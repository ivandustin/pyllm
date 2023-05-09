from functools import partial
from .completion import completion
from .chat import chat

llm = partial(chat, model="gpt-3.5-turbo", temperature=0)

__all__ = ["llm", "completion", "chat"]
