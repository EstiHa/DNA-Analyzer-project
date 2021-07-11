class Existing_DNA:
    __instance=None
    __existing_DNAs = {}
    __DNA_names={}

    def __new__(cls, *args, **kwargs):
        if not Existing_DNA.__instance:
            Existing_DNA.__instance = object.__new__(cls)
        return Existing_DNA.__instance

    def get_DNAs(self, key=None):
        if key==None:
            return Existing_DNA.__existing_DNAs
        return Existing_DNA.__existing_DNAs[key]

    def add_new_DNA(self, key, seq_object):
        Existing_DNA.__existing_DNAs[key]=seq_object

    def get_names(self, key=None):
        if key==None:
            return Existing_DNA.__DNA_names
        return Existing_DNA.__DNA_names[key]

    def add_name(self, id, name):
        Existing_DNA.__DNA_names[name]=id

    def remove_seq(self, id, name):
        Existing_DNA.__existing_DNAs.pop(id)
        Existing_DNA.__DNA_names.pop(name)