DNA = ''
RNA = ''
protein = ''
base=['U','C','A','G']
codon = []

for i in base:
    for j in base:
        for k in base:
            codon.append(i+j+k)
            
amino='~~!!%%%%(())<<>?!!!!^^^^--__????@@@#&&&&++==[[]]$$$$****{{}}\\\\\\\\'

DNA = input('input DNA : ')

for c in DNA:
    if( c == 'A'):
        RNA = RNA + 'U'
    elif( c == 'T'):
        RNA = RNA + 'A'
    elif( c == 'G'):
        RNA = RNA + 'C'
    elif( c == 'C'):
        RNA = RNA + 'G'
        
print('RNA : %s' %RNA)

for i in range(0,len(RNA),3):
    for code in codon:
        if( RNA[i:i+3] == code):
            j = codon.index(code)
            break
    protein = protein + amino[j]
    
print('protein : %s' %protein)