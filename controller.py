from dna_sequence import DnaSequence
from dup_command import Dup
from load_command import Load
from new_command import New


class Controller:

    def __init__(self):
        self.existing_DNAs={}

    def handle_command(self, command):
        # handler=CommandHandler(command)
        # handler.execute()
        command = command.split()
        commands = {
            "new": New,
            "load": Load,
            "dup": Dup
        }
        cmd = commands[command[0]]()
        req= cmd.perform_action(command)
        # if type(req) is DnaSequence:
        #     self.existing_DNAs[req.id]=(req.name, req.DNA_seq)
