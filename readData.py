from textwrap import wrap
from collections import Counter
import json

tb = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N',
      'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R', 'CTA': 'L', 'CTC': 'L',
      'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H', 'CAT': 'H', 'CAA': 'Q',
      'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
      'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
      'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F',
      'TTA': 'L', 'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': 'END', 'TAG': 'END', 'TGC': 'C', 'TGT': 'C',
      'TGA': 'END', 'TGG': 'W', }

checkStr=["A", "C", "D","E", "F", "G","H", "I", "K","L", "M", "N","P", "Q", "R","S", "T", "V","W", "Y"]

def check_string(string):
    if len(string)==0:
        return False
    for i in list(string):
        if i not in checkStr:
            return False
    return True


def readData(data):
    ns = wrap(data, 3)
    print(len(ns))

    occ = Counter(ns)

    res = {"A": [], "C": [], "D": [],
           "E": [], "F": [], "G": [],
           "H": [], "I": [], "K": [],
           "L": [], "M": [], "N": [],
           "P": [], "Q": [], "R": [],
           "S": [], "T": [], "V": [],
           "W": [], "Y": [], "END": []}
    for i in occ:
        if (len(i) == 3):
            up = i.upper()
            el = {"codon": i, "i": occ[i]}
            res[tb[up]].append(el)

    for i in res:
        sum = 0
        for e in res[i]:
            sum += int(e["i"])
        for e in res[i]:
            pr = round(float(e["i"] / sum), 2)
            e["i"] = pr

    with open("res.json","w") as jsn:
        jsn.write(json.dumps(res,indent=4))

    return res

def testData(result):


    occ2 = Counter(result)

    res2 = {"A": [], "C": [], "D": [],
            "E": [], "F": [], "G": [],
            "H": [], "I": [], "K": [],
            "L": [], "M": [], "N": [],
            "P": [], "Q": [], "R": [],
            "S": [], "T": [], "V": [],
            "W": [], "Y": [], "END": []}

    for i in occ2:
        if (len(i) == 3):
            up = i.upper()
            el = {"codon": i, "i": occ2[i]}
            res2[tb[up]].append(el)

    for i in res2:
        sum = 0
        for e in res2[i]:
            sum += int(e["i"])
        for e in res2[i]:
            if sum == 0:
                sum = 1
            pr = round(float(e["i"] / sum), 2)
            e["i"] = pr

    return res2