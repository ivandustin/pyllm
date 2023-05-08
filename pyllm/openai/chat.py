from random import choice
import logging
import openai
from .retry import retry

logger = logging.getLogger(__name__)


def chat(model):
    def function(prompt):
        logger.info(f"Model {model}")
        logger.info(f"Input\n{prompt}")
        response = request(model, prompt)
        logger.info(f"Response\n{response}")
        output = choice(response["choices"])["message"]["content"]
        logger.info(f"Output\n{output}")
        return output

    return function


@retry
def request(model, prompt):
    return openai.ChatCompletion.create(
        model=model,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
