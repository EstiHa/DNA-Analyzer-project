from analysis.analysis import Analysis

class Find(Analysis):

    def perform_action(self, command):
        try:
            sequence=self.extract_sequence(command[1])
            seq_to_find=self.get_seq_to_find(command[2])
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

