from batch.batch import Batch


class BatchLoad(Batch):
    def __init__(self, command):
        super().__init__()
        self.file= command[1]
        if len(command)>2:
            self.new_batch_name=command[2]
        else:
            self.new_batch_name=command[:command[1].find('.')]

    def perform_action(self):
        try:
            batch=Batch()
            with open(self.file) as file:
                for line in file:
                    batch.add_command(line.rstrip().split())
                Batch.batches_dict[self.new_batch_name]=batch
        except Exception as e:
            print(e)