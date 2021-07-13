import json
from batch.batch import Batch


class BatchSave(Batch):
    def __init__(self, command):
        super().__init__()
        self.batch_name = command[1][1:]
        if len(command)>2:
            self.file=command[2]
        else:
            self.file='.dnabatch'

    def perform_action(self):
        try:
            with open(self.file,'w') as file:
                for command in Batch.batches_dict[self.batch_name].get_commands().queue:
                    file.write(command+'\n')
        except Exception as e:
            print(e)