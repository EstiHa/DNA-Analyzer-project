from cffi.backend_ctypes import xrange

from analysis.analysis import Analysis

class FindAll(Analysis):

    def perform_action(self, command):
        try:
            sequence = self.extract_sequence(command[1]).get_seq()
            seq_to_find = self.get_seq_to_find(command[2])
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
