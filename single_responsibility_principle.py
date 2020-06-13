# SRP - Separation of concern
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_enrty(self, pos):
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        return '\n'.join(self.entries)

    # additional responsibility for persistence
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


# separate the method to do other functionality with object like saving the object
class PersistenceManager:
    @staticmethod
    def save(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('my name is Akshay')
j.add_entry('I am an engineer')

file = r'C:\Users\akshay.dhotre\codeingWorkspaces\pythonWorkspace\designPatternsWithPython\journal.txt'
PersistenceManager.save(j, file)

with open(file) as fh:
    print(fh.read())
