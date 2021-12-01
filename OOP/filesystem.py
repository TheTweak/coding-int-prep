'''
Explain the data structures and algorithms that you would use to design an in-memory
file system. Illustrate with an example in code where possible.
'''

class FileDescription:
    def __init__(self, file: str):
        self.file = file
        self.offset = 0


class FileDescriptor:
    def __init__(self, description: FileDescription, flags: int):
        self.description = description
        self.flags = flags


class FSTreeNode:
    pass

class FSTreeNode:
    def __init__(self, name: str):
        self.parent: FSTreeNode = None
        self.child: list[FSTreeNode] = []
        self.name: str = name
        self.is_dir = False
    
    def get_full_path(self) -> str:
        pass


class InMemoryFS:
    def __init__(self):
        self.fs_root: FSTreeNode = FSTreeNode('/')
        self.file_data: dict[str:bytes] = {}
        self.file_descriptions: list[FileDescription] = []
        self.file_descriptors: list[FileDescriptor] = []

    def read(self, fd: int, bytes_cnt: int, bytes: bytes) -> int:
        pass

    def write(self, fd: int, bytes: bytes) -> int:
        pass

    def open(self, path: str, flags: int) -> int:
        pass

    def remove(self, path: str) -> int:
        pass

    def __find_fs_node(self, path: str, root: FSTreeNode) -> FSTreeNode:
        if root.get_full_path() == path:
            return root

        for n in root.child:
            result = self.__find_fs_node(path, n)
            if result:
                return result
        
        return None

    def mkdir(self, path: str) -> int:
        parent_path = '/'.join(path.split('/')[:-1])
        parent_fs_node = self.__find_fs_node(parent_path, self.fs_root)

        if not parent_fs_node:
            raise RuntimeError(f'Directory {parent_path} does not exist')

        fsnode = FSTreeNode(path)
        fsnode.parent = parent_fs_node
        parent_fs_node.child.append(fsnode)
        return 1
