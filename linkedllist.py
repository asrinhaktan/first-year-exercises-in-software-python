#önceki ve sonraki düğümü belirtir
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class ListArray:
    def __init__(self):
        self.firstNode = None       #first node ilk düğümü tutmak için
        self.lastNode = None        #last node son düğümü tutmak için
        self.redoLastNode = None    #çıkarttığımız elemanları redolastnode ile ilerliyoruz
        self.redoCounter = 0        #sayaç

#undo redo veya yaz girilmediği sürece listeye ekleme kısmı
    def ekle(self, data):
        lList = LinkedList(data)

        if self.firstNode is None:
            self.firstNode = lList
            self.lastNode = self.firstNode   #birinci ve ikinci eleman birbirine bağlansın diye
        else:
            lList.prev = self.lastNode
            self.lastNode.next = lList
            self.lastNode = lList

        self.redoLastNode = None     #ekleme yapıldıktan sonra redo olmasın diye
        self.redoCounter = 0

#silinen elemanı tekrar listeye eklemek için
    def redo(self):
        if self.redoCounter <= 0:
            return

        if self.redoLastNode is None:
            return

        yedekBefore = None         #buradaki amaç redonun son elemanı bir yere kaybolmasın diye
        if self.redoLastNode.prev is not None:
            yedekBefore = self.redoLastNode.prev
            yedekBefore.next = None

        if self.lastNode is None:
            self.lastNode = self.redoLastNode
            self.lastNode.prev = None
            if self.firstNode is None:
                self.firstNode = self.redoLastNode
        else:
            self.lastNode.next = self.redoLastNode
            self.redoLastNode.prev = self.lastNode
            self.lastNode = self.redoLastNode
        self.redoLastNode = yedekBefore

        self.redoCounter -= 1            #buradaki amaç sıfırdan küçük ise buraya girilmez(5 elemandan fazla yapılamaz)
        if self.redoCounter < 0:
            self.redoCounter = 0

    def undo(self):
        if self.lastNode is None:        #asıl listedeki son elemanı yedekte tutmak için
            return

        yedekBefore = None               #last node olarak düşünülür
        if self.lastNode.prev is not None:
            yedekBefore = self.lastNode.prev
            yedekBefore.next = None
        else:
            self.firstNode = None

        if self.redoLastNode is None:
            self.redoLastNode = self.lastNode
            self.redoLastNode.prev = None
        else:
            self.redoLastNode.next = self.lastNode
            self.lastNode.prev = self.redoLastNode
            self.redoLastNode = self.lastNode

        self.lastNode = yedekBefore
        print(self.lastNode)

#max 5e kadar geri aldırılır.

        self.redoCounter += 1
        if self.redoCounter > 5:
            self.redoCounter = 5

#başından başlayıp listeyi bastırmak
    def yaz(self):
        gezgin = self.firstNode
        counter = 10
        count = 0
        while gezgin is not None:
            print(gezgin.data)
            gezgin = gezgin.next
            count += 1
            if count > counter:
                break


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
