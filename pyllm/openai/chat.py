from random import choice
import logging
import openai

logger = logging.getLogger(__name__)


def chat(prompt, **kwargs):
    response = openai.ChatCompletion.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        **kwargs,
    )
    logger.info(f"Parameters\n{kwargs}")
    logger.info(f"Response\n{response}")
    return choice(response["choices"])["message"]["content"]
