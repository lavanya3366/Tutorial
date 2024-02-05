class myBird:
    def __init__(self):
        print("myBird class constructor is executing..")

    def whatType(self):
        print("I am a bird...")

    def canSwim(self):
        print("I can swim..")

class myPenguin(myBird):
    def __init__(self):
        super().__init__()
        print("myPenguin class constructor is running..")

    def whoisThis(self):
        print("I am a penguin..")

    def canRun(self):
        print("Can run")

ob1 = myPenguin()
ob1.whatType()
ob1.whoisThis()
ob1.canSwim()
ob1.canRun()
