from existing_DNA import existing_DNAs


class Dup:
    def perform_command(self, command):
        try:
            if len(command)>2:
               name= command[2][1:]
            else:
                i=1
                name = f'{command[1]}_{i}'
                while True:
                    name1=''
                    for n in existing_DNAs['id'][0]:
                        if name==n:
                            i+=1
                            name1=f'{command[1]}_{i}'
                    if name==name1:
                        break
                    name=name1
            # DnaSequence(command[1],name)
            print(f"[{new_seq.id}] {name}: {command[1]}")
            return new_seq
        except IndexError:
            print("Not enough arguments for creating DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")