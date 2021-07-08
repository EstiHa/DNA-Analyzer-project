from dna_sequence import DnaSequence
from existing_DNA import Existing_DNA

class Dup:
    existing_DNA=Existing_DNA()

    def perform_action(self, command):
        try:
            # if command[1][0]=='#':
            #     seq_to_dup=Dup.existing_DNA.get_DNAs(int(command[1][1:]))
            if len(command)>2:
                name= command[2][1:]
            else:

                if command[1][0]=='#':
                    i=1
                    seq_to_dup = Dup.existing_DNA.get_DNAs(int(command[1][1:]))
                    name = f'{seq_to_dup[0]}_{i}'
                    while True:
                        name1=name
                        for n in Dup.existing_DNA.get_DNAs().values():
                            name=name1
                            if name==n[0]:
                                i+=1
                                name=f'{seq_to_dup[0]}_{i}'
                        if name==name1:
                            break
                else:
                    i=1
                    name = f'{command[1][1:]}_{i}'
                    while True:
                        name1=name
                        for n in Dup.existing_DNA.get_DNAs().values():
                            if name==n[0]:
                                i+=1
                                name=f'{command[1][1:]}_{i}'
                        if name==name1:
                            break
            sequence=''
            if command[1][0]=='#':
                for key in Dup.existing_DNA.get_DNAs().keys():
                    if int(command[1][1:])==key:
                        sequence=Dup.existing_DNA.get_DNAs(key)[1]
            else:
                for val in Dup.existing_DNA.get_DNAs().values():
                    if command[1][1:] == val[0]:
                        sequence = val[1]

            DnaSequence(sequence,name)
            Dup.existing_DNA.add_new_DNA(DnaSequence.instance_number, name, sequence)
            print(f"[{DnaSequence.instance_number}] {name}: {sequence}")

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except Exception as e:
            print("e is:" ,e)