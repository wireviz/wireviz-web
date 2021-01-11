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
        del super()[k]

    def __setitem__(self, k, v):
        try:
            del self.rev[self[k]]
        except KeyError:
            pass
        super()[k] = v
        self.rev[v] = k

    def lookup(self, v):
        return self.rev[v]
