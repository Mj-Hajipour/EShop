import itertools
import os


# For Grouping items
def my_grouper(n,iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

# For Seprated Comma
def format_currency(amount):
            return '{: ,}'.format(amount)

#For Upload Image
def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext




