
def type_ch(item):
    try:
        if '.' in item:
            x=float(item)
        else :
            x=int(item)
        return str(x)
    except :
        if item=='True' or item=='true':
            return str(True)
        if item=='False' or item=='false':
            return str(False)

        return '"'+item+'"'

class csv_to_json():
    def __init__(self):
        self.a=[]
        self.d=[]
        self.b=[]
        self.sti=[]
        self.p=''



    def read_cs(self, path=None):
        if path==None:
            raise Exception('file name not found')
        f=open(path,'r')
        self.p=path

        self.a = f.readline()
        self.d = self.a.split(",")
        for i in range(len(self.d)):
            self.d[i]=self.d[i].replace('\n','')
        self.b = f.readlines()
        for i in range(len(self.b)):
            self.b[i]=self.b[i].replace('\n','')
    def write_js(self,path=None,label=None):
        if path==None:
            m=self.p.index('.')
            self.p=(self.p[:m]+'.json')
            f=open(self.p,'w')
        else :
            f=open(path,'w')
        if label!=None:
            if len(self.b[0].split(','))!=len(label):
                raise Exception('length of label incompatible')
            else :
                self.d=label
        f.write("{")
        f.write("\n")
        k=0
        if len(self.b) == 1:
            self.sti=self.b[0].split(',')
            for i in self.d:
                f.write("\t")

                f.write(type_ch(i))
                f.write(" : ")
                f.write(type_ch(self.sti[k]))

                k+=1
                f.write(',')
                f.write("\n")
            f.write("}")
        else :
            for j in range(len(self.b)):
                self.sti=self.b[j].split(',')
                for k in range(len(self.sti)):
                    self.sti[k]=self.sti[k].replace('\n','')
                f.write('\t')
                f.write('{')
                f.write('\n')
                for k in range(len(self.sti)):
                    f.write('\t')
                    f.write('\t')
                    f.write(type_ch(self.d[k]))
                    f.write(' : ')
                    f.write(type_ch(self.sti[k]))

                    f.write(',')
                    f.write('\n')
                f.write('\t')
                f.write('} \n')
            f.write('}')
        f.close()
