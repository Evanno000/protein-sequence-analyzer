#Protein sequence analyzer

protein = "ACDEFGHIKLMNPQRSTVWY"

amino_acids =  "ACDEFGHIKLMNPQRSTVWY"

#Convert sequence to uppercace
protein = protein.upper()

#Checking whether the sequence is valid
if not protein or any(aa not in amino_acids for aa in protein):
    print("Invalid protein sequence")

else:
    length = len(protein)

    print("PROTEIN SEQUENCE ANALYSIS")
    print("-------------------------")
    print("Protein:", protein)
    print("Length:", length, "Amino Acids",)

print("\nAmino Acid Composition:")
for aa in amino_acids:
    count = protein.count(aa)
    if count > 0:
       percentage = (count / length) * 100
       print(f"{aa}: {count} ({percentage:.2f}%)")