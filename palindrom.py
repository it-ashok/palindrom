format(585, 'b')
'rev' == 'rev'[::-1]
[1,2,3],[::-1]
def con_bin(number):
   return format(number, 'b')

def is_pal(string):
  return string == string[::-1]

val = list(range(1000000))
val[-1]

pair = {str(a) : con_bin(a) for a in val}
pair['585']

once = {}

for k, v in pair.items():
   if is_pal(k) and is_pal(v):
      once[k] = v

len(pair.keys())
len(once.keys())
once
sum(list(map(int, list(once.keys()))))