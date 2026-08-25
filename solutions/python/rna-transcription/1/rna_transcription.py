"""
RNA transcription utilities.

This module contains a function for converting a DNA strand
into its complementary RNA strand.
"""
def to_rna(dna_strand):
    """
Convert a DNA strand into its complementary RNA strand.

Each DNA nucleotide is replaced with its RNA complement:
G -> C, C -> G, T -> A, A -> U.

Args:
dna_strand (str): DNA sequence to transcribe.

Returns:
str: Complementary RNA sequence.
    """
    dna_nucleotides = ["G", "C", "T", "A"]
    rna_nucleotides = ["C", "G", "A", "U"]

    rna = ""
    
    for nucleotide in dna_strand: 
        searching_index = dna_nucleotides.index(nucleotide)
        rna += rna_nucleotides[searching_index] 
    return rna