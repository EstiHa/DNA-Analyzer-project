from batch.batch import Batch


class BatchList(Batch):
    def __init__(self, command):
        super().__init__()

    def perform_action(self):
        for key in Batch.batches_dict.keys():
            print(key)