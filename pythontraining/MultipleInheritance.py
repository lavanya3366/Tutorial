class Base1:
    def funcBase1(self):
        print("funcBase1() is executing...")
class Base2:
    def funcBase2(self):
        print("funcBase2() is executing...")
class Base3:
    def funcBase3(self):
        print("funcBase3() is executing...")
class MultiDerived(Base1,Base2,Base3):
    def funcMultiDerived(self):
        print("funcMultiDerived() is executing...")
