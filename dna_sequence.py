
class DnaSequence:
    def __init__(self, sequence):
        valid=True
        for x in sequence:
            if x not in ["A", "C", "T", "G"]:
                raise TypeError
        self.DNA_seq=sequence

    def insert(self, index, nucleotide):
        if type(index) is not int or index<0 or index>=len(self.DNA_seq):
            raise IndexError
        for x in nucleotide:
            if x not in ["A", "C", "T", "G"]:
                raise TypeError
        self.DNA_seq=self.DNA_seq[:index+1]+nucleotide+self.DNA_seq[index+1:]

    def __str__(self):
        return 'THE DNA sequence is: '+self.DNA_seq

    def __eq__(self, other):
        if type(other)!= DnaSequence:
            return TypeError
        return self.DNA_seq==other.DNA_seq

    def __ne__(self, other):
        if type(other)!= DnaSequence:
            return TypeError
        return self.DNA_seq!=other.DNA_seq

    def __len__(self):
        return len(self.DNA_seq)

    def __getitem__(self, index):
        if type(index) is not int or index<0 or index>=len(self.DNA_seq):
            raise IndexError
        return self.DNA_seq[index]

    def assignment(self, other):
        if type(other) is str:
            self.DNA_seq=other
        elif type(other)==DnaSequence:
            self.DNA_seq=other.DNA_seq
        else:
            raise TypeError



#Tests.....
# dna=DnaSequence("ATG")
# dna1=DnaSequence("AAATG")
# print(len(dna))
# print(dna[2])
# if dna==dna1:
    # print("equal")
# else:
    # print("not equal")

# print(type("aa"))
# print(dna)

# dna.assignment(dna1)
# print(dna)

# dna.assignment("AAA")
# print(dna)

# dna2=DnaSequence("as")
# print(dna2)

# dna.insert(1,"T4")
# print(dna)

# print(type(dna))