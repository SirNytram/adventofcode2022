# from typing import Dict

commands = open('day7ex.txt').read().split('\n')
            
class Folder:
    parent = None
    name = ''
    folders = {}
    files = {}
    # folders = Dict[str, object] = {}
    # files: Dict[str,int] = {}

    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        if parent:
            parent.folders[name] = self

    def get_size(self):
        size = 0
        for file in self.files.items():
            print(f'name: {file[0]} size: {file[1]}')
            size += file[1]

        for folder in self.folders.items():
            size += folder[1].get_size()

        print(f'name: {self.name[0]} size: {size}')
        return size

root:Folder = Folder(None, '')
curFolder = None
curCommand = None
for commandLine in commands:
    print(commandLine)
    items = commandLine.split(' ')
    if items[0] == '$':
        if items[1] == 'cd':
            if items[2] == '/':
                curFolder = root
            elif items[2] == '..':
                curFolder = curFolder.parent
            else:
                curFolder = curFolder.folders[items[2]]
        elif items[1] == 'ls':
            curCommand = 'ls'
    else:
        if curCommand == 'ls':
            if items[0] == 'dir':
                Folder(curFolder, items[1])
            else:
                curFolder.files[items[1]] = int(items[0])


print(root.get_size())
