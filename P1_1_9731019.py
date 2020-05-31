f = open("DFA_input_1.txt", "r")
lines = []
# at first, we read the dfa from the text file
while True:
    line = f.readline()
    if line == '':
        break
    lines.append(line)
print(* lines)
n = len(lines[0].split())
# print(n)
dfa = {}
i = 4
# implementing the dfa wih dictionary to dictionary data structure
while i < len(lines):
    d = {}
    for j in range(n):
        x = lines[i + j].split()
        # print(i , "," ,j)
        d.update({x[1]: x[2]})
        temp = x[0]
    x = lines[i].split()
    dfa[x[0]] = d
    i = i + 2
print("the dfa is:")
print(dfa)


def next_state(current, char):  # this function returns the next state
    di = dfa[current]
    # print(di[char])
    return di[char]


def check_input(string):
    allowed_chars = set(lines[0])
    if set(string).issubset(allowed_chars):
        return True
    else:
        return False


# here we check if the string which we enter is accepted by the dfa or not
print("please enter the string :")
string = input()
state = lines[2].rstrip("\n")
if check_input(string) :
    for ch in string:
        state = next_state(state, ch)
    print("the last state of the string is: " + state)
    if state == lines[3].rstrip("\n"):
        print("the string is accepted by the dfa")
    else:
        print("the string is not accepted by the dfa")
else:
    print("the string is not valid")
f.close()







