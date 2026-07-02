# Case Study Analysis of Biocon

company = {
    "Company Name": "Biocon",
    "Founder": "Kiran Mazumdar-Shaw",
    "Founded": "1978",
    "Headquarters": "Bengaluru, India",

    "Innovation": [
        "Biosimilars",
        "Insulin Products",
        "Monoclonal Antibodies"
    ],

    "Applications": [
        "Diabetes Treatment",
        "Cancer Therapy",
        "Autoimmune Diseases"
    ],

    "Challenges": [
        "Regulatory Approval",
        "High R&D Costs",
        "Global Competition"
    ],

    "Market Impact": [
        "Affordable Medicines",
        "Global Presence",
        "Advancement in Biotechnology"
    ]
}

print("\nCASE STUDY ANALYSIS: BIOCON\n")

for key, value in company.items():

    print(key + ":")

    if isinstance(value, list):
        for item in value:
            print("-", item)
    else:
        print(value)

    print()