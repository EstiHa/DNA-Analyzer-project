from analysis.count_command import Count
from analysis.find_all_command import FindAll
from analysis.len_command import Len
from analysis.find_command import Find
from managment.delete_command import Delete
from creation.dup_command import Dup
from creation.load_command import Load
from creation.new_command import New
from manipulation.replace_command import Replace
from managment.save_command import Save
from manipulation.slice_command import Slice


class Controller:

    def __init__(self):
        self.existing_DNAs={}

    def handle_command(self, command):
        command = command.split()
        commands = {
            "new": New,
            "load": Load,
            "dup": Dup,
            "slice": Slice,
            "replace": Replace,
            "del": Delete,
            "save": Save,
            "len": Len,
            "find": Find,
            "count": Count,
            "findall": FindAll
        }
        cmd = commands[command[0]]()
        req= cmd.perform_action(command)
        print(req)