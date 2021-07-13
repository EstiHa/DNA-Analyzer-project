from analysis.analysis import Analysis

class Find(Analysis):

    def __init__(self, command):
        try:
            self.seq_to_find_in=command[1]
            self.seq_to_be_found=command[2]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            sequence=self.extract_sequence(self.seq_to_find_in)
            seq_to_find=self.get_seq_to_find(self.seq_to_be_found)
            index=sequence.get_seq().find(seq_to_find)
            if index==-1:
                return "The sequence was not found"
            return index+1

        except IndexError:
            print("Not enough arguments in order to delete DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")

