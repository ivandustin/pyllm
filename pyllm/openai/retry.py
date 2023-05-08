from pyllm.retry import retry as function
import openai

retry = function(openai.error.RateLimitError)
