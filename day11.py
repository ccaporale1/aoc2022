import math
import numpy as np
import operator

verbose = False

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

class Monkey ():
    
    worry_management = None

    def __init__(self,items=[1,2,3],operation=['+',1],test=3,true_val=2,false_val=3):
        self.items = items
        self.operation_type = operators[operation[0]]
        if len(operation) == 2:
            self.operation_amt = int(operation[1])
        else: self.operation_amt = 'none'
        self.test_val = test
        self.true_val = true_val
        self.false_val = false_val
        self.num_inspect = 0

    @staticmethod
    def set_worry_management(troop):
        Monkey.worry_management = math.prod([m.test_val for m in troop])

    def operate(self,old):
        if not isinstance(self.operation_amt,int):
            if not self.operation_amt.isdigit():
                amt = int(old)
            else: amt =self.operation_amt
        else: amt =self.operation_amt
        return self.operation_type(old,amt)

    def monkey_test(self,item):
        # tests item on monkey and returns which monkey it should go to
        self.num_inspect += 1
        if item % self.test_val == 0:
            return self.true_val           
        
        else: return self.false_val
        


with open('./inputs/day11_input.txt') as f:
    data = f.read().split('\n')

part_id = 2
if part_id == 1:
    rounds = 20
elif part_id == 2:
    rounds = 10000
# create default monkey object
monkey = {
    'num': 0,
    'items': [10,20],
    'operand': '+ 2',
    'test': 'div by 19',
    'true': 1,
    'false': 2,
}

monkeys = []
# build monkey objects
for line in data:
    if 'Monkey' in line: 
        monkey['num'] += 1
    if 'Starting' in line:
        monkey['items'] = []
        for items in line.split():
            if items.replace(',','').isdigit():
                monkey['items'].append(int(items.replace(',','')))
    if 'Operation' in line:
        monkey['operand'] = []
        for items in line.split():
            if items in operators.keys() or items.isdigit():
                monkey['operand'].append(items)
    if 'Test' in line:
        for items in line.split():
            if items.isdigit():
                monkey['test'] = int(items)
    if 'true' in line:
        for items in line.split():
            if items.isdigit():
                monkey['true'] = int(items)
    if 'false' in line:
        for items in line.split():
            if items.isdigit():
                monkey['false'] = int(items)
    if line == '':
        monkeys.append(Monkey(items=monkey['items'],operation=monkey['operand'],test=monkey['test'],true_val=monkey['true'],false_val=monkey['false']))
monkeys.append(Monkey(items=monkey['items'],operation=monkey['operand'],test=monkey['test'],true_val=monkey['true'],false_val=monkey['false']))

if part_id == 2:
        Monkey.set_worry_management(monkeys)

for x in range(0,rounds):
    for y in range(0,len(monkeys)):
        if verbose: print('Monkey ',y,':')
        for item in range(0,len(monkeys[y].items)):
            if verbose: print('Monkey inspects an item with a worry level of ', monkeys[y].items[0])
            new_worry_level = int(monkeys[y].operate(monkeys[y].items[0]))
            
            if verbose: print('Worry level increases: ',monkeys[y].operation_type,' ',monkeys[y].operation_amt,' to ',new_worry_level)
            if part_id == 1: monkeys[y].items[0] = math.floor( new_worry_level / 3)
            if part_id == 2: monkeys[y].items[0] = math.floor(new_worry_level % Monkey.worry_management)
            if verbose: print('Monkey gets bored and worry level drops to ',monkeys[y].items[0])
            perform_check = monkeys[y].monkey_test(monkeys[y].items[0])
            if verbose: print('Item with worry level ', monkeys[y].items[0],' is thrown to monkey',perform_check)
            monkeys[perform_check].items.append(monkeys[y].items.pop(0))
            
    if verbose: print('After round ', x+1)
    for y in range(0,len(monkeys)):
        if verbose: print('Monkey ',y,': ',monkeys[y].items)


monkey_business = []
for y in range(0,len(monkeys)):
    monkey_business.append(monkeys[y].num_inspect)
monkey_business.sort(reverse=True)

print('Part ',part_id,': monkey business value is ',monkey_business[0] * monkey_business[1])
