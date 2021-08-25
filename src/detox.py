#Detox -> 16-bit language by .S L E E P Y'

reg = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '0',
    11: 'A',
    12: 'B',
    13: 'C',
    14: 'D',
    15: 'E',
    16: 'F'
}

mem=[]
cK=list(reg.keys()) #cache keys
cV=list(reg.values()) #cache values

for bit in reg:
    mem.append('0x-%s' % reg[bit])

class Build:
    def __init__(self, eax, ebx):
        self.eax = eax
        self.ebx = ebx

    def mov(self): #move cell eax to ebx
        mem.insert(self.ebx, '%s  |  %s' % (mem[self.ebx], mem[self.eax])); mem.remove(mem[self.eax]); mem.remove(mem[self.ebx]); mem.insert(self.eax, '-')

    def pop(self, pAddr): #pAddr is the cell you want you to pop
        if pAddr < 11:
            p1=mem[pAddr][:5]; p1=p1.replace('0x-', ''); p2=mem[pAddr][12:]; p2=p2.replace('0x-', ''); p1=int(p1); p2=int(p2)
            mem.remove(mem[pAddr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % p1); mem.insert(p2-1, '0x-%s' % p2)
        else:
            p1=mem[pAddr][:4]; p1=p1.replace('0x-', ''); p2=mem[pAddr][12:]; p2=p2.replace('0x-', ''); p1=cK[cV.index(p1)]; p2=cK[cV.index(p2)]
            mem.remove(mem[pAddr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % reg[p1]); mem.insert(p2-1, '0x-%s' % reg[p2])

class Interpreter:
    bL = list()
    def __init__(self, bL):
        pass
    
    def sum(array, var: int):
        for i in range(len(array)):
            var+=array[i]
        return var

    def read(self):
        with open('output.txt', 'r', encoding='utf-8') as ot:
            data = ot.readlines()
            for ln in data:
                self.bL.append(ln)

    def calc(self, total=0):
        bls = self.bL[0]; rev=list(); calcD=dict()
        for evr in bls:
            rev.append(str(evr))
        print(rev)
        for elm in range(len(rev)):
            if rev[elm] == '0': rev[elm]=2
            elif rev[elm] == '-': rev[elm]=2
            elif rev[elm] == '1': rev[elm]=4**2
            else: pass
        for i in rev:
            total+=sum(rev)
