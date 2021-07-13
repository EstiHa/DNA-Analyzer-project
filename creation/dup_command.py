from DNA.dna_sequence import DnaSequence
from DNA.existing_DNA import Existing_DNA

class Dup:
    existing_DNA=Existing_DNA()

    def __init__(self, command):
        try:
            self.new_seq_name=None
            self.seq_to_dup=command[1]
            if len(command)>2:
                self.new_seq_name=command[2]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            if self.new_seq_name!=None:
                name= self.new_seq_name[1:]
            else:

                if self.seq_to_dup[0]=='#':
                    i=1
                    seq_to_dup = Dup.existing_DNA.get_DNAs(int(self.seq_to_dup[1:]))
                    name = f'{seq_to_dup.name}_{i}'
                    while True:
                        name1=name
                        for val in Dup.existing_DNA.get_DNAs().values():
                            name=name1
                            if name==val.name:
                                i+=1
                                name=f'{seq_to_dup.name}_{i}'
                        if name==name1:
                            break
                else:
                    i=1
                    name = f'{self.seq_to_dup[1:]}_{i}'
                    while True:
                        name1=name

                        for val in Dup.existing_DNA.get_DNAs().values():
                            if name==val.name:
                                i+=1
                                name=f'{self.seq_to_dup[1:]}_{i}'
                        if name==name1:
                            break
            sequence=''
            if self.seq_to_dup[0]=='#':
                for key in Dup.existing_DNA.get_DNAs().keys():
                    if int(self.seq_to_dup[1:])==key:
                        sequence=Dup.existing_DNA.get_DNAs(key).DNA_seq
            else:
                for val in Dup.existing_DNA.get_DNAs().values():
                    if self.seq_to_dup[1:] == val.name:
                        sequence = val.DNA_seq

            new_seq=DnaSequence(sequence,name)
            Dup.existing_DNA.add_new_DNA(DnaSequence.instance_number, new_seq)
            Dup.existing_DNA.add_name(DnaSequence.instance_number, new_seq.name)
            return f"[{DnaSequence.instance_number}] {name}: {sequence}"

        except IndexError:
            print("Not enough arguments in order to dup DNA")
        except ValueError:
            print("The sequence is invalid")
        except Exception as e:
            print("e is:" ,e)