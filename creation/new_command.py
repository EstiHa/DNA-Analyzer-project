from DNA.dna_sequence import DnaSequence
from DNA.existing_DNA import Existing_DNA


#The class creates a new DNA sequence
class New:
    instance_number=1
    existing_DNA=Existing_DNA()

    def __init__(self, command):
        try:
            self.new_seq_name = None
            self.sequence = command[1]
            if len(command) > 2:
                self.new_seq_name = command[2]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            if self.new_seq_name != None:   #Creates the name of the new sequence
               name= self.new_seq_name[1:]
            else:
                name = f'seq{self.instance_number}'
                New.instance_number += 1
            new_seq=DnaSequence(self.sequence,name) #Creates a new DNA object
            New.existing_DNA.add_new_DNA(new_seq.id, new_seq) #Add
            New.existing_DNA.add_name(new_seq.id, new_seq.name)
            return f"[{new_seq.id}] {name}: {self.sequence}"

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
