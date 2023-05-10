class Fractie(object):
    def __init__(self):
        self.numarator = None
        self.numitor = None

    def __str__(self):
        return str(self.numarator)+"/"+str(self.numitor)

    def __add__(self, other):
        return str(self.numarator + other.numarator)+"/"+str(self.numitor + other.numitor)

    def __sub__(self, other):
        return str(self.numarator - other.numarator)+"/"+str(self.numitor - other.numitor)

    def inverse(self):
        return str(self.numitor)+"/"+str(self.numarator)

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
    print("afisam \"numărător/numitor\": "+str(f1))
    print("returnam o noua fractie care reprezinta adunarea: "+str(f1 + f2))
    print("returnam o nouă fracție care reprezinta scădearea: "+str(f1 - f2))
    print("returnează o nouă fracție (inversa fracției): "+str(f1.inverse()))


main()
