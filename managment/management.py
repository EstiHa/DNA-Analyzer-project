from DNA.existing_DNA import Existing_DNA

class Management:
    existing_DNA=Existing_DNA()

    def extract_sequence(self, identity):
        if identity[0] == '#':
            return Management.existing_DNA.get_DNAs(int(identity[1:]))
        elif identity[0]=='@':
            id = Management.existing_DNA.get_names(identity[1:])
            return Management.existing_DNA.get_DNAs(id)
        else:
            print('DNA identity is not valid')