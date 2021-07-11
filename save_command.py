from existing_DNA import Existing_DNA
from management import Management

class Save(Management):
    existing_DNA = Existing_DNA()

    def perform_action(self, command):
        try:
            sequence = self.extract_sequence(command[1])
            if len(command)<3:
                file_name=sequence.get_name()+'.rawdna'
            else:
                file_name=command[2]
            with open(file_name, 'w') as file:
                file.write(f'[{sequence.get_id()}] {sequence.get_name()}: {sequence.get_seq()}\n')
                print(f"saved {sequence.get_name()} DNA sequence successfully.")

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
