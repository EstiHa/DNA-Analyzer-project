class Existing_DNA:
    __instance=None
    __existing_DNAs = {}

    def __new__(cls, *args, **kwargs):
        if not Existing_DNA.__instance:
            Existing_DNA.__instance = object.__new__(cls)
        return Existing_DNA.__instance

    def get_DNAs(self, key=None):
        if key==None:
            return Existing_DNA.__existing_DNAs
        return Existing_DNA.__existing_DNAs[key]

    def add_new_DNA(self, key, name, seq):
        Existing_DNA.__existing_DNAs[key]=(name, seq)
