import json, sys
nb = json.load(open(sys.argv[1], encoding='utf-8'))
out = []
for i, c in enumerate(nb['cells']):
    out.append(f'---CELL {i} {c["cell_type"]}---')
    out.append(''.join(c['source']))
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out))
print('wrote', sys.argv[2])
