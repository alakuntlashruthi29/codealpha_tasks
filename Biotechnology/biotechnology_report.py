# Research Report on Recent Advancements in Medical Biotechnology

report = {
    "Topic": "Medical Biotechnology",

    "Recent Advancements": [
        "mRNA Vaccines",
        "CRISPR Gene Editing",
        "Stem Cell Therapy",
        "AI-based Diagnostics",
        "Personalized Medicine"
    ],

    "Applications": [
        "Disease Prevention",
        "Cancer Treatment",
        "Genetic Disorder Therapy",
        "Early Disease Detection"
    ],

    "Advantages": [
        "Improved Healthcare",
        "High Precision Treatments",
        "Reduced Side Effects",
        "Rapid Vaccine Development"
    ]
}

print("\nRECENT ADVANCEMENTS IN MEDICAL BIOTECHNOLOGY\n")

for key, value in report.items():
    print(key + ":")

    if isinstance(value, list):
        for item in value:
            print("-", item)
    else:
        print(value)

    print()