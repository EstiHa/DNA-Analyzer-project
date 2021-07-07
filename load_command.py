from dna_sequence import DnaSequence


class Load:
    def perform_action(self, command):
        try:
            if len(command) > 2:
                name = command[2][1:]
            else:
                name = command[1][:len(command[1])-7]

            print(name)
            with open(command[1]) as file:
                print("hi", command[1])
                sequence=file.readline()
                print(sequence)
            print("seq" ,sequence)
            new_seq = DnaSequence(sequence, name)
            print(f"[{new_seq.id}] {name}: {sequence}")
            return new_seq
        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
