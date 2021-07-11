from manipulation import Manipulation

class Slice(Manipulation):
    def perform_action(self, command):
        try:
            sequence=self.extract_sequence(command[1])
            seq=sequence.get_seq()[int(command[2]):int(command[3])]
            self.keep_manipulate( command,sequence, seq, "s")

        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
