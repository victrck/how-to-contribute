

geneticCode = {
'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L',
'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST',
'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W',
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}

entrada = "GGC.CGA.UUA.AUG.CUU.AAA.UGC.GGC.CUA.AAU.UAU"

aminoacido = ""
codons = entrada.split('.')
start = False

for codon in codons:
    if start == False:
        if codon == 'AUG':
            aminoacido += geneticCode[codon]
            start = True
    elif (codon == 'UAA') and (codon == 'UAG') and (codon == 'UGA'):
        break   
    else:
        aminoacido += geneticCode[codon]

print("INPUT: RNAm - ", entrada)
print("OUTPUT: Cadeia de Aminoacido - ", aminoacido)