from functools import partial
from .chat import chat

llm = partial(chat, model="gpt-3.5-turbo", temperature=0)
