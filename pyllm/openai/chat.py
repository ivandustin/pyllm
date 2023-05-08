from random import choice
import logging
import openai

logger = logging.getLogger(__name__)


def chat(prompt, **kwargs):
    logger.info(f"Input\n{prompt}")
    logger.info(f"Parameters\n{kwargs}")
    response = openai.ChatCompletion.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        **kwargs,
    )
    logger.info(f"Response\n{response}")
    output = choice(response["choices"])["message"]["content"]
    logger.info(f"Output\n{output}")
    return output
