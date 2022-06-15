#Detox -> python language from scratch by sleepy

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

mem=[]
path=os.path.dirname(os.path.abspath(__file__))
filePath=os.path.join(path, 'test.dx') # Later i will make it inherit the name of the file u run it with
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
    def __init__(self, memcache: list, vars: list, storage: list, bits: list, temp: dict):
        self.memcache = memcache
        self.vars = vars
        self.storage = storage
        self.bits = bits
        self.temp = temp

    def readFile(self):
        with open(filePath, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for i in data:
                self.memcache.append(i.strip('\n'))

    def readData(self):
        try:
            if not bool(self.memcache):
                raise CodeError
            else:
                try:
                    if 'program' in self.memcache[0]:
                        programName = self.memcache[0][7:]
                        #Initialize the program function here *(...)
                        try:
                            for i in self.memcache:
                                if i == None:
                                    self.memcache.remove(self.memcache[i])
                            for k in range(len(self.memcache)):
                                if 'mov' in self.memcache[k]:
                                    movIndex = self.memcache.index(self.memcache[k])
                                    init.mov(int(self.memcache[movIndex][4:5]), int(self.memcache[movIndex][7]))
                            print(mem)
                            for j in range(len(self.memcache)):
                                if 'pop' in self.memcache[j]:
                                    popIndex = self.memcache.index(self.memcache[j])
                                    init.pop(int(self.memcache[popIndex][4:]))
                            print(mem)
                            # if 'save' in self.memcache:
                            #     init.save(self.memcache[-1][5:len(self.memcache[-1])])
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
                                with open('output.txt', 'w', encoding='utf-8') as output:
                                    for i in self.vars:
                                        output.write(i)
                            except:
                                pass
                        except SaveError:
                            print('SaveError: Save location not given.')
                    else:
                        raise ProgramError
                except ProgramError:
                    print('ProgramError: Program not allocated correctly. \n/!\ Check if its first in the code, if not, move it there.')
        except CodeError:
            print('CodeError: The interpreter failed reading the file. \n/!\ Check if its last in the code, if not, move it there.')

# class Evaluate:
#     storage = list()
#     def __init__(self, storage):
#         pass

    def sum(self, array, var: int):
        for i in range(len(array)):
            var+=array[i]
        return var

    def readOutput(self):
        with open('output.txt', 'r', encoding='utf-8') as ot:
            data = ot.readlines()
            for line in data:
                self.storage.append(line)

    def calculate(self, total=0):
        for i in self.storage:
            if '' in self.storage[i]:
                UIndex = self.memcache.index(self.memcache[i])
                self.storage.remove(UIndex)

        storageA = self.storage[0]#; bits=list(); temp=dict()
        for each in storageA:
            self.bits.append(str(each))
        print(self.bits)
        for element in range(len(self.bits)):
            if self.bits[element] == '0': self.bits[element]=2
            elif self.bits[element] == '-': self.bits[element]=2
            elif self.bits[element] == '1': self.bits[element]=4**2
            else: pass
        for _ in self.bits:
            total+=sum(self.bits)

interpreter = Interpreter([], [], [], [], {})
interpreter.readFile()
interpreter.readData()
