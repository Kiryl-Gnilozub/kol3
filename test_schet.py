import os
import subprocess
import pytest

def test_script_execution():
    subprocess.run(["python", "schet.py", ".", "2"], capture_output=True, text=True)
    out_file_path = os.path.join(".", "out.dat")
    assert os.path.isfile(out_file_path)

    with open(out_file_path, "r") as out_file:
        content = out_file.readlines()

    for line in content:
        assert "from" in line

def test_output_file_content():
    subprocess.run(["python", "schet.py", ".", "2"], capture_output=True, text=True)

    with open("out.dat", "r") as output_file:
        content = output_file.readlines()

    for line in content:
        assert "from" in line

def test_invalid_directory():
    result = subprocess.run(
        ["python", "schet.py", "invalid_directory", "2"],
        capture_output=True, text=True
    )

    assert result.returncode != 0
    assert "FileNotFoundError" in result.stderr
