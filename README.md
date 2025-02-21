# Python Reference
Quick reference for some useful Python modules

## Examples

### argparse
Useful for processing command-line arguments in your scripts.

[Basics](argparser.py)

```python
> ./argparser.py -h
usage: main.py [-h] [--verbose] num

General description

positional arguments:
  num            required number

optional arguments:
  -h, --help     show this help message and exit
  --verbose, -v  optional flag

> ./argparser.py 10
Namespace(num=10, verbose=False)

> ./argparser.py -v 10
Namespace(num=10, verbose=True)
```

[Repeated field](cat.py)

```python
> ./cat.py -h
usage: cat.py [-h] files [files ...]

print files to standard output

positional arguments:
  files       files

optional arguments:
  -h, --help  show this help message and exit

> ./cat.py hello.txt foo.txt
Namespace(files=['hello.txt', 'foo.txt'])
hello, world!
bar
```

---

### pickle
Good for serializing simple Python data structures to a file.

[Pickle viewer script](pickle_viewer.py)

```python
> ./pickle_viewer.py --pretty example.pickle
{ 'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'text': {'hello': 'world!', 'foo': 'bar'}}
```
