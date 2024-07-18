# Project to practice python 

def is_valid(sequence):
    if sequence == None:
        return False

    for each_nucleotide in sequence:
        if each_nucleotide not in "ATCG":
            return False
    return True

def get_sequence_from_file(filename):
    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()
            print(f"The DNA sequence entered is: {sequence}")
        return sequence
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

def get_sequence_from_user():
    sequence = input("Please enter the DNA sequence: ").upper()
    if is_valid(sequence) == False or sequence == "":
        print("This DNA sequence is invalid")
        return None
    print(f"The DNA sequence entered is: {sequence}")
    return sequence

def nucleotide_count(sequence):
    a_count, t_count, c_count, g_count = 0, 0, 0, 0
    if (is_valid(sequence)):
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

def transcribe_rna(sequence):
    rna = ""
    if (is_valid(sequence)):
        for nucleotide in sequence:
            if (nucleotide == "T"):
                rna += "U"
            else:
                rna += nucleotide
    #  if the sequence entered is always valid no need
    #  else:
    #     print("This DNA sequence is invalid")
    return rna

def transcribe_dna(sequence):
    dna = ""
    if (is_valid(sequence)):
        for nucleotide in sequence:
            if (nucleotide == "U"):
                dna += "T"
            else:
                dna += nucleotide
    #  if the sequence entered is always valid no need
    #  else:
    #     print("This DNA sequence is invalid")
    return dna

def complement(sequence):
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    if (is_valid(sequence)):
        return ''.join(complements[nucleotide] for nucleotide in (sequence))
    #  if the sequence entered is always valid no need
    #  else:
    #     print("This DNA sequence is invalid")

def reverse_complement(sequence):
    return complement(sequence)[::-1]
    #  if the sequence entered is always valid no need
    #  else:
    #     print("This DNA sequence is invalid")

# orf includes start codon but not stop codon
def first_orf(sequence):
    start_codon = "AUG"
    stop_codons = {"UAA", "UGA", "UAG"}
    if not is_valid(sequence):
        return "This DNA sequence is invalid"

    sequence = transcribe_rna(sequence)
    start_index = sequence.find(start_codon)
    if start_index != -1:
        for i in range(start_index, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if codon in stop_codons:
                return sequence[start_index:i]
        return "No stop codon detected"
    else:
        return "No start codon detected"

# presents amino acid that corresponds to the codon in an orf
def codon_to_amino_acid(sequence):
    codon_to_amino_acid = {
        "AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine",
        "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine", "UAC": "Tyrosine",
        "UGU": "Cysteine", "UGC": "Cysteine", "UGG": "Tryptophan", "CUU": "Leucine",
        "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine", "CCU": "Proline",
        "CCC": "Proline", "CCA": "Proline", "CCG": "Proline", "CAU": "Histidine",
        "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine", "CGU": "Arginine",
        "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AUU": "Isoleucine",
        "AUC": "Isoleucine", "AUA": "Isoleucine", "ACU": "Threonine", "ACC": "Threonine",
        "ACA": "Threonine", "ACG": "Threonine", "AAU": "Asparagine", "AAC": "Asparagine",
        "AAA": "Lysine", "AAG": "Lysine", "AGU": "Serine", "AGC": "Serine", "AGA": "Arginine",
        "AGG": "Arginine", "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",
        "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine", "GAU": "Aspartate",
        "GAC": "Aspartate", "GAA": "Glutamate", "GAG": "Glutamate", "GGU": "Glycine", "GGC": "Glycine",
        "GGA": "Glycine", "GGG": "Glycine"
    }

    amino_acids = []
    if not is_valid(sequence):
        return "This DNA sequence is invalid"
        
    orf_sequence = first_orf(sequence)
    if is_valid(transcribe_dna(orf_sequence)):
        for i in range(0, len(orf_sequence) - 2, 3):
            codon = orf_sequence[i:i+3]
            amino_acid = codon_to_amino_acid.get(codon)
            amino_acids.append(amino_acid)
    else:
        return "There is no Open Reading Frame detected."

    return ' '.join(amino_acids)

def test():
    #ACTGTCGACGATCGTAGC
    #ATCHSYCTAGCTATCCTA
    #ATCGTAGCTAGCTSTAC
    #ATATGTACGTCAGATCATGACG

    sequence = get_sequence_from_user()
    #print(is_valid(sequence))
    if (sequence != None):
        nucleotide_count(sequence)
        print(transcribe_rna(sequence))
        print(complement(sequence))
        print(reverse_complement(sequence))
        print(first_orf(sequence))
        print(codon_to_amino_acid(sequence))

if __name__ == "__main__":
    test()
