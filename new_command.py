from dna_sequence import DnaSequence
from existing_DNA import Existing_DNA

class New:
    instance_number=1
    existing_DNA=Existing_DNA()

    def perform_action(self, command):
        try:
            if len(command)>2:
               name= command[2][1:]
            else:
                name = f'seq{self.instance_number}'
                New.instance_number += 1
            new_seq=DnaSequence(command[1],name)
            print(f"[{new_seq.id}] {name}: {command[1]}")
            New.existing_DNA.add_new_DNA(new_seq.id, new_seq)
            New.existing_DNA.add_name(new_seq.id, new_seq.name)

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
