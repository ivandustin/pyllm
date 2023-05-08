from random import choice
import logging
import openai
from .retry import retry

logger = logging.getLogger(__name__)


def chat(prompt, **kwargs):
    default = dict(model="gpt-3.5-turbo", temperature=0)
    parameters = {**default, **kwargs}
    logger.info(f"Input\n{prompt}")
    logger.info(f"Parameters\n{parameters}")
    response = request(prompt, parameters)
    logger.info(f"Response\n{response}")
    output = choice(response["choices"])["message"]["content"]
    logger.info(f"Output\n{output}")
    return output


@retry
def request(prompt, parameters):
    return openai.ChatCompletion.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        **parameters,
    )
