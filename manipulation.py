from dna_sequence import DnaSequence
from existing_DNA import Existing_DNA


class Manipulation:
    existing_DNA=Existing_DNA()

    def keep_manipulate(self, command,dna_object, manipulate_seq, default_name):
        split_command=''.join(command).split(":")
        if len(split_command)>1:
            new_sequence=split_command[1].split()
            if new_sequence[0]=='@@':
                i=1
                while True:
                    name=f'{dna_object.get_name()}_{default_name}{i}'
                    if name in Manipulation.existing_DNA.get_names().keys():
                        i+=1
                    else:
                        break
                new_seq=DnaSequence(manipulate_seq, name)
            else:
                new_seq = DnaSequence(manipulate_seq, new_sequence[0][1:])
            Manipulation.existing_DNA.add_new_DNA(new_seq.id, new_seq)
            Manipulation.existing_DNA.add_name(new_seq.id, new_seq.name)
            print(f"[{new_seq.id}] {new_seq.name}: {manipulate_seq}")
        else:
            dna_object.assignment(manipulate_seq)
            print(f"[{dna_object.get_id()}] {dna_object.get_name()}: {manipulate_seq}")

    def extract_sequence(self, identity):
        if identity[0] == '#':
            return Manipulation.existing_DNA.get_DNAs(int(identity[1:]))
        elif identity[0]=='@':
            id = Manipulation.existing_DNA.get_names(identity[1:])
            return Manipulation.existing_DNA.get_DNAs(id)
        else:
            print('DNA identity is not valid')




