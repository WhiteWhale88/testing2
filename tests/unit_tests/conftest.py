''' Фикстуры для pytest '''
import pytest


@pytest.fixture
def file_valid_data(tmp_path):
    '''Файл с верными данными'''
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w", encoding="UTF-8") as f:
        f.write("234,0\t67,99")
    return file_path


@pytest.fixture
def file_invalid_data(tmp_path):
    '''Файл с нечитаемыми данными'''
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w", encoding="UTF-8") as f:
        f.write("invalid")
    return file_path
