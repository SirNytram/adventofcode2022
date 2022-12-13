# from typing import Dict

commands = open('day7.txt').read().split('\n')
ans = 0
            
class Folder:

    def __init__(self, parent, name) -> None:
        self.folders = {}
        self.files = {}

        self.parent = parent
        self.name = name
        if parent:
            parent.folders[name] = self

    def get_size(self):
        global ans
        size = 0
        for file in self.files.items():
            # print(f'size file: {file[0]} size: {file[1]}')
            size += file[1]

        for folder in self.folders.items():
            size += folder[1].get_size()

        print(f'size folder: {self.name[0]} size: {size}')
        if size < 100000:
            print('ok one')
            ans += size

            
        return size

root:Folder = Folder(None, '/')
curFolder = None
curCommand = None
for commandLine in commands:
    # print(commandLine)
    items = commandLine.split(' ')
    if items[0] == '$':
        if items[1] == 'cd':
            if items[2] == '/':
                print(f'root {commandLine}')
                curFolder = root
            elif items[2] == '..':
                print(f'moveup {commandLine}')
                curFolder = curFolder.parent
            else:
                foldername = items[2]
                print(f'cd {foldername} {commandLine}')
                curFolder = curFolder.folders[foldername]
        elif items[1] == 'ls':
            curCommand = 'ls'
    else:
        if curCommand == 'ls':
            if items[0] == 'dir':
                name = items[1]
                print(f'new folder {name} {commandLine}')
                Folder(curFolder, name)
            else:
                name = items[1]
                print(f'new file {name} {commandLine}')
                curFolder.files[name] = int(items[0])


print(root.get_size())
print(f'ans: {ans}')
