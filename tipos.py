# O tipo Lista é mutável e multivalorada
print(">>>>> LISTA")
l = [ ]
la = list()
l.append(10)
l.append(10.5)
l.append("Teste")
l.append(True)
l.append(list())
l.append(tuple())
print(la, l) # ver os métodos possíveis: l.

# Tupla é imutável e multivalorada, usada para manter headers de tabelas imutáveis
print(">>>>> TUPLA")
t = (10,10.5,"Teste",True,list(),tuple(),(10,2))
ta = tuple()
print(ta, t) # ver os métodos possíveis: t.

# Set é mutável, multivalorado e NÃO PERMITE DADOS REPETIDOS, simula um banco de dados (JOIN)
print(">>>>> SET")
s = {10}
sa = set()
#sa.add(2)
s.add(20.5)
s.add(10)
s.add(10.0)
s.add(20.0)
s.add(20)
s.add('10.0')
print(s) # ver os métodos possíveis: s.

# Dicionário é mutável, multivalorado e "dá nomes" aos índices, NÃO PERMITE CHAVES REPETIDAS (importou chaves {} do set)
print(">>>>> DICIONÁRIO")
da = dict()
db = {}
d = {
    'nome': 'felipe',
    'idade': 10,
    "nome": 'felipe2'
}
print(da, db, type(db), d) # ver os métodos possíveis: d.