from cffi.backend_ctypes import xrange

from analysis.analysis import Analysis

class FindAll(Analysis):
    def __init__(self, command):
        try:
            self.seq_to_find_in = command[1]
            self.seq_to_be_found = command[2]
        except IndexError:
            print("Not enough arguments")


    def perform_action(self):
        try:
            sequence = self.extract_sequence(self.seq_to_find_in).get_seq()
            seq_to_find = self.get_seq_to_find(self.seq_to_be_found)
            indices=""
            for n in xrange(len(sequence)):
                if sequence.find(seq_to_find, n)==n:
                    indices+=f' {n+1}'
            return indices

        except IndexError:
            print("Not enough arguments in order to delete DNA")
        except ValueError:
            print("The sequence is invalid")
        except:
            print("Error")
