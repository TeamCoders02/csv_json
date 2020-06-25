"""hello"""
class csv_to_json():
    def __init__(self):
        self.a=[]
        self.d=[]
        self.b=[]
        self.sti=[]


    def read_csv(self, path=None):
        if path==None:
            raise Exception('file name not found')
        f=open(path,'r')


        self.a = f.readline()
        self.d = self.a.split(",")
        for i in range(len(self.d)):
            self.d[i]=self.d[i].replace('\n','')
        self.b = f.readlines()
        for i in range(len(self.b)):
            self.b[i]=self.b[i].replace('\n','')
    def write_json(self,path=None,label=None):
        if path==None:
            f=open("JSON.json", "w")
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
                f.write(str(i))
                f.write(" : ")
                f.write(self.sti[k])
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
                    f.write(self.d[k])
                    f.write(' : ')
                    f.write(self.sti[k])
                    f.write(',')
                    f.write('\n')
                f.write('\t')
                f.write('} \n')
            f.write('}')
        f.close()
