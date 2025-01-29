import itertools

# For Grouping items
def my_grouper(n,iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

# For Seprated Comma
def format_currency(amount):
            return '{: ,}'.format(amount)