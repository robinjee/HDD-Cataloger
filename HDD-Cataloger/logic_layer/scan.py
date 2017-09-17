

class Scan:
    
    def __init__(self, disk):
        self.diskPath = disk
        

    def addDisk():
        for root, dirs, files in os.walk(diskPath):
            for file in files:
                if file.endswith(".txt"):
                    print(os.path.join(root, file))