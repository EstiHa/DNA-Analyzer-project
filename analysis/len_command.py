from DNA.existing_DNA import Existing_DNA
from analysis.analysis import Analysis


class Len(Analysis):

    def perform_action(self, command):
        try:
            sequence= Analysis.existing_DNA.get_DNAs(int(command[1][1:]))
            return len(sequence.get_seq())
        except IndexError:
            print("Not enough arguments in order to delete DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")