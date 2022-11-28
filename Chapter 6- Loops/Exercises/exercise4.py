sandwhich_order=['Mutton','Egg','Hotdog','boneless fish']
finished_sandwhich=[]

while sandwhich_order:
    current_sandwhich=sandwhich_order.pop()
    print('I made your '+  current_sandwhich  +' sandwhich')
    finished_sandwhich.append(current_sandwhich)
    print('\n')

for sandwhich in finished_sandwhich:
    print('I made your ' + sandwhich + ' sandwhich')