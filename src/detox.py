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

commands = {
    'program': program,
    'mov': mov,
    'pop': pop,
    'save': save
}

mem=[]
cK=list(reg.keys()) #cache keys
cV=list(reg.values()) #cache values

for bit in reg:
    mem.append('0x-%s' % reg[bit])

#Traceback errors (Exceptions)
class ProgramNotPointed(Exception): pass
class InsufficientParameters(Exception): pass
class UndefinedSavingPoint(Exception): pass
class InsufficientCodePass(Exception): pass
class EvaluationGoneWrongOMG(Exception): pass

class Build:
    def __init__(self, eax, ebx):
        self.eax = eax
        self.ebx = ebx

    def mov(self): #move cell eax to ebx
        try:
            if self.eax or self.ebx == None:
                raise InsufficientParameters
            else:
                mem.insert(self.ebx, '%s  |  %s' % (mem[self.ebx], mem[self.eax])); mem.remove(mem[self.eax]); mem.remove(mem[self.ebx]); mem.insert(self.eax, '-')
        except InsufficientParameters:
            print('ParameterError: Falsely pointed parameters.')

    def pop(self, addr): #addr is the cell you want you to pop
        try:
            if addr == None:
                raise InsufficientParameters
            else:
                if addr < 11:
                    p1=mem[addr][:5]; p1=p1.replace('0x-', ''); p2=mem[addr][12:]; p2=p2.replace('0x-', ''); p1=int(p1); p2=int(p2)
                    mem.remove(mem[addr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % p1); mem.insert(p2-1, '0x-%s' % p2)
                else:
                    p1=mem[addr][:4]; p1=p1.replace('0x-', ''); p2=mem[addr][12:]; p2=p2.replace('0x-', ''); p1=cK[cV.index(p1)]; p2=cK[cV.index(p2)]
                    mem.remove(mem[addr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % reg[p1]); mem.insert(p2-1, '0x-%s' % reg[p2])
        except InsufficientParameters:
            print('ParameterError: Falsely pointed parameters.')

init = Build()

# HardCodedXD
class Interpreter:
    memLoc=[]
    vars=[]
    with open('test.dx', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for i in data:
            memLoc.append(i)

    def readData():
        try:
            if bool(memLoc):
                raise InsufficientCodePass
            else:
                try:
                    if 'program' in memLoc[0]:
                        programName = memLoc[0][7:]
                        try:
                            for i in memLoc:
                                if '' in memLoc:
                                    memLoc.remove(memLoc[i])
                            for k in memLoc:
                                if 'mov' in memLoc:
                                    movIndex[k] = memLoc.index(memLoc[k])
                            for j in memLoc:
                                if 'pop' in memLoc:
                                    popIndex[j] = memLoc.index(memLoc[j])
                            for l in memLoc:
                                if 'save' in memLoc:
                                    saveIndex[l] = memLoc.index(memLoc[l])
                                else:
                                    raise UndefinedSavingPoint
                            try:
                                init.mov(memLoc[movIndex][4:], memLoc[movIndex][5:len(memLoc[movIndex])])
                                init.pop(memLoc[popIndex][4:len(memLoc[popIndex])])
                                #save(memLoc[saveIndex][5:len(memLoc[saveIndex])])
                                try:
                                    for n in mem:
                                        if len(mem[n]) == 4:
                                            vars.insert(n, '0')
                                        elif len(mem[n]) == '-':
                                            vars.insert(n, '0')
                                        elif len(mem[n]) > 4:
                                            vars.insert(n, '1')
                                        else: pass
                                    with open('output.txt', 'w', encoding='utf-8') as ot:
                                        for i in vars:
                                            ot.write(i)
                                except:
                                    pass
                            except:
                                pass
                        except UndefinedSavingPoint:
                            print('SaveError: Undefined output position.')
                    else:
                        raise ProgramNotPointed
                except ProgramNotPointed:
                    print('ProgramError: Program not initialized.')
        except InsufficientCodePass:
            print('CodeError: Empty file or something went wrong.')

class Evaluate:
    bL = list()
    def __init__(self, bL):
        pass

    def sum(array, var: int):
        for i in range(len(array)):
            var+=array[i]
        return var

    def readOutput(self):
        with open('output.txt', 'r', encoding='utf-8') as ot:
            data = ot.readlines()
            for ln in data:
                self.bL.append(ln)

    def calc(self, total=0):
        for i in self.bL:
            if '' in self.bL[i]:
                UIndex = memLoc.index(memLoc[l])
                self.bL.remove(UIndex)

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
