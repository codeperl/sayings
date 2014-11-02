# def enum(*sequential, **named):
#     enums = dict(zip(sequential, range(len(sequential))), **named)
#     return type('Enum', (), enums)

def enum(**enums):
    """Create enum like behaviour with this class
    """
    return type('Enum', (), enums)