from DNA.existing_DNA import Existing_DNA
from analysis.analysis import Analysis


class Len(Analysis):
    def __init__(self, command):
        try:
            self.seq_id=command[1]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            sequence= Analysis.existing_DNA.get_DNAs(int(self.seq_id[1:]))
            return len(sequence.get_seq())
        except IndexError:
            print("Not enough arguments in order to delete DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")