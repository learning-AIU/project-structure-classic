from pathlib import Path
from sys import path


def root_path():
    return Path(path[0]).parent


if __name__ == '__main__':
    resolved_path = root_path()
    assert str(resolved_path) == r'D:\G-Doc\YandexDisk\Scripts\_Educational\Структуры проектов\project\src', f'got: {resolved_path}'
