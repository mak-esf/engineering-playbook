import re

def replace_extension(filename):
    return re.sub(r'\.html$', '.aspx', filename)

def on_files(files, **kwargs):
    for f in files:
        if f.is_documentation_page():
            f.dest_path = replace_extension(f.dest_path)
            f.abs_dest_path = replace_extension(f.abs_dest_path)
            f.url = replace_extension(f.url)