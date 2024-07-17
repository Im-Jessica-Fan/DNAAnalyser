# Project to practice python 

# Input DNA Sequence:

# Accept a DNA sequence as input from the user.
# Validate DNA Sequence:

# Ensure the input sequence contains only valid nucleotide characters (A, T, C, G).
# Nucleotide Count:

# Count the occurrences of each nucleotide (A, T, C, G) in the sequence.
# Transcription:

# Transcribe the DNA sequence to its corresponding RNA sequence (replacing T with U).
# Reverse Complement:

# Generate the reverse complement of the DNA sequence.
# Find Motifs:

# Search for specific motifs (subsequences) within the DNA sequence.

def is_valid(sequence):
    if sequence == None:
        return False

    for each_nucleotide in sequence:
        if each_nucleotide not in "ATCG":
            return False
    return True

def get_sequence():
    sequence = input("Please enter the DNA sequence: ").upper()
    if is_valid(sequence) == False or sequence == "":
        print("This DNA sequence is invalid")
        return None
    print(f"The DNA sequence entered is: {sequence}")
    return sequence

def nucleotide_count(sequence):
    a_count, t_count, c_count, g_count = 0, 0, 0, 0
    if (is_valid(sequence) == True):
        for nucleotide in sequence:
            if nucleotide == "A": 
                a_count += 1
            if nucleotide == "T":
                t_count += 1
            if nucleotide == "C":
                c_count += 1
            if nucleotide == "G":
                g_count += 1
        print(f"Number of A: {a_count}\nNumber of T: {t_count}\nNumber of C: {c_count}\nNumber of G: {g_count}")
    #  if the sequence entered is always valid no need
    #  else:
    #     print("This DNA sequence is invalid")

def test():
    #ACTGTCGACGATCGTAGC
    #ATCHSYCTAGCTATCCTA
    #ATCGTAGCTAGCTSTAC

    sequence = get_sequence()
    #print(is_valid(sequence))
    if (sequence != None):
        nucleotide_count(sequence)

if __name__ == "__main__":
    test()
