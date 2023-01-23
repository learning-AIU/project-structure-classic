import src.package1.module2 as m2


def test_m2_root_path():
    resolved_path = m2.root_path()
    assert str(resolved_path) == r'D:\G-Doc\YandexDisk\Scripts\_Educational\Project Structures\project-structure-classic\src'
