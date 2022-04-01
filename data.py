def initilize( )  -> tuple:
    with open('./text.csv','r') as raw_csv:
        tuple_csv = tuple(raw_csv.read().splitlines())
    # main symbol and combinations of [ 4bit + 4bit ]
    sym = []
    part1 = []
    part1_unicode = []
    part2 = []
    part2_unicode = []
    #
    #### #### #### #### #### #### #### ####
    for i in tuple_csv:
        a,b,c = i.split(',')
        sym.append(a)
        part1.append(f'0b{b+c}')
        part2.append(f'0b{c+b}')
        part1_unicode.append(int(f'0b{b+c}',base=2))
        part2_unicode.append(int(f'0b{c+b}',base=2))
    return (sym,part1,part2,part1_unicode,part2_unicode)

def get( data:int )  -> str:
    sym,byte,etyb,unicode,edocinu = initilize()
    try:
        var = unicode.index(data)
        return (sym[var])
    except ValueError :
        print("\033[1;33msecound possibilitys for ",chr(data),'\033[0m\t\t',end='')
        try:

            var = edocinu.index(data)
            print("[  \033[1;32mOk\033[0m  ]")
            return (sym[var])
        except ValueError as e:
            print("[  \033[1;31mError\033[0m  ] \n skiping",chr(data),e)
            return "\033[1;31m#\033[0m"
from sys import argv
res=''
for i in argv[1]:
    res+=get(ord(i))
print("output\n",res)
