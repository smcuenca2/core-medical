class Concept():
    code = None
    term = None
    terminology = None
    original_terminologies = None

    def __repr__(self):
        return str(self.__dict__)


class Relation(Concept):
    def __repr__(self):
        return str(self.__dict__)


class ConceptDTO(Concept):
    relation = Relation

    def __repr__(self):
        return str(self.__dict__)
