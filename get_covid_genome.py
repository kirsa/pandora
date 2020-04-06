"""Download Corona virus genomes from NCBI."""

import json

import requests
import yaml
from Bio import Entrez


def getCorSeq():
    """Get Corona virus sequences from NCBI."""

    # ncov sequence url
    ncov_url = "https://www.ncbi.nlm.nih.gov/core/assets/genbank/files/ncov-sequences.yaml"
    genbank_yaml = yaml.load(requests.get(ncov_url).text)

    # Get everything under genbank-sequences
    genbank_yaml = genbank_yaml['genbank-sequences']
    assert(len(genbank_yaml) > 0), "ERROR : Corona yaml not downloaded"
    print('Downloaded %d sequences' % len(genbank_yaml))
    # Dict of all sequences
    cor_seq_dict = {}
    for entry in genbank_yaml:
        if 'gene-region' in entry and entry['gene-region'] == 'complete':
            genbank_id = entry['accession']
            print("Downloading sequence id: ", genbank_id)
            dna_seq = Entrez.efetch(
                db='nucleotide', id=genbank_id, rettype='fasta',
                retmode='text').read().split('\n')[1:]
            cor_seq_dict[genbank_id] = ''.join(dna_seq)
    assert(len(cor_seq_dict) > 0), "ERROR : No Completed Corona sequences"
    print("Completed CORONA seqs downloaded")
    return cor_seq_dict


def createJson(cor_seq_dict):
    """Create JSON file."""
    with open('covid_data/all_corona_seq.json', 'w') as f:
        json.dump(cor_seq_dict, f)
    print("all_corona_seq.json FILE CREATED")


if __name__ == '__main__':
    createJson(getCorSeq())
