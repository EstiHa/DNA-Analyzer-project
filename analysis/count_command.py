from analysis.analysis import Analysis


class Count(Analysis):

    def perform_action(self, command):
        try:
            sequence = self.extract_sequence(command[1]).get_seq()
            seq_to_find = self.get_seq_to_find(command[2])
            counter=sequence.count(seq_to_find)
            return counter

        except IndexError:
            print("Not enough arguments in order to delete DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
