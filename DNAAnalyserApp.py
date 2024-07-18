from DNAAnalyser import *

def main():
    # Below is a sample sequence used in DNASequence.txt for option 1 and can be copied and pasted for option 2
    # ATCGGCTATGCTTACGATCGTAGCTGATCGTAGCTAGCTGATCGTACGAGCTAGCTAGTACGATC

    print("To analyse a DNA sequence, either insert a file or enter in a DNA sequence.")
    print("To insert a file with a DNA sequence, enter 1.\nTo enter in a DNA sequence, enter 2")
    while True:
        option_chosen = input("\nPlease choose either 1 or 2. (Enter 0 to Quit): ")
        if option_chosen == "1":
            filename = input("Please enter the name of the file: ")
            sequence = get_sequence_from_file(filename)
        elif option_chosen == "2":
            sequence = get_sequence_from_user()
        elif option_chosen == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        if sequence:
            while True:
                print("\nWhat would you like to do next?\n1 - Display the DNA sequence\n2 - Get nucleotide count\n3 - Transcribe the DNA sequence to RNA\n4 - Get complement strand")
                print("5 - Get reverse complement strand\n6 - Find the first Open Reading Frame\n7 - Translate the first Open Reading Frame into amino acids")
                print("0 - Quit")
                option_chosen = input("Please choose an action. (Enter 0 to Quit): ")
                if option_chosen == "1":
                    # Sample sequence output should be ATCGGCTATGCTTACGATCGTAGCTGATCGTAGCTAGCTGATCGTACGAGCTAGCTAGTACGATC
                    print("\n" + sequence)
                elif option_chosen == "2":
                    # Sample sequence output should be A: 15, T: 18, C: 15, G: 17 
                    print("")
                    nucleotide_count(sequence)
                elif option_chosen == "3":
                    # Sample sequence output should be AUCGGCUAUGCUUACGAUCGUAGCUGAUCGUAGCUAGCUGAUCGUACGAGCUAGCUAGUACGAUC
                    print("\n" + transcribe_rna(sequence))
                elif option_chosen == "4":
                    # Sample sequence output should be TAGCCGATACGAATGCTAGCATCGACTAGCATCGATCGACTAGCATGCTCGATCGATCATGCTAG
                    print("\n" + complement(sequence))
                elif option_chosen == "5":
                    # Sample sequence output should be GATCGTACTAGCTAGCTCGTACGATCAGCTAGCTACGATCAGCTACGATCGTAAGCATAGCCGAT
                    print("\n" + reverse_complement(sequence))
                elif option_chosen == "6":
                    # Sample sequence output should be AUGCUUACGAUCGUAGCUGAUCGUAGC
                    print("\n" + first_orf(sequence))
                elif option_chosen == "7":
                    # Sample sequence output should be Methionine Leucine Threonine Isoleucine Valine Alanine Aspartate Arginine Serine
                    print("\n" + codon_to_amino_acid(sequence))
                elif option_chosen == "0":
                    print("\nGoodbye!")
                    break
                else:
                    print("Invalid choice.")
                    continue
    
main()