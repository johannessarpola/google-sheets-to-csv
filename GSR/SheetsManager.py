import SheetDataStore

class Manager:
    def __init__(self, store):
        out = SheetDataStore.parseDataToSheet(SheetDataStore.readData(store))
        self.storage = out
        self.nextindex = 0
        self.hasnext = True

    def getNext(self):
        if(self.hasnext == True):
            sheet = self.storage[self.nextindex]
            self.nextindex += 1
            if(self.nextindex == len(self.storage)):
                self.hasnext = False
            return sheet
        else:
            return None

    def hasNext(self):
        return self.hasnext
