from manipulation.manipulation import Manipulation

class Slice(Manipulation):

    def __init__(self, command):
        try:
            self.new_seq_details=None
            self.seq_to_slice = command[1]
            self.start_index = command[2]
            self.end_index = command[3]
            if ":" in command:
                self.new_seq_details = command[command.index(":") + 1:]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            sequence=self.extract_sequence(self.seq_to_slice)
            seq=sequence.get_seq()[int(self.start_index):int(self.end_index)]
            self.keep_manipulate( self.new_seq_details,sequence, seq, "s")

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
