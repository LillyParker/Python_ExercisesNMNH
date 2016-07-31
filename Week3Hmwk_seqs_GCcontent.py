seq_file = open("seqs.fasta") #read in the seqs.fasta file
GClist = [] #make an empty list for the GC contents of each sequence or line

for line in seq_file.readlines():
    newline = line.strip("\n")   
    if newline[0] != ">":
        line_length = len(newline)
        GCcount=0
        GCcontent=0
        for nucleotide in newline:
            if nucleotide == "C" or nucleotide=="G":
                GCcount = GCcount + 1
        GCcontent = (GCcount/line_length)
        GClist.append(GCcontent)
        
print("The maximum GC content is",round(max(GClist),2))

seq_file.close()




