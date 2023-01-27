# validity of a string of parantheses
def check(sequence):
    for i in range(0,4):
        if "()" in sequence:
            sequence = sequence.replace("()" , "")
        elif "{}" in sequence:
            sequence = sequence.replace("{}" , "")
        elif "[]" in sequence:
            sequence = sequence.replace("[]" , "")
        else:
            return not sequence
def main():
    seq = "{{}{["
    print(f"if the set of parnatheses is correct? - {check(seq)}")
    seq2 = "(){}[]"
    print(f"if the set of parnatheses is correct? - {check(seq2)}")
main()
