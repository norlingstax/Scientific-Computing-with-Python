class Category:
    wdrwls = 0
    def __init__ (self,cat):
        self.ledger = []
        self.cat = cat
        self.balance = 0
    def check_funds (self, am):
        if am > self.balance:
            return False
        else: return True
    def deposit (self, am, des = ''):
        self.ledger.append({'amount': am, 'description': des})
        self.balance += am
    def withdraw (self, am, des = ''):
        if self.check_funds(am) == True:
            self.ledger.append({'amount': -am, 'description': des})
            self.balance-=am
            self.wdrwls += abs(am)
            return True
        else:return False
    def get_balance (self):
        return self.balance
    def transfer (self, am, cat):
        if self.check_funds(am) == True:
            wdes = 'Transfer to ' + cat.cat
            ddes = 'Transfer from ' + self.cat
            self.withdraw(am, wdes)
            cat.deposit(am, ddes) 
            return True
        else: return False
    def __str__ (self):
        header = self.cat.center(30,'*')+'\n'
        output = ''
        total = 0
        for item in self.ledger:
            desc = item['description'][0:23]
            am = str("%.2f" % item['amount'])[0:7].rjust(30-len(desc))
            output += f"{desc}{am}\n"
            total += item['amount']
        output += f'Total: {total}'
        return header + output

def create_spend_chart (categories):
    header = 'Percentage spent by category'
    body = ''
    
    totexp = {}
    catexp = {}
    total = 0
    
    for cat in categories:
        totexp[cat.cat] = cat.wdrwls
        total += cat.wdrwls
    for cat, am in totexp.items():
        catexp[cat] = round((am)/total*100)
    for num in range(100,-1,-10):
        body += f'\n{str(num).rjust(3)}| '
        for v in catexp.values():
          if (v>=num):
            body += 'o  '
          else:
            body += '   '
    line = f'\n    -{"---"*len(categories)}\n'
    
    maxname = max(len(name) for name in totexp.keys())
    names = ''
    for i in range (maxname):
        names += ' ' * 5
        for key in totexp.keys():
            if (len(key) <= maxname):
                key = key + (" ")*(maxname-len(key))
                names += f"{key[i]}  "
        names += "\n"
    names = names.rstrip()
    names += '  '
    #print (type(header),type(body),type(line),type(names))
    return header + body + line + names