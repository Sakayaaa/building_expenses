from model.entity import *


class Units(Base):
    __tablename__ = 'units'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _unit_no = Column("unit_no", Integer, unique=True, nullable=False)
    _name = Column("name", String(30), nullable=False)
    _family = Column("family", String(30), nullable=False)
    _no_people = Column("no_people", Integer, nullable=False)

    def __init__(self, unit_no, name, family, no_people):
        self.id = None
        self.unit_no = unit_no
        self.name = name
        self.family = family
        self.no_people = no_people

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        self._family = value

    @property
    def no_people(self):
        return self._no_people

    @no_people.setter
    def no_people(self, value):
        self._no_people = value

    @property
    def unit_no(self):
        return self._unit_no

    @unit_no.setter
    def unit_no(self, value):
        self._unit_no = value
