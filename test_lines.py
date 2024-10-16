from lines import count_lines_of_code, get_filename_from_argv
import pytest

def test_count_lines_of_code():
    assert count_lines_of_code("path_test/testfile.py") == 4

def test_get_filename_from_argv():
    args = ["test_lines.py", "lines.py"]
    assert get_filename_from_argv(args) == "lines.py"

def test_too_many_arguments():
    args = ["test_lines.py", "lines.py", "test"]
    with pytest.raises(SystemExit) as e:
        get_filename_from_argv(args)
    assert "Too many arguments" in str(e.value)

def test_too_few_arguments():
    args = ["test_lines.py"]
    with pytest.raises(SystemExit) as e:
        get_filename_from_argv(args)
    assert "Too few arguments" in str(e.value)

def test_not_a_python_file():
    args = ["test_lines.py", "lines"]
    with pytest.raises(SystemExit) as e:
        get_filename_from_argv(args)
    assert "Not a Python File" in str(e.value)

def test_file_not_found():
    with pytest.raises(FileNotFoundError) as e:
        count_lines_of_code("path_test/Hello.py")
    assert "File not found" in str(e.value)


        