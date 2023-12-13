import random

delay_int = open("delay.txt","r")
delay_int = delay_int.read()
delay_max=0
temp = ""
list_of_instructions=[]
for i in delay_int:
    if i != '\n':
        
        temp += i
        # print(temp)
    else:

        list_of_instructions.append(temp)
        temp=""

x = list(map(str,list_of_instructions[0].split()))

for i in x:
    if (int(i) > delay_max):
        delay_max = int(i)

def generate_random_value(mean):
    std_dev=0.1*float(mean)
    while True:
        random_val = random.gauss(mean, std_dev)
        if mean - 3 * std_dev <= random_val <= mean + 3 * std_dev:
            return random_val

all_delays=[]
for i in range(9):
    temp1=[]
    for j in range(3):
        temp1.append(generate_random_value(int(x[j])))
    all_delays.append(temp1)

for i in range(len(x)):
    x[i]=int(x[i])
print(all_delays)