class PoolEmptyError(object):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯萎')