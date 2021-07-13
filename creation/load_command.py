from DNA.dna_sequence import DnaSequence
from DNA.existing_DNA import Existing_DNA


class Load:
    existing_DNA=Existing_DNA()

    def __init__(self, command):
        try:
            self.new_seq_name = None
            self.file_name = command[1]
            if len(command) > 2:
                self.new_seq_name = command[2]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            if self.new_seq_name != None:
                name = self.new_seq_name[1:]
            else:
                if "." in  self.file_name:
                    name =  self.file_name[: self.file_name.index('.')]
                else:
                    name= self.file_name
            if "." in self.file_name:
                file_name= self.file_name
            else:
                file_name= self.file_name+'.rawdna'

            with open(file_name) as file:
                sequence=file.readline()
            new_seq = DnaSequence(sequence, name)
            if len(sequence)>40:
                sequence=sequence[:32]+"..."+sequence[len(sequence)-4:]
                print(sequence)
            Load.existing_DNA.add_new_DNA(new_seq.id, new_seq)
            Load.existing_DNA.add_name(new_seq.id, new_seq.name)
            return f"[{new_seq.id}] {name}: {sequence}"


        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")