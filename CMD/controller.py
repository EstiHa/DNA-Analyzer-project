from analysis.count_command import Count
from analysis.find_all_command import FindAll
from analysis.len_command import Len
from analysis.find_command import Find
from batch.batch import Batch
from batch.batchlist_command import BatchList
from batch.batchload_command import BatchLoad
from batch.batchsave_command import BatchSave
from batch.batchshow_command import BatchShow
from managment.delete_command import Delete
from creation.dup_command import Dup
from creation.load_command import Load
from creation.new_command import New
from manipulation.replace_command import Replace
from managment.save_command import Save
from manipulation.slice_command import Slice


class Controller:

    def __init__(self):
        self.commands= {
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
            "findall": FindAll,
            "batchlist": BatchList,
            "batchshow": BatchShow,
            "batchsave": BatchSave,
            "batchload": BatchLoad
        }
        self.mode="cmd"
        self.current_batch=None

    def run_command(self, command):
        try:
            cmd = self.commands[command[0]](command)
            req = cmd.perform_action()
            if req != None:
                print(req)
        except KeyError:
            print("Command not found")

    def handle_command(self, command):
        splited_command = command.split()
        if splited_command[0]=="batch":
            self.current_batch=Batch()
            Batch.batches_dict[splited_command[1]]=self.current_batch
            self.mode="batch"
            return
        if splited_command[0] == "end":
            self.mode = "cmd"
            return
        if splited_command[0] == 'run':
            while not Batch.batches_dict[splited_command[1][1:]].get_commands().empty():
                self.run_command(Batch.batches_dict[splited_command[1][1:]].get_commands().get())
            Batch.batches_dict.pop(splited_command[1][1:])
            return
        if self.mode == 'cmd':
            self.run_command(splited_command)
        else:
            self.current_batch.add_command(command)


