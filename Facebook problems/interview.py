#Given an unordered list of directories remove any directories that are ancestors of other directories in the list and return the new list. Order of results is irrelevant.
# e.g.: ['/abc/xyc', '/def/', '/def/foo', '/'] => ['/abc/xyc', '/def/foo']
# e.g.: ['/', '/abc/xyc', /abc/xyc/def/', '/abc/xyc/foo'] => ['/abc/xyc/def/', '/abc/xyc/foo']
class Node:
    def __init__(self, info):
        self.info = info
        self.children = {}

    def __repr__(self):
        return 'Im: {}'.format(self.info)

    def getLeafs(self):
        queue = [self]
        [queue.append(x) for x in self.children.values()]
        curnode = queue.pop(0)
        res = []
        i = 0
        while len(queue) >= 0 and i <= 15:
            i += 1
            if len(curnode.children.keys()) == 0:
                res.append(curnode.info)
                try:
                    curnode = queue.pop(0)
                except:
                    return res
            else:
                curnode = queue.pop(0)
                [queue.append(x) for x in curnode.children.values()]
        return res

    def addChild(self, node):
        curnode = self
        i = 1
        curdir = node[0]
        n = 0
        if node[-1] != '/':
            node += '/'
        while curdir != node:
            curdir = node[:node.index('/', i)]
            try:
                curnode = curnode.children[curdir]
            except:
                curnode.children[curdir] = Node(curdir)
                curnode = curnode.children[curdir]
            i = len(curdir)+1
            if i >= len(node):
                break

    def buildTree(self, dirs):
        for dir in dirs:
            pass

def remove_directories(dirs):
    root = Node('/')
    for dir in dirs:
        if dir == '/':
            continue
        root.addChild(dir)
    return root.getLeafs()

print(remove_directories(['/', '/abc/xyc', '/abc/xyc/def/', '/abc/xyc/foo']))
print(remove_directories(['/abc/xyc', '/def/', '/def/foo', '/']))



# Write a function to check if two integers are digit-shuffled. It returns true if the a, b have the same digits. Example is_shuffled(123, 231) = true and is_shuffled(123, 124) = false.
# def is_shuffled(a, b):
#     a1 = [0]*10
#     b1 = [0]*10
#     a = str(a)
#     b = str(b)
#     for digit in a:
#         a1[int(digit)] += 1
#     for digit in b:
#         b1[int(digit)] += 1
#     if a1 != b1:
#         return False
#     return True
# print(is_shuffled(112, 221))





#
