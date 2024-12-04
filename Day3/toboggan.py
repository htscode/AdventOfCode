# multiply numbers
# mul(X,Y)
# X,Z 1-3 digits
# ignore invalid patterns
import re
# load data
with open('input.txt','r') as f:
    data = f.read()
# built regex
myregex = r"mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)"
allfinds = re.findall(myregex,data)
sum = 0
for multiplication in allfinds:
    number1=int(multiplication[0])
    number2=int(multiplication[1])
    result = number1*number2
    sum += result

print(sum)
# part 2
# stat mul enable
# dont turns it of
# do turns it on
dos = data.find("do()")


do_regex=r"do\(\)"
dont_regex=r"don't\(\)"

do_pos_old= [match.start() for match in re.finditer(do_regex,data)]
do_pos = [0]+do_pos_old
dont_pos= [match.start() for match in re.finditer(dont_regex,data)]
regex_pos= [match.start() for match in re.finditer(myregex,data) ]
regex_nums= [match.group().strip("mul") for match in re.finditer(myregex,data) ]
on = True
i=0
j=0
sum_advanced = 0
for mul,k in zip(regex_pos,range(0,len(regex_pos))):
    #check if forward
    while i+1 < len(dont_pos) and dont_pos[i+1]< mul:
        i+=1
    while j+1 < len(do_pos) and do_pos[j+1]< mul:
        j+=1
    #check on off change
    if dont_pos[i] > do_pos[j] and dont_pos[i] < mul:
        on = False
    else:
        on = True
    if on:
        number1 = int(allfinds[k][0])
        number2 = int(allfinds[k][1])
        result = number1 * number2
        sum_advanced += result
print(sum_advanced)




#while notend:
#    first_mul_ind = data.find('mul')
#    if data[first_mul_ind+1]=='(':
#        #check one or 3 digit number
#        try:
#            mul_num_1= int(data[first_mul_ind+2])
#        except ValueError:
#            flag  = False

# cut string


# scan to find mul
# check next (
# check next 1-3 digit number
# check ,
# check 1-3 digit number
# check )
# if true multiply numbers
# add to subtotal

print("Yeah")