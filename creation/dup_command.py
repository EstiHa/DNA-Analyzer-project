from DNA.dna_sequence import DnaSequence
from DNA.existing_DNA import Existing_DNA

class Dup:
    existing_DNA=Existing_DNA()

    def perform_action(self, command):
        try:
            if len(command)>2:
                name= command[2][1:]
            else:

                if command[1][0]=='#':
                    i=1
                    seq_to_dup = Dup.existing_DNA.get_DNAs(int(command[1][1:]))
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
                    name = f'{command[1][1:]}_{i}'
                    while True:
                        name1=name

                        for val in Dup.existing_DNA.get_DNAs().values():
                            if name==val.name:
                                i+=1
                                name=f'{command[1][1:]}_{i}'
                        if name==name1:
                            break
            sequence=''
            if command[1][0]=='#':
                for key in Dup.existing_DNA.get_DNAs().keys():
                    if int(command[1][1:])==key:
                        sequence=Dup.existing_DNA.get_DNAs(key).DNA_seq
            else:
                for val in Dup.existing_DNA.get_DNAs().values():
                    if command[1][1:] == val.name:
                        sequence = val.DNA_seq

            new_seq=DnaSequence(sequence,name)
            Dup.existing_DNA.add_new_DNA(DnaSequence.instance_number, new_seq)
            Dup.existing_DNA.add_name(DnaSequence.instance_number, new_seq.name)
            # print(f"[{DnaSequence.instance_number}] {name}: {sequence}")
            return f"[{DnaSequence.instance_number}] {name}: {sequence}"

        except IndexError:
            print("Not enough arguments in order to dup DNA")
        except ValueError:
            print("The sequence is invalid")
        except Exception as e:
            print("e is:" ,e)