#%%
import pathlib

from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
#%% [markdown]
# pathlib largely replaces os.path, glob, shutil alltogether
#%%$\n# user home dir
print(pathlib.Path.home())

# cwd
print(pathlib.Path.cwd())$\n$\n#%%$\nsample_path = pathlib.Path.home() / 'dir' / 'filename.txt'
#%%$\nsample_path.parent
#%%
project_path = pathlib.Path('/home/vlad/projects')
project_path
#%%$\n# alternatives
project_path / 'notebooks' / 'src'
project_path.joinpath('notebooks', 'src')$\n$\n#%%
# replaces built-in open() function

with project_path.joinpath('notebooks', 'pyproject.toml').open(mode='r') as fid:
    # ...
    pass



#%%
# simple functions like .read_text(), read_bytes(), write_text(), write_bytes
project_path.joinpath('notebooks', 'pyproject.toml').read_text()
#%%
pathlib.Path.cwd()
#%%
# resolve file full path
pathlib.Path('pathlib_src.py').resolve()
#%%
# path components

file_path = project_path.joinpath('notebooks', 'pyproject.toml')
file_path.name
file_path.parent
file_path.stem
file_path.suffix

file_path.parents[2]
#%%
file_path.exists()$\n$\n#%%$\ntmp_dir = pathlib.Path.cwd().joinpath('tmp_dir')
tmp_dir.mkdir()
tmp_dir.mkdir()
#%%
tmp_dir.mkdir(exist_ok=True)
file_path = tmp_dir.joinpath('tmp.txt')

with file_path.open(mode='w') as f:
    f.write('some line')
    pass

file_path.read_text()
#%%$\nfile_path.exists()
#%%
# safe file moving (avoids race conditions)
file_copy_path = file_path.parent / 'tmp2.txt'

with file_copy_path.open(mode='xb') as fid:
    fid.write(file_path.read_bytes())
# need to delete the old file now

file_copy_path.read_text()

# less safe file move
if not file_copy_path.exists():
    file_path.replace(file_copy_path)
#%%$\nfile_path.with_name('another_file.txt')  # same dir but another file
file_path.with_suffix('.py')  # same file name but another suffix
#%%$\n$\n# iterate over dir using .iterdir()
for p in pathlib.Path.cwd().iterdir():
    print(p)

print('\n Only directories')
for p in pathlib.Path.cwd().iterdir():
    if p.is_dir():
        print(p)

# using .glob() for file patterns
print('\n File type pattern')
for p in pathlib.Path.cwd().glob('*.to*'):
    print(p)

# recursive glob .rglob()
for p in pathlib.Path.cwd().rglob("*.ipynb"):
    print(p)
#%%$\nfile_path.unlink()
file_path.exists()
#%%$\n# use shutil (https://docs.python.org/3/library/shutil.html) for high level file operations (copy, remove, copytree, archive etc) - no support for this in pathlib for now

# os.walk functionality is also missing from pathlib
import os

for f in os.walk(tmp_dir):
    print(f)$\n$\n#%%$\ntmp_dir.rmdir()
#%% [markdown]
"""
## Binary and text files

* python handles 2 types of files: binary and text
* most of the files that require specific handling are binary : like .doc, .xls, .pdf, .png, .sqlite
* a test file has no special encoding (can be opened with text editor)

* open(filename, mode) function (context manager):
  - modes: 'r', 'w' (erases the existing file), 'x' (creating a file - will fail if already exists), 'a' (append, pointer at the end), 'r+' (read and change, pointer at the start)

* fileobj.read(size) - size in bytes, default - full file
* fileobj.name
* for text files: fileobj.readline(), fileobj.readlines()
* for line in fileobj:
      print)
"""
#%%$\nresource_dir = pathlib.Path.cwd() / 'src' / 'pathlib_rsrc'
text_file = resource_dir.joinpath('text_file.txt')$\n$\nif text_file.exists():
    text_file.unlink()

# creating text file (python built-in tools)
with open(text_file, mode='x') as f:
    f.write(
        """When a file operation fails for an I/O-related reason, 
    the exception IOError is raised. This includes situations where
     the operation is not defined for some reason, like seek() on a
      tty device or writing a file opened for reading."""
    )

# same as running f = open(...); ...; f.close()$\n$\nwith open(text_file, 'r+') as f:
    f.read()

with open(text_file, 'r+') as f:
    f.readline()
    next(f)

with open(text_file, 'r+') as f:
    f.readlines()

with open(text_file, 'r+') as f:
    for i, line in enumerate(f):
        print(f'line number {i}', line)

with open(text_file, 'r+') as f:
    f.seek(10)
    print(f.read())
    f.tell()
    f.write(" <extra string> ")

with open(text_file, 'r+') as f:
    print(f.read())$\n$\n#%%
# modes for binary files : 'xb', 'rb', 'wb'

binary_file = resource_dir.joinpath('binary_file')

with open(binary_file, 'xb') as f:
    f.write(b"some binary string")
#%%
binary_file.read_bytes()
#%% [markdown]

# full description here https://docs.python.org/2.4/lib/bltin-file-objects.html
#%%
with open(binary_file, 'rb+') as f:
    print(f.readline())
    # to write array to a binary file - use bytearray
    byte_array = bytearray([102, 4, 12])
    f.write(byte_array)$\n$\nbinary_file.read_bytes()
#%% [markdown]

# both text and binary files are sequences of bytes, but text files are stored as  it
# is, while binary files apply specific rules.
#
# in Python binary string can be encoded/decoded simply by putting ```b'in front of a string'```
#%%
# exists_ok and parents parameters
resource_dir.joinpath('level1', 'level2').mkdir(parents=True)
#%%$\nfor f in os.walk(resource_dir):
    print(f)
#%%
for f in resource_dir.glob("*"):
    print(f)
#%%
import shutil

shutil.copy(
    resource_dir / 'text_file.txt', resource_dir / 'nested_dir/text_file_copy.txt'
)
#%%
for f in resource_dir.rglob('text_*.txt'):
    print(f)$\n$\n#%% [markdown]
"""
## shutil methods

* .copy(source, dest)
* .copy2(..)  - preserve file metadata (like creation time)
* .move(..)
* copytree
* rename
* copyfileobj - copy file objects - can be used together with double ```open``` for overwrite security

(need to check if destination file exist, shutil will overwrite it)
has arg ```follow_symlinks``` to decide whether e.g. to copy a symlink or it's content (if true)

path.open(..) context manager is very useful to lock file and avoid race condition
(because the race condition can happen between any existence check and the next line)
"""
#%%
resource_dir.stat()
#%%$\nimport zipfile
import io

if resource_dir.joinpath('new.zip').exists():
    resource_dir.joinpath('new.zip').unlink()

file_list = ['text_file.txt', 'level1/']
with zipfile.ZipFile(resource_dir / 'new.zip', 'w') as new_zip:
    for name in file_list:
        new_zip.write(
            resource_dir / name, name
        )  # second arg - shortname (full path won't be stored)

with zipfile.ZipFile(resource_dir / 'new.zip', 'a') as new_zip:
    new_zip.write(resource_dir / 'binary_file', 'binary_file')
    [f.filename for f in new_zip.filelist]
    new_zip.namelist()

with zipfile.ZipFile(resource_dir / 'new.zip', 'r') as new_zip:
    new_zip.extractall(path=resource_dir / 'zip_extract/')

with zipfile.ZipFile(resource_dir / 'new.zip', 'r') as new_zip:
    with new_zip.open('binary_file') as f:
        f.read()
        isinstance(f, io.IOBase)
#%%
with open(resource_dir / 'binary_file', 'rb') as f:
    isinstance(f, io.BufferedIOBase)
    bytes_ = f.read()

binary_buffer = io.BytesIO(bytes_)

with open(resource_dir / 'binary_file2', 'wb') as f:
    f.write(binary_buffer.getvalue())

binary_buffer.close()  # discard buffer memory

resource_dir.joinpath('binary_file2').read_bytes()
#%%
# check path-like object in general
resource_dir.joinpath('binary_file2').read_bytes()$\n$\n#%%
import io

output = io.StringIO()
output.write("sample string")
output.seek(0)
output.read()
output.close()
#%%
# buff = io.BytesIO('àéè'.encode('utf-8'))

buff.getvalue()

text_wrapper = io.TextIOWrapper(buff, encoding='utf-8')
text_wrapper.seek(0)
text_wrapper.read()

b'\xc3\xa0\xc3\xa9\xc3\xa8'.decode('utf-8')
#%%
# working with yaml files (mostly used offline for config files)

import yaml

dct = {'first': [{'a': 5, 'b': 4}, {'x': 10, 'y': 12}], 'second': 5}

with open(resource_dir / 'test_yaml.yml', 'w') as f:
    yaml.dump(dct, f)$\n$\nwith open(resource_dir / 'test_yaml.yml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    type(data)
    print(data)$\n$\n#%%
# working with JSON (used for data transfer, e.g. by http APIs, cf requests)

import json

dct = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [{"firstName": "Alice", "age": 6}, {"firstName": "Bob", "age": 8}],
}

json.dumps(dct)

# serialization - process of encoding json

# python pickle uses format specific to python (that is not json)

with open(resource_dir / 'sample.json', 'w') as f:
    json.dump(dct, f)

with open(resource_dir / 'sample.json', 'r') as f:
    output = json.load(f)
    type(output)
    print(output)
#%%
import requests$\n$\nresponse = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos = response.json()  # same result$\n$\n# some simple python objects are naturally json-serializable (like e.g. tuple, list, dict)
json.dumps((5, 4))$\n$\n# set
set_ = {1, 2, 3}  # not serializable

# custom json encoder
def set_json_encoder(set_):
    return list(set_)$\n$\njson.dumps(set_, default=set_json_encoder)
