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

class Initials:
    def __init__(self, eax, ebx):
        self.eax = eax
        self.ebx = ebx

    def mov(self): #move cell eax to ebx
        mem.insert(self.ebx, '%s  |  %s' % (mem[self.ebx], mem[self.eax])); mem.remove(mem[self.eax]); mem.remove(mem[self.ebx]); mem.insert(self.eax, '-')

    def pop(self, pAddr): #pAddr is the cell you want you to pop
        if pAddr < 11:
            p1=mem[pAddr][:5]; p1=p1.replace('0x-', ''); p2=mem[pAddr][12:]; p2=p2.replace('0x-', ''); p1=int(p1); p2=int(p2)
            print(p1, p2, type(p1), type(p2), '\n')
            mem.remove(mem[pAddr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % p1); mem.insert(p2-1, '0x-%s' % p2)
        else:
            p1=mem[pAddr][:4]; p1=p1.replace('0x-', ''); p2=mem[pAddr][12:]; p2=p2.replace('0x-', ''); p1=cK[cV.index(p1)]; p2=cK[cV.index(p2)]
            print(p1, p2, type(p1), type(p2), '\n')
            mem.remove(mem[pAddr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % reg[p1]); mem.insert(p2-1, '0x-%s' % reg[p2])

asm = Initials(1, 14)

for pos in mem:
    print('%s' % pos)
print('--------------------\n\n')

asm.mov()

for pos in mem:
    print('%s' % pos)
print('--------------------\n\n')

asm.pop(14)

for pos in mem:
    print('%s' % pos)
print('--------------------\n\n')
input()
