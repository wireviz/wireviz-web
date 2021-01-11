import logging
import sys


def setup_logging(level=logging.INFO):
    log_format = "%(asctime)-15s [%(name)-15s] %(levelname)-7s: %(message)s"
    logging.basicConfig(format=log_format, stream=sys.stderr, level=level)


class ReversibleDict(dict):
    """
    Reverse dictionary lookup.

    http://stupidpythonideas.blogspot.com/2014/07/reverse-dictionary-lookup-and-more-on.html
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rev = {v: k for k, v in self.items()}

    def __delitem__(self, k):
        del self.rev[self[k]]
        super(ReversibleDict, self).__delitem__(k)

    def __setitem__(self, k, v):
        try:
            del self.rev[self[k]]
        except KeyError:
            pass
        super(ReversibleDict, self).__setitem__(k, v)
        self.rev[v] = k

    def lookup(self, v):
        return self.rev[v]
