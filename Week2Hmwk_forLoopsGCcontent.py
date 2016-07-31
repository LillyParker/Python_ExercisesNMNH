seq_file = open("seqs.fasta")

for line in seq_file.readlines()
    print(line)
seq_file.close()