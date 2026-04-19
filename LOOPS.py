#print('round: 1')
#print('round: 2')
#print('round: 3')
#print('round: 4')
#print('round: 5')
#instead of repeating like this yor can just use loop function 
for i in (1, 2, 3, 4, 5):
    print( f'round: {i}')

for joy in ('fear', 'anxiety', 'drama'):
    print(f'emotion: {joy}')

tests = ('a', 'b', 'c', 'd', 'e')
for test in tests:
    print(f'round: {test}')
    
#for item in range('start', 'end', 'step'):
    #print(f'round: {item}') 
    # therefore. also range is always of numbers

for item in range(2, 10, 2):
    print( f'round: {item}')

# real life application of 'FOR LOOPS'
files = ['  Report.Csv', ' DATA.csV   ', ' FINAl.txt ']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f'processing {file}')

#chall: print the table of 7 from 1 to 10 using loop
#chall2: print a left aligned pyramind of starts with 6 rows using for loop


#BREAK STATEMENT IN FOR LOOP 
names = ['kavya', 'hitesh', '', 'jatin']
for name in names:
    if name == '':
        print('empty detected')
        break
    print(f'name = {name}')

# CONTINUE IN FOR LOOP 

names = ['kavya', 'hitesh', '', 'jatin']
for name in names:
    if name == '':
        print('empty detected')
        continue
    print(f'name = {name}')

# PASS IN FOR LOOP

names = ['kavya', 'hitesh', '', 'jatin']
for name in names:
    if name == '':
        print('empty detected')
        pass
    print(f'name = {name}')

# OR WE CAN DO THIS AS WELL 
names = ['kavya', 'hitesh', '', 'jatin']
for name in names:
    if name == '':
        name = name.replace('','NA')   
    print(f'name = {name}')


#TASK: SCAN THRU EMAILS AND BLOCK UNSAFE DATA ENTERING INTO SYSTEM==6.04.31
#6:15:38
#CHALL: CHECK WHETHER DUPLICATE OR NOT, else all files unique
file_list = [
    'kavya.csv',
    'bkp.csv',
    'summary.pdf',
    'opd.csv'
]
print(file_list)

#else foe nested loop ##### used for pairing and combining data
#  OR navigating heirarchy
for x in range(3): #outer loop
    for y in range(2):
        for z in range(2): #inner loop
            print(f'({x}, {y}, {z})')

## WHILE LOOP ##
# creating counter page loop  ##
count = 1
while count <= 5:
    print(count)
    count += 1 

answer = ''
while answer != 'yes':
    answer = input('do you agree?(yes/no): ')
print('thnk u')

## WHILE TRUE
while True:
    answer = input(' do u agree?(yes/no): ')
    if answer == 'yes':
        break 
print('thank u')

#chall: same yes/no challenge ## 
# only 3 attemots, if yes then 'glad were on the same page'; 
# else '3 strikes! youre out!'
