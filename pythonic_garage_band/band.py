
class Band:

    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __str__(self):
        return f"Band: {self.name}"

    def __repr__(self):
        return f'Band("{self.name, self.members}")'

    def to_list(self):
        pass

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.solo)
        return solos



class Musician:
    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f'Musician("{self.name}")'

    def get_instrument(self):
        return(self.instrument)

    def play_solo(self):
        return(self.solo)


class Guitarist(Musician):
    def __init__(self, name):
        Musician.__init__(self, name, "guitar", "face melting guitar solo")

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

class Bassist(Musician):
    def __init__(self, name):
        Musician.__init__(self, name, "bass", "bom bom buh bom")
    
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

class Drummer(Musician):
    def __init__(self, name):
        Musician.__init__(self, name, "drums", "rattle boom crash")
    
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'