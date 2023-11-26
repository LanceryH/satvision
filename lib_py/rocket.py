class Rocket_class:
    def __init__(self,STAGES="undefined",PAYLOAD_MASS=0.0,FAIRING_MASS=0.0):
        self.STAGES = STAGES
        self.TOTAL_MASS = 0.0
        self.PAYLOAD_MASS = PAYLOAD_MASS
        self.FAIRING_MASS = FAIRING_MASS

    def build(self):
        for index in self.STAGES:
            self.TOTAL_MASS += index.PROPELLANT_MASS + index.STRUCTURAL_MASS
        self.TOTAL_MASS += self.PAYLOAD_MASS + self.FAIRING_MASS