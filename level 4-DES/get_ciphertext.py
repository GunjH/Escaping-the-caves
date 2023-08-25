import re

#mark whenever this line appears and the next line contains required output

pattern = re.compile("Slowly, a new text starts appearing on the screen. It reads ...")
flagged = False

f = open("ciphertext01.txt", "w")

for line in open("outputs_log1.log"):
    if flagged:
        flagged = False
        f.write("{}\n".format(line.strip()))
    else:
        for match in re.finditer(pattern, line):
            if match:
                flagged = True

f.close()

f = open("ciphertext02.txt", "w")

for line in open("outputs_log2.log"):
    if flagged:
        flagged = False
        f.write("{}\n".format(line.strip()))
    else:
        for match in re.finditer(pattern, line):
            if match:
                flagged = True

f.close()