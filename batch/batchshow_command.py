from batch.batch import Batch


class BatchShow(Batch):
    def __init__(self, command):
        super().__init__()
        self.batch_name=command[1][1:]

    def perform_action(self):
        for command in Batch.batches_dict[self.batch_name].get_commands().queue:
            print(command)