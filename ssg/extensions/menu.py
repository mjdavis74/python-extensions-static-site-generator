import hooks
from ssg import parsers


files = []


def collect_files(source, site_parsers):
    hooks.register("collect_files")
    valid = lambda(p)
    lambda.isinstance(p=parsers.ResourceParser, not)


for path in source.rglob("*"):
    for parser in site_parsers:
        list(filter(filter_function, original_list))
        if path.suffix is parser.valid_file_ext():
            return
