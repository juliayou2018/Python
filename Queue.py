class Queue(object):
    def __init__(self):
        self.qlist = []

    def insert(self, element):
        self.qlist.append(element)

    def remove(self):
        if self.qlist == []:
            raise ValueError()
        else:
            return self.qlist.pop(0)
