# DIP
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


# low level module
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_child(self, parent_entity, child):
        self.relations.append(
            (parent_entity, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent_entity)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# high level module
class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'Adinath' and r[1] == Relationship.PARENT:
    #             print(f'Adinath has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('Adinath'):
            print(f'Adinath has a child called {p}')


parent = Person('Adinath')
child1 = Person('Akshay')
child2 = Person('Rohit')

relationship = Relationships()
relationship.add_parent_child(parent, child1)
relationship.add_parent_child(parent, child2)
Research(relationship)
