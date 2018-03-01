# Reading a file in Python3

## This code does

- Read a file
- Rewinds a file
- Reads a line

> Reads a file

```python
read_all(filename)
```

> Rewind a file

```python
rewind(filename, line_number):
```

> Print a line

```python
get_line(filename)
```

### Usage 
 
 ```python 
 from read_line_py3 import Filereader
 
freader_object = Filereader()

input_file = "stuff.txt"

current_file = open(input_file,"r") 
```