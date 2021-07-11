from DNA.existing_DNA import Existing_DNA
from manipulation.manipulation import Manipulation

class Replace(Manipulation):
    existing_DNA=Existing_DNA()

    def perform_action(self, command):
        try:
            if ":" in command:
                command1 = command[2:command.index(":")]
            else:
                command1=command[2:]
            sequence = self.extract_sequence(command[1])
            seq = sequence.get_seq()
            # if len(command)<2:
            #     pass
            # else:
            seq=list(seq)
            for i in range(len(command1)//2):
                seq[int(command1[i*2])]=command1[i*2+1]
            seq="".join(seq)
            return self.keep_manipulate(command, sequence, seq, "r")

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
