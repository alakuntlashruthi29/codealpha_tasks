# Comparative Study of NCBI, UniProt, and PDB

databases = {
    "NCBI": {
        "Primary Data": "DNA and Protein Sequences",
        "Maintained By": "NIH",
        "Main Application": "Genomics",
        "Search Tool": "BLAST"
    },

    "UniProt": {
        "Primary Data": "Protein Sequences",
        "Maintained By": "UniProt Consortium",
        "Main Application": "Proteomics",
        "Search Tool": "Protein Search"
    },

    "PDB": {
        "Primary Data": "3D Structures",
        "Maintained By": "Worldwide PDB",
        "Main Application": "Structural Biology",
        "Search Tool": "Structure Search"
    }
}

print("\nCOMPARATIVE STUDY OF NCBI, UniProt, AND PDB\n")

for name, details in databases.items():
    print("=" * 40)
    print("Database:", name)

    for key, value in details.items():
        print(f"{key}: {value}")

    print()