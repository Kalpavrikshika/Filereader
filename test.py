from read_line_py3 import Filereader

f_reader = Filereader()
data_file = open("stuff.txt","r")

#current_file = data_file.read()
whole_file = """this is a text file
that does some cool stuff
hope it is read well
with no mistakes."""

def test_read_file():
    data = f_reader.read_all(data_file)
    assert data == whole_file

def test_seek_contents():
    seek_pointer = 0
    data = f_reader.rewind(data_file, seek_pointer)
    expect_seek = 0
    assert data == expect_seek

def test_line_read():
    data = f_reader.get_line(data_file)
    expect_line = 'this is a text file\n'
    assert data == expect_line
