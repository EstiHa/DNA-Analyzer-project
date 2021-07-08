from dna_sequence import DnaSequence
from existing_DNA import Existing_DNA


class Load:
    existing_DNA=Existing_DNA()

    def perform_action(self, command):
        try:
            if len(command) > 2:
                name = command[2][1:]
            else:
                if "." in command[1]:
                    name = command[1][:command[1].index('.')]
                else:
                    name=command[1]
            if "." in command[1]:
                file_name=command[1]
            else:
                file_name=command[1]+'.rawdna'
            with open(file_name) as file:
                sequence=file.readline()

            new_seq = DnaSequence(sequence, name)
            if len(sequence)>40:
                sequence=sequence[:32]+"..."+sequence[len(sequence)-4:]
            print(f"[{new_seq.id}] {name}: {sequence}")
            Load.existing_DNA.add_new_DNA(new_seq.id, name, sequence)
            return new_seq
        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")