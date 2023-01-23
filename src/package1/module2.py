from pathlib import Path


def root_path():
    return Path.cwd()


if __name__ == '__main__':
    resolved_path = root_path()
    assert str(resolved_path) == r'D:\G-Doc\YandexDisk\Scripts\_Educational\Project Structures\project-structure-classic\src', f'got: {resolved_path}'
