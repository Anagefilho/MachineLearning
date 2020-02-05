class Conjuntos:
    dict = {}
    objects = []

    def __init__(self, dict,poda):
        self.dict = dict
        self.poda = poda

    def setPoda(self):
        self.poda = 1
    def getPoda(self):
        return self.poda

    def getFreq(self):
        return self.dict[2]

    def save(self):
        self.__class__.objects.append(self)


    def __repr__(self):
        return '<Conj. {} - Podado? {}>\n'.format(self.dict, self.poda)

    @classmethod
    def all(cls):
        return cls.objects

c1 = Conjuntos({"agag": 10,"bbbalga":20}, 0)
c1.save()
print(c1)
for x in c1.dict.values():
    print(x)
