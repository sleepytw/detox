#Detox -> python language from scratch by .S L E E P Y'

import os

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

# commands = {
#     'program': program,
#     'mov': mov,
#     'pop': pop,
#     'save': save
# }

path=os.path.dirname(os.path.abspath(__file__))
filePath=os.path.join(path, 'test.dx') # Later i will make it inherit the name of the file u run it with
mem=[]
cK=list(reg.keys()) #cache keys
cV=list(reg.values()) #cache values

for bit in reg:
    mem.append('0x-%s' % reg[bit])

#Traceback errors (Exceptions)
class ProgramError(Exception): pass
class ParameterError(Exception): pass
class SaveError(Exception): pass
class CodeError(Exception): pass
class EvaluationGoneWrongLOLXDDDD(Exception): pass

class Build:
    # def __init__(self, eax, ebx):
    #     self.eax = eax
    #     self.ebx = ebx

    # def program(*args, **kwargs):
    #     pass

    def mov(self, eax: int, ebx: int): #move cell eax to ebx
        try:
            if eax or ebx in cV:
                mem.insert(ebx, '%s  |  %s' % (mem[ebx], mem[eax])); mem.remove(mem[eax]); mem.remove(mem[ebx]); mem.insert(eax, '-')
            else:
                raise ParameterError
        except ParameterError:
            print('ParameterError: Parameters not found and/or cannot convert str to int.')

    def pop(self, addr: int): #addr is the cell you want you to pop
        try:
            if str(addr) in cV:
                if addr < 11:
                    p1=mem[addr][:5]; p1=p1.replace('0x-', ''); p2=mem[addr][12:]; p2=p2.replace('0x-', ''); p1=int(p1); p2=int(p2)
                    mem.remove(mem[addr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % p1); mem.insert(p2-1, '0x-%s' % p2)
                else:
                    p1=mem[addr][:4]; p1=p1.replace('0x-', ''); p2=mem[addr][12:]; p2=p2.replace('0x-', ''); p1=cK[cV.index(p1)]; p2=cK[cV.index(p2)]
                    mem.remove(mem[addr]); mem.remove(mem[p2-1]); mem.insert(p1-2, '0x-%s' % reg[p1]); mem.insert(p2-1, '0x-%s' % reg[p2])
            else:
                raise ParameterError
        except ParameterError:
            print('ParameterError: Parameters not found and/or cannot convert str to int.')

    # def save(*args, **kwargs):
    #     pass

init = Build()

# HardCodedXD
class Interpreter:
    def __init__(self, memLoc: list, vars: list, bL: list, rev: list, calcD: dict):
        self.memLoc = memLoc
        self.vars = vars
        self.bL = bL
        self.rev = rev
        self.calcD = calcD

    def readFile(self):
        with open(filePath, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for i in data:
                self.memLoc.append(i.strip('\n'))

    def readData(self):
        try:
            if not bool(self.memLoc):
                raise CodeError
            else:
                try:
                    if 'program' in self.memLoc[0]:
                        programName = self.memLoc[0][7:]
                        #Initialize the program function here *(...)
                        try:
                            for i in self.memLoc:
                                if i == None:
                                    self.memLoc.remove(self.memLoc[i])
                            for k in range(len(self.memLoc)):
                                if 'mov' in self.memLoc[k]:
                                    movIndex = self.memLoc.index(self.memLoc[k])
                                    init.mov(int(self.memLoc[movIndex][4:5]), int(self.memLoc[movIndex][7]))
                            for j in range(len(self.memLoc)):
                                if 'pop' in self.memLoc[j]:
                                    popIndex = self.memLoc.index(self.memLoc[j])
                                    init.pop(int(self.memLoc[popIndex][4:]))
                            # if 'save' in self.memLoc:
                            #     init.save(self.memLoc[-1][5:len(self.memLoc[-1])])
                            #else:
                                #raise SaveError
                            try:
                                for n in mem:
                                    if len(mem[n]) == 4:
                                        self.vars.insert(n, '0')
                                    elif mem[n] == '-':
                                        self.vars.insert(n, '0')
                                    elif len(mem[n]) > 4:
                                        self.vars.insert(n, '1')
                                    else: pass
                                with open('output.txt', 'w', encoding='utf-8') as ot:
                                    for i in self.vars:
                                        ot.write(i)
                            except:
                                pass
                        except SaveError:
                            print('SaveError: Save location not given.')
                    else:
                        raise ProgramError
                except ProgramError:
                    print('ProgramError: Program not allocated correctly.')
        except CodeError:
            print('CodeError: The interpreter failed reading the file.')

# class Evaluate:
#     bL = list()
#     def __init__(self, bL):
#         pass

    def sum(self, array, var: int):
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
                UIndex = self.memLoc.index(self.memLoc[i])
                self.bL.remove(UIndex)

        bls = self.bL[0]#; rev=list(); calcD=dict()
        for evr in bls:
            self.rev.append(str(evr))
        print(self.rev)
        for elm in range(len(self.rev)):
            if self.rev[elm] == '0': self.rev[elm]=2
            elif self.rev[elm] == '-': self.rev[elm]=2
            elif self.rev[elm] == '1': self.rev[elm]=4**2
            else: pass
        for i in self.rev:
            total+=sum(self.rev)

interpreter = Interpreter([], [], [], [], {})
interpreter.readFile()
interpreter.readData()
