
class DnaSequence:

    valid_nucleotide="ACTG"
    instance_number=0

    def __init__(self, sequence, name):
        if any(x not in DnaSequence.valid_nucleotide for x in sequence):
            raise ValueError
        self.DNA_seq=sequence
        self.id=DnaSequence.instance_number+1
        DnaSequence.instance_number+=1
        self.name=name


    def insert(self, index, nucleotide):
        if type(index) is not int or index<0 or index>=len(self.DNA_seq):
            raise IndexError
        if any(x not in DnaSequence.valid_nucleotide for x in nucleotide):
            raise ValueError
        self.DNA_seq=self.DNA_seq[:index+1]+nucleotide+self.DNA_seq[index+1:]

    def __str__(self):
        return 'The DNA sequence is: '+self.DNA_seq

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

    def __setitem__(self, key, value):
        if type(key) is not int or key<0 or key>=len(self.DNA_seq):
            raise IndexError
        if any(x not in DnaSequence.valid_nucleotide for x in value):
            raise ValueError
        self.DNA_seq=self.DNA_seq[:key]+value+self.DNA_seq[key+1:]

    def get_seq(self):
        return self.DNA_seq

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def assignment(self, other):
        if type(other) is str:
            if any(x not in DnaSequence.valid_nucleotide for x in other):
                raise TypeError
            self.DNA_seq=other
        elif type(other)==DnaSequence:
            self.DNA_seq=other.DNA_seq
        else:
            raise TypeError


#Tests.....
# dna=DnaSequence("ATG")
# dna[1]="A"
# print(dna)

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