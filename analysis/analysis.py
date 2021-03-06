from DNA.existing_DNA import Existing_DNA

#The class is the 'frame' of all the analysis commands
class Analysis:
    existing_DNA=Existing_DNA()

    # Get the DNA sequence object by a name or id of a sequence.
    def extract_sequence(self, identity):
        if identity[0] == '#':
            return Analysis.existing_DNA.get_DNAs(int(identity[1:]))
        elif identity[0]=='@':
            id = Analysis.existing_DNA.get_names(identity[1:])
            return Analysis.existing_DNA.get_DNAs(id)
        else:
            print('DNA identity is not valid')

    #Get the wanted sequence by id ,name ot the seq itself.
    def get_seq_to_find(self, seq_to_be_found):
        if seq_to_be_found[0] in ["@", "#"]:
            seq = self.extract_sequence(seq_to_be_found)
            seq_to_find = seq.get_seq()
        else:
            seq_to_find = seq_to_be_found
        return seq_to_find

