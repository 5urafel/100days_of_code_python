row1 = ["\U0001f600" , "\U0001F923","\U0001F606" ]
row2 = ["\U0001F923","\U0001F606" ,"\U0001f600" ]
row3 = [ "\U0001F606","\U0001f600" ,"\U0001F923" ]

map = [row1 , row2 ,row3]
print(f"{row1} \n{row2} \n{row3}")
position = input('where do you want to put your treasur? ')

col=int(position[0]) - 1
row=int(position[1]) - 1

map [row][col] = 'X'
print(f"{row1} \n{row2} \n{row3}")
