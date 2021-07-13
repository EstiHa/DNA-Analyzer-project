from DNA.existing_DNA import Existing_DNA
from manipulation.manipulation import Manipulation

class Replace(Manipulation):
    existing_DNA=Existing_DNA()

    def __init__(self, command):
        try:
            self.new_seq_details=None
            self.seq_to_be_replaced = command[1]
            if ":" in command:
                self.replacement = command[2:command.index(":")]
                self.new_seq_details=command[command.index(":")+1:]
            else:
                self.replacement=command[2:]
        except IndexError:
            print("Not enough arguments")

    def perform_action(self):
        try:
            sequence = self.extract_sequence(self.seq_to_be_replaced)
            seq = sequence.get_seq()
            seq=list(seq)
            for i in range(len(self.replacement)//2):
                seq[int(self.replacement[i*2])]=self.replacement[i*2+1]
            seq="".join(seq)
            return self.keep_manipulate(self.new_seq_details, sequence, seq, "r")

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
