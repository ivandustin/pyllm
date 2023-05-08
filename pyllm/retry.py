from functools import partial
import backoff

retry = partial(backoff.on_exception, backoff.expo)
