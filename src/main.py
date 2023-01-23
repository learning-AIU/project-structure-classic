import package1.module2 as m2


def main():
    """"""


if __name__ == '__main__':
    main()

    resolved_path = m2.root_path()
    assert str(resolved_path) == r'D:\G-Doc\YandexDisk\Scripts\_Educational\Структуры проектов\project\src', f'got: {resolved_path}'
