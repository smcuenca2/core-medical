class SicknessTreatDTO():
    code = None
    term = None
    terminology = None
    original_terminologies = None
    term_rel = None

    def __repr__(self):
        return str(self.__dict__)
