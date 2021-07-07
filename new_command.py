from dna_sequence import DnaSequence
from existing_DNA import existing_DNAs

class New:
    instance_number=1

    def perform_action(self, command):
        try:
            if len(command)>2:
               name= command[2][1:]
            else:
                name = f'seq{self.instance_number}'
                New.instance_number += 1
            new_seq=DnaSequence(command[1],name)
            print(f"[{new_seq.id}] {name}: {command[1]}")
            existing_DNAs[id]=(name, command[1])
            # return new_seq
        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
