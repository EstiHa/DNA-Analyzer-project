from DNA.dna_sequence import DnaSequence
from DNA.existing_DNA import Existing_DNA

#The class is the 'frame' of all the manipulation commands
class Manipulation:
    existing_DNA=Existing_DNA()

#This function gets the manipulated sequence and updates it.
    def keep_manipulate(self, new_seq_details ,dna_object, manipulate_seq, default_name):
        if new_seq_details!=None:
            new_seq_details.split()
            if new_seq_details[1]=='@@':
                i=1
                while True:
                    name=f'{dna_object.get_name()}_{default_name}{i}'
                    if name in Manipulation.existing_DNA.get_names().keys():
                        i+=1
                    else:
                        break
                new_seq=DnaSequence(manipulate_seq, name)
            else:
                new_seq = DnaSequence(manipulate_seq, new_seq_details[1][1:])
            Manipulation.existing_DNA.add_new_DNA(new_seq.id, new_seq)
            Manipulation.existing_DNA.add_name(new_seq.id, new_seq.name)
            return f"[{new_seq.id}] {new_seq.name}: {manipulate_seq}"
        else:
            dna_object.assignment(manipulate_seq)
            return f"[{dna_object.get_id()}] {dna_object.get_name()}: {manipulate_seq}"

#Get the DNA sequence object by a name or id of a sequence.
    def extract_sequence(self, identity):
        if identity[0] == '#':
            return Manipulation.existing_DNA.get_DNAs(int(identity[1:]))
        elif identity[0]=='@':
            id = Manipulation.existing_DNA.get_names(identity[1:])
            return Manipulation.existing_DNA.get_DNAs(id)
        else:
            print('DNA identity is not valid')




