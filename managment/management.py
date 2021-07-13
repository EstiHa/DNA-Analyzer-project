from DNA.existing_DNA import Existing_DNA

#The class is the 'frame' of all the managment commands
class Management:
    existing_DNA=Existing_DNA()

    # Get the DNA sequence object by a name or id of a sequence.
    def extract_sequence(self, identity):
        if identity[0] == '#':
            return Management.existing_DNA.get_DNAs(int(identity[1:]))
        elif identity[0]=='@':
            id = Management.existing_DNA.get_names(identity[1:])
            return Management.existing_DNA.get_DNAs(id)
        else:
            print('DNA identity is not valid')