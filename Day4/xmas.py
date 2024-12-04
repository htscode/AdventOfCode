
xmas_all = []
with open('input.txt','r') as f:
    for line in f:
        row= line.split()
        chared = list(row[0])
        xmas_all.append(chared)
sub_rectangle= [xmas_all[0][0:4],xmas_all[1][0:4],
                xmas_all[2][0:4],xmas_all[3][0:4]]


diagonal_2d = [[0,0],[1,1],[2,2],[3,3]]
vertical_2d = [[0,0],[1,0],[2,0],[3,0]]

vertical_2d_reversed=[[3,0],[2,0],[1,0],[0,0]]
diagonal_2d_reversed = [[3,3],[2,2],[1,1],[0,0]]

other_diagonal_2d = [[0,3],[1,2],[2,1],[3,0]]
other_diagonal_2d_reversed = [[3,0],[2,1],[1,2],[0,3]]

horizontal_2d = [[0,0],[0,1],[0,2],[0,3]]
horizontal_2d_reversed = [[0,3],[0,2],[0,1],[0,0]]

patterns = [diagonal_2d,vertical_2d,vertical_2d_reversed,diagonal_2d_reversed,
            other_diagonal_2d,other_diagonal_2d_reversed,horizontal_2d,horizontal_2d_reversed]
xmas = ['X','M','A','S']
counter = 0
pattern_names=['dig','ver','ver-rev','dig-rev','o-dig','o-dig-rev','hor','hor-rev']

for i in range(0,len(xmas_all)-3):
    for j in range(0,len(xmas_all[0])-3):
        sub_rectangle = [xmas_all[i][j:j+4],xmas_all[i+1][j:j+4],
                        xmas_all[i+2][j:j+4],xmas_all[i+3][j:j+4]]
        print('-'*20)
        #print("i",i,"j",j)
        #[print(row) for row in sub_rectangle]
        for pattern,name in zip(patterns,pattern_names):

            word = [sub_rectangle[index[0]][index[1]] for index in pattern]
            if word ==xmas:
                print(name)

                counter +=1
                print(counter)
        #last two rows not checked for horizontals
        if i == (len(xmas_all)-4):
            print("extra")
            for pattern in [horizontal_2d,horizontal_2d_reversed]:
                for e in range(1,4):
                    word = [sub_rectangle[index[0]+e][index[1]] for index in pattern]
                    #print(word)
                    if word == xmas:
                        print(name)
                        # print(word)
                        counter += 1
                        print("extra_counter",counter)
        if j == (len(xmas_all) - 4):
            for pattern in [vertical_2d, vertical_2d_reversed]:
                for e in range(1, 4):
                    word = [sub_rectangle[index[0] ][index[1]+ e] for index in pattern]
                    # print(word)
                    if word == xmas:
                        print(name)
                        # print(word)
                        counter += 1
                        print("extra_counter_vert", counter)

print(counter)
# part two
dig_mas =  [[0,0],[1,1],[2,2]]
other_dig_mas = [[0,2],[1,1],[2,0]]
dig_sam = [[2,2],[1,1],[0,0]]
other_dig_sam =[[2,0],[1,1],[0,2]]

mas = ["M","A","S"]
pattern_set_1 = [dig_mas,dig_sam]
pattern_set_2 = [other_dig_mas,other_dig_sam]
mas_counter = 0
for i in range(0,len(xmas_all)-2):
    for j in range(0,len(xmas_all[0])-2):
        print("-"*20)
        print("i",i,"j",j)
        sub_rectangle = [xmas_all[i][j:j+3],xmas_all[i+1][j:j+3],
                        xmas_all[i+2][j:j+3]]
        [print(row) for row in sub_rectangle]
        for pattern in pattern_set_1:
            word1 = [sub_rectangle[index[0]][index[1]] for index in pattern]

            for pattern_2 in pattern_set_2:
                word2=[sub_rectangle[index[0]][index[1]] for index in pattern_2]
                print("."*20)
                print(word1)
                print(word2)
                if word1==mas and word2 == mas:
                    mas_counter +=1
                    print(mas_counter)

print(mas_counter)
print("Yeah")