# coding=utf-8
f = open("NFA_input_2.txt", "r")
lines = []
while True:
    line = f.readline()
    if line == '':
        break
    lines.append(line)
print("input NFA:")
print(* lines)
alphabets = lines[0].split()
states = lines[1].split()
start_states = lines[2].split()
final_states = lines[3].split()
transitions = []
for i in range(4, len(lines)):
    x = lines[i].split()
    transitions.append(x)
# in the transition list we store all the state transitions
# first we want to convert the nfa with landa moves to nfa without landa moves
for state in reversed(transitions):
    # print(state, "current")
    if state[1] == 'β':
        for i in transitions:
            if i[0] == state[2]:
                temp = [state[0], i[1], i[2]]
                transitions.append(temp)
                if start_states.count(state[0]) > 0 and start_states.count(state[2]) == 0:
                    start_states.append(state[2])
                if final_states.count(state[2]) > 0 and final_states.count(state[0]) == 0:
                    final_states.append(state[0])
        transitions.remove(state)
print("the nfa without lambda moves:")
print(*transitions)
print("nfa's final states:")
print(*final_states)
print("nfa's initial states:")
print(*start_states)
# now we have converted our nfa with landa moves to a nfa without landa moves. the next step is to convert this automata
# to a dfa. this is done below.
# the result will be written in a text file located in the project file name DFA_Output_2.txt


def string_to_list(l):
    return [(l[i: i + 2]) for i in range(0, len(l), 2)]


def next_state(current, c):
    l = []
    for i in transitions:
        if i[0] == current and i[1] == c:
            l.append(i)
    tmp = ""
    for j in l:
        tmp += j[2]
    return [current, c, tmp]


def func(list):  # this function is used to create a union of next states for dfa and remove the duplicate states
    temp = []
    for a in list:
        h = string_to_list(a)
        for t in h:
            if temp.count(t) == 0:
                temp.append(t)
    tmp = ''.join(map(str, temp))
    return tmp


dfa_states = []
dfa_states.append(states[0])
dfa_trans = []
for s in dfa_states:
    h = string_to_list(s)
    # print(h)
    for k in alphabets:  # here we produce the states for the dfa
        li = []
        stro = []
        for c in h:
            # print("c = ", c, "k = ", k)
            li.append(next_state(c, k))
            stro.append(next_state(c, k)[2])

        w = func(stro)
        # print(w + " the func result")
        if dfa_states.count(w) == 0:  # adding them to dfa states
            dfa_states.append(w)
        for x in li:
            x[0] = s
            x[2] = w
            if dfa_trans.count(x) == 0:
                dfa_trans.append(x)








dfa = []
for a in dfa_trans:  # checking for the duplicate lines nad removing them
    h = string_to_list(a[0])
    h2 = string_to_list(a[2])
    r = set(h)
    r1 = set(h2)
    a[0] = r
    a[2] = r1
    dfa.append(a)

# for a in dfa:
#     print(*a)
print()
dfa_f = []
f1 = open("DFA_Output_2.txt", "w")
f1.write(' '.join(map(str, alphabets)))  # writing in the file
f1.write("\n")
f1.write(' '.join(map(str, dfa_states)))
f1.write("\n")
f1.write(''.join(map(str, start_states[0])))
f1.write("\n")
final = []
for i in dfa_states:  # handling the the duplicates in the states of dfa and writing them in the file
    for j in final_states:
        if i.find(j) > -1 and final.count(i) == 0:
            tmp = set(string_to_list(i))
            final.append(tmp)
# print("the states:")
# print(final)
last = []
for a in final:
    if last.count(a) == 0 :
        last.append(a)
        b = ''.join(map(str, list(a)))
        f1.write(b + " ")
f1.write("\n")


for a in dfa:  # writing the transitions in the file
    if dfa_f.count(a) == 0:
        dfa_f.append(a)
        b1 = ''.join(map(str, list(a[0])))
        b2 = ''.join(map(str, list(a[2])))
        # a = ' '.join(map(str, list(a)))
        b = b1 + " " + a[1] + " " + b2
        f1.write(b + "\n")
        print(b)
f.close()
f1.close()














