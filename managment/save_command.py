from DNA.existing_DNA import Existing_DNA
from managment.management import Management

class Save(Management):
    existing_DNA = Existing_DNA()

    def __init__(self, command):
        try:
            self.file_name = None
            self.seq_to_be_saved = command[1]
            if len(command) > 2:
                self.file_name= command[2]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            sequence = self.extract_sequence(self.seq_to_be_saved)
            if self.file_name != None:
                file_name=sequence.get_name()+'.rawdna'
            else:
                file_name=self.file_name
            with open(file_name, 'w') as file:
                file.write(f'[{sequence.get_id()}] {sequence.get_name()}: {sequence.get_seq()}\n')
                return f"saved {sequence.get_name()} DNA sequence successfully."

        except IndexError:
            print("Not enough arguments for saving DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
