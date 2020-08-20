

class json_to_csv():
    def __init__(self):
        self.stri=''
        self.st=''
        self.a=[]
        self.b=[]
        self.p=''

    def read_js(self,path):
        self.p=path
        l=open(path,'r').readlines()
        for i in l:
            i=i.replace('\t','')
            i=i.replace('\n','')
            self.stri+=i
        self.st=self.stri



    def write_cs(self,path=None,head=None):
        self.st=self.stri
        self.st=self.st.replace('{','')
        self.st=self.st.replace('}','')


        while len(self.st)!=0:
            try:
                i=self.st.index(':')
                k=self.st[:i]
                k=k.replace(' ','')
                if k not in self.a:
                    self.a.append(k)
                self.st=self.st[i+1:]


                try :
                    i=self.st.index(',')
                    self.b.append(self.st[:i])
                    self.st=self.st[i+1:]
                except :
                    self.b.append(self.st[:])
                    self.st=''
            except:
                self.st=''


        for i in range(len(self.b)):
            self.b[i]=self.b[i].replace(' ','')

        if path==None:
            m=self.p.index('.')
            self.p=(self.p[:m]+'.csv')
            f=open(self.p,'w')



        else :
            f=open(path,'w')

        if head==None:


            for i in self.a:
                if self.a.index(i)!=len(self.a)-1:
                    f.write(i)
                    f.write(',')
                else:
                    f.write(i)
                    f.write('\n')
            for i in range(len(self.b)):
                if i%len(self.a)!=len(self.a)-1:

                    f.write(self.b[i])
                    f.write(',')
                else:

                    f.write(self.b[i])
                    f.write('\n')
        else :


            for i in head:
                if head.index(i)!=len(head)-1:
                    f.write(i)
                    f.write(',')
                else:
                    f.write(i)
                    f.write('\n')
            for i in self.b:
                if self.b.index(i)%len(self.a)!=len(self.a)-1:
                    f.write(i)
                    f.write(',')
                else:
                    f.write(i)
                    f.write('\n')
