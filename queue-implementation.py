class Queue:
    def __init__(self):
        self.cue = []

    def encue(self,item):
        self.cue.append(item)

    def decue(self):
        if len(self.cue) < 1:
            return None
        self.cue.pop(0)

    def display(self):
        print(self.cue)

    def size(self):
        return len(self.cue)

         


obj = Queue()

obj.display()

obj.encue(1)

obj.encue(3)
obj.encue(2)
obj.decue()



obj.display()