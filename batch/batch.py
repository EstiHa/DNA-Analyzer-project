from queue import Queue

#Batch is a kind of structure that holds a few commands (that didn't ever run)
class Batch:
    batches_dict={}

    def __init__(self):
        self.commands_queue = Queue()

    def add_command(self, command):
        self.commands_queue.put(command)

    def get_commands(self):
        return self.commands_queue

    def run_command(self):
        return self.commands_queue.get()