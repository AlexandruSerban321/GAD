class Fractie(object):
    def __init__(self):
        self.numarator = None
        self.numitor = None

    def __str__(self):
        return str(self.numarator) + "/" + str(self.numitor)

    def __add__(self, other):
        return "numitor_nou: " + str(self.numitor + other.numitor) + " numarator_nou: "\
            + str(self.numarator + other.numarator)

    def __sub__(self, other):
        return "numitor_nou: " + str(self.numitor - other.numitor) + " numarator_nou: "\
            + str(self.numarator - other.numarator)

    def inverse(self):
        return "numitor_nou: " + str(self.numarator) + " numarator_nou: " + str(self.numitor)

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def set_numitor(self, new_numitor):
        self.numitor = new_numitor

    def set_numarator(self, new_numarator):
        self.numarator = new_numarator


def main():
    f1 = Fractie()
    f2 = Fractie()
    f1.set_numarator(2)
    f1.set_numitor(3)
    f2.set_numarator(4)
    f2.set_numitor(5)
    print(f1 + f2)
    print(f1 - f2)
    print(f1.inverse())


print(main())
