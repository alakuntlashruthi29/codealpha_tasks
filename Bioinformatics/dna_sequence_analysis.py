from Bio.Blast import NCBIWWW, NCBIXML

# Example DNA sequence
sequence = """
ATGCGTACGTAGCTAGCTAGCTAGCGTAGCTAGCTAGCGTACGTAGCTAGCTAG
"""

print("Performing BLAST search...")
result_handle = NCBIWWW.qblast("blastn", "nt", sequence)

# Save BLAST results
with open("blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()

# Read BLAST results
with open("blast_result.xml") as result_file:
    blast_records = NCBIXML.parse(result_file)

    for record in blast_records:
        print("\nTop Matches:")
        for alignment in record.alignments[:5]:
            for hsp in alignment.hsps:
                print("Sequence:", alignment.title)
                print("Length:", alignment.length)
                print("Score:", hsp.score)
                print("Identity:", hsp.identities)
                print("-" * 50)