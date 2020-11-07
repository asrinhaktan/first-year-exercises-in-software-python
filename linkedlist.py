class LinkedList:                 
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class ListArray:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.redoLastNode = None
        self.redoFirstNode = None
        self.redoCounter = 0

    def ekle(self, data):
        lList = LinkedList(data)

        if self.firstNode is None:
            self.firstNode = lList
            self.lastNode = self.firstNode
        else:
            if self.lastNode is None:
                self.firstNode.next = lList
                self.lastNode = lList
                lList.prev = self.firstNode
            else:
                lList.prev = self.lastNode
                self.lastNode.next = lList
                self.lastNode = lList

        self.redoFirstNode = None
        self.redoLastNode = None
        self.redoCounter = 0

    def redo(self):
        if self.redoCounter <= 0: return

        if self.redoFirstNode is not None:
            data = None
            if self.redoLastNode is not None:
                data = self.redoLastNode.data
                if self.redoLastNode.prev is None:
                    self.redoLastNode = None
                    self.redoFirstNode = None
                else:
                    self.redoLastNode.prev.next = None
                    self.redoLastNode = self.redoLastNode.prev

            else:
                data = self.redoFirstNode.data
                self.redoFirstNode = None

            yedek = LinkedList(data)
            if self.firstNode is None:
                self.firstNode = yedek
                self.lastNode = yedek
            else:
                yedek.prev = self.lastNode
                self.lastNode.next = yedek
                self.lastNode = yedek

        self.redoCounter -= 1
        if self.redoCounter < 0:
            self.redoCounter = 0

    def undo(self):
        if self.firstNode is not None:
            if self.redoFirstNode is None:
                self.redoFirstNode = LinkedList(self.lastNode.data)
                self.redoFirstNode.next = None
                self.redoFirstNode.prev = None
            else:
                if self.redoLastNode is None:
                    self.redoLastNode = LinkedList(self.lastNode.data)
                    self.redoLastNode.prev = self.redoFirstNode
                    self.redoLastNode.next = None
                    self.redoFirstNode.next = self.redoLastNode
                else:
                    yedek = LinkedList(self.lastNode.data)
                    yedek.prev = self.redoLastNode
                    self.redoLastNode.next = yedek
                    self.redoLastNode = yedek

            if self.lastNode.prev is None:
                self.lastNode = None
                self.firstNode = None
            else:
                self.lastNode.prev.next = None
                self.lastNode = self.lastNode.prev

        self.redoCounter += 1
        if self.redoCounter > 5:
            self.redoCounter = 5

    def yaz(self):
        gezgin = self.firstNode

        while gezgin is not None:
            print(gezgin.data)
            gezgin = gezgin.next


listArray = ListArray()

while True:
    girdi = input("islem: ")
    if girdi == "redo":
        listArray.redo()
    elif girdi == "undo":
        listArray.undo()
    elif girdi == "yaz":
        listArray.yaz()
    else:
        listArray.ekle(girdi)
