"""protein_to_daltons.py"""

# Hard-coded protein sequence
PROTEIN_SEQUENCE = """MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC
CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH
KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ
KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ
EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK
GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM
EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE
NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY
PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF
DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV"""

# Removing newline characters if any
PROTEIN_SEQUENCE = PROTEIN_SEQUENCE.replace('\r', '').replace('\n', '')

# Constants
AVERAGE_MOLECULAR_WEIGHT_PER_AA = 110  # in Daltons

# Calculating the molecular weight
MOLECULAR_WEIGHT = len(PROTEIN_SEQUENCE) * AVERAGE_MOLECULAR_WEIGHT_PER_AA

# Converting to kilodaltons
MOLECULAR_WEIGHT_KDA = MOLECULAR_WEIGHT / 1000

print("\nThe length of 'Protein kinase C beta type' is:", len(PROTEIN_SEQUENCE))
print("The average weight of this protein sequence in kilodaltons is:",
      round(MOLECULAR_WEIGHT_KDA, 2))
