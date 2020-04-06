"""Library of functions for genome analysis."""


def translateCodonToAmino(codon):
    """Translate a DNA codon to it's Amino acid using the RNA codon table."""
    rna_codon_table = {
        ('GCT', 'GCC', 'GCA', 'GCG'): 'A'
    }
    return rna_codon_table[codon]


def translateDnaToPeptides(dna):
    """Translate the entire DNA sequence to polypeptide sequences."""
    # 3 reading frames
    polypeptide_dict = {[], [], []}
    start_recording = 0
    polypeptide = ''
    for n_rd_frm in range(3):
        for i in range(n_rd_frm, len(dna)-2, 3):
            codon = dna[i:i+3]
            pp = translateCodonToAmino(codon)
            if (start_recording):
                polypeptide = polypeptide+pp
            if (pp == 'START'):
                start_recording = 1
            if (pp == 'STOP'):
                start_recording = 0
                polypeptide_dict[n_rd_frm].append(polypeptide)
                polypeptide = ''

    return polypeptide_dict
