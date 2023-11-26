class Stage_class:
    def __init__(self,
                 PROPELLANT_TYPE="undefined",
                 PROPELLANT_MASS="undefined",
                 STAGE_NUMBER="undefined"):
        self.STAGES_CHAR={"Solid":{"allow":[1],
                                   "Isp":{"1":266},
                                   "Struct_Ind":0.12},
                         "LOX-RP1":{"allow":[1,2,3],
                                     "Isp":{"1":285,
                                            "2":320,
                                            "3":320},
                                     "Struct_Ind":0.16},
                          "LOX-LK2":{"allow":[2,3],
                                     "Isp":{"2":450,
                                            "3":450},
                                     "Struct_Ind":0.25}}
        self.STAGE_NUMBER = STAGE_NUMBER
        self.PROPELLANT_TYPE = PROPELLANT_TYPE
        self.PROPELLANT_MASS = PROPELLANT_MASS
        self.STRUCTURAL_MASS = 0
        self.TOTAL_MASS = 0
        self.ISP = self.STAGES_CHAR[self.PROPELLANT_TYPE]["Isp"][STAGE_NUMBER]
        self.STRUCTURAL_INDEX = self.STAGES_CHAR[self.PROPELLANT_TYPE]["Struct_Ind"]
    def build(self):
        self.STRUCTURAL_MASS = self.STRUCTURAL_INDEX*self.PROPELLANT_MASS
        self.TOTAL_MASS = self.STRUCTURAL_MASS + self.PROPELLANT_MASS 