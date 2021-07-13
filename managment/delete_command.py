from DNA.existing_DNA import Existing_DNA
from managment.management import Management


class Delete(Management):
    existing_DNA=Existing_DNA()

    def __init__(self, command):
        try:
            self.seq_to_be_deleted = command[1]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            sequence = self.extract_sequence(self.seq_to_be_deleted )
            print(f"Do you really want to delete {sequence.get_name()}: {sequence.get_seq()}?\nPlease confirm by 'y' or 'Y', or cancel by 'n' or 'N'.\n> confirm >>>", end=" ")
            confirm=input()
            while confirm not in ["y","Y","n","N"]:
                print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.\n> confirm >>>", end=" ")
                confirm=input()
            if confirm in ["n","N"]:
                print("Delete is canceled")
            else:
                Management.existing_DNA.remove_seq(sequence.get_id(), sequence.get_name())
                return f"Deleted: [{sequence.get_id()}] {sequence.get_name()}: {sequence.get_seq()}"

        except IndexError:
            print("Not enough arguments in order to delete DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
