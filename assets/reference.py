from customtkinter import CTkFrame, CTkEntry, CTkComboBox, CTkLabel, CTkSwitch, CTkFont, StringVar, DoubleVar, IntVar, CTkScrollableFrame, CTkImage
from typing import Literal
from PIL import Image

# Detail & Adjust Frame
INF = {"f": (0, 0, 4, 4, (10,(10,5)), (3,2), "h"),
       "l": ((0,3,"w"), (3,3,"w"), (6,3,"w"), (9,3,"w"))#col, colspan, sticky #info
      } 
TAB = {"f": (3, 0, (10,5), (13,2)),
       "l": (((0,13,"ew"), (0,13,"w")), #title
             ((1,5,"w"), (6,3,"e"),  (9,3,"e")), # point
             ((0,9,"e"), (9,3,"e")),#result
             ((0,6,"w"), (6,3,"e"), (9,3,"e")),#highlight1
             ((0,6,"w"), (6,6,"e"))#highlight2
            )
      }
# Data Pajak
PTKP = {
    "s":("TK/0"      ,"TK/1"      ,"TK/2"      ,"TK/3"      ,"K/0"       ,"K/1"       ,"K/2"       ,"K/3"),
    "t":(54000000    ,58500000    ,63000000    ,67500000    ,58500000    ,63000000    ,67500000    ,72000000),
    "k":("Kategori A","Kategori A","Kategori B","Kategori B","Kategori A","Kategori B","Kategori B","Kategori C")}
KATEGORI = {
    "Kategori A":{"-":(0      ,5400001,5650001,5950001,6300001,6750001,7500001,8550001,9650001 ,10050001,10350001,10700001,11050001,11600001,12500001,13750001,15100001,16950001,19750001,24150001,26450001,28000001,30050001,32400001,35400001,39100001,43850001,47800001,51400001,56300001,62200001,68600001,77500001,89000001 ,103000001,125000001,157000001,206000001,337000001,454000001,550000001,695000001,910000001 ,1400000001),
                  "+":(5400000,5650000,5950000,6300000,6750000,7500000,8550000,9650000,10050000,10350000,10700000,11050000,11600000,12500000,13750000,15100000,16950000,19750000,24150000,26450000,28000000,30050000,32400000,35400000,39100000,43850000,47800000,51400000,56300000,62200000,68600000,77500000,89000000,103000000,125000000,157000000,206000000,337000000,454000000,550000000,695000000,910000000,1400000000,999999999999999),
                  "%":(0      ,0.0025 ,0.005  ,0.0075 ,0.01   ,0.0125 ,0.015  ,0.0175 ,0.02    ,0.0225  ,0.025   ,0.03    ,0.035   ,0.04    ,0.05    ,0.06    ,0.07    ,0.08    ,0.09    ,0.1     ,0.11    ,0.12    ,0.13    ,0.14    ,0.15    ,0.16    ,0.17    ,0.18    ,0.19    ,0.2     ,0.21    ,0.22    ,0.23    ,0.24     ,0.25     ,0.26     ,0.27     ,0.28     ,0.29     ,0.3      ,0.31     ,0.32     ,0.33      ,0.34)},
    "Kategori B":{"-":(0      ,6200001,6500001,6850001,7300001,9200001 ,10750001,11250001,11600001,12600001,13600001,14950001,16400001,18450001,21850001,26000001,27700001,29350001,31450001,33950001,37100001,41100001,45800001,49500001,53800001,58500001,64000001,71000001,80000001,93000001 ,109000001,129000001,163000001,211000001,374000001,459000001,555000001,704000001,957000001 ,1405000001),
                  "+":(6200000,6500000,6850000,7300000,9200000,10750000,11250000,11600000,12600000,13600000,14950000,16400000,18450000,21850000,26000000,27700000,29350000,31450000,33950000,37100000,41100000,45800000,49500000,53800000,58500000,64000000,71000000,80000000,93000000,109000000,129000000,163000000,211000000,374000000,459000000,555000000,704000000,957000000,1405000000,999999999999999),
                  "%":(0      ,0.0025 ,0.005  ,0.0075 ,0.01   ,0.015   ,0.02    ,0.025   ,0.03    ,0.04    ,0.05    ,0.06    ,0.07    ,0.08    ,0.09    ,0.1     ,0.11    ,0.12    ,0.13    ,0.14    ,0.15    ,0.16    ,0.17    ,0.18    ,0.19    ,0.2     ,0.21    ,0.22    ,0.23    ,0.24     ,0.25     ,0.26     ,0.27     ,0.28     ,0.29     ,0.3      ,0.31     ,0.32     ,0.33      ,0.34)},
    "Kategori C":{"-":(0      ,6600001,6950001,7350001,7800001,8850001,9800001 ,10950001,11200001,12050001,12950001,14150001,1550001,17050001,19500001,22700001,26600001,28100001,30100001,32600001,35400001,38900001,43000001,47400001,51200001,55800001,60400001,66700001,74500001,83200001,95600001 ,110000001,134000001,169000001,221000001,390000001,463000001,561000001,709000001,965000001 ,1419000001),
                  "+":(6600000,6950000,7350000,7800000,8850000,9800000,10950000,11200000,12050000,12950000,14150000,1550000,17050000,19500000,22700000,26600000,28100000,30100000,32600000,35400000,38900000,43000000,47400000,51200000,55800000,60400000,66700000,74500000,83200000,95600000,110000000,134000000,169000000,221000000,390000000,463000000,561000000,709000000,965000000,1419000000,999999999999999),
                  "%":(0      ,0.0025 ,0.005  ,0.0075 ,0.01   ,0.0125 ,0.015   ,0.0175  ,0.02    ,0.03    ,0.04    ,0.05   ,0.06    ,0.07    ,0.08    ,0.09    ,0.1     ,0.11    ,0.12    ,0.13    ,0.14    ,0.15    ,0.16    ,0.17    ,0.18    ,0.19    ,0.2     ,0.21    ,0.22    ,0.23    ,0.24     ,0.25     ,0.26     ,0.27     ,0.28     ,0.29     ,0.3      ,0.31     ,0.32     ,0.33      ,0.34)},
    "Harian":{"-":(0     ,450000), 
              "+":(450001,2500000), 
              "%":(0     ,0.005)}}
PKP = {
    "-":(0, 0       , 60000001 , 250000001, 500000001 , 5000000001),
    "+":(0, 60000000, 250000000, 500000000, 5000000000, 999999999999999),
    "~":(0, 60000000, 190000000, 250000000, 4500000000, 999999999999999),
    "%":(0, 0.05    , 0.15     , 0.25     , 0.3       , 0.35)}

# Input Frame
IK = {"f" : (0, 0, 4, 4, (10,(10,5)), (4,2), "g"),
      "t" : ("Informasi Karyawan", 0, 0, 4),
      "l" : [("PTKP",0,1), ("Jenis Penghitungan",2,1), ("Masa Penghasilan",0,3), ("Sampai dengan",2,3), ("Penghitungan",0,2)],
      "c" : [(["TK/0","TK/1","TK/2","TK/3","K/0","K/1","K/2","K/3"],1,1), (["Bulanan (Jan-Nov)","Final (Des)"],3,1), (["Setahun","Disetahunkan"],1,2), (["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"],1,3), (["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"],3,3)],
      "s" : [("Memiliki NPWP", 2, 2, ["off","on"]),("Gross-up",3,2, ["off","on"])]}
PH = {"f" : (4, 0, 7, 2, ((10,5),5),(6,1), "b"),
      "t" : ("Penghasilan", 0, 0, 2),
      "l" : [("Gaji Pokok",0,1), ("Bonus/THR",0,2), ("Lembur",0,3), ("Natura",0,4), ("Honorarium",0,5), ("Lainnya",0,6)],
      "e" : [("Masukkan Gaji",1,1), ("Masukkan Bonus/THR",1,2), ("Masukkan Lembur",1,3), ("Masukkan Natura",1,4), ("Masukkan Honorarium",1,5), ("Masukkan Ph. Lainnya",1,6)]}
KR = {"f" : (8, 1, 5, 2, ((5,10),5), (4,1), "c"),
      "t" : ("Pengurang", 0, 0, 2),
      "l" : [("Premi JP (%)",0,1), ("Premi JHT (%)",0,2), ("Premi Kes (%)",0,3), ("Denda/Pinalti",0,4)],
      "e" : [("1.0",1,1), ("2.0",1,2), ("1.0",1,3), ("Masukkan Denda/Pinalti",1,4)]}
PT = {"f" : (4, 1, 5, 2, ((5,10),5), (4,1), "c"),
      "t" : ("Tunjangan", 0, 0, 2),
      "l" : [("Tunj. Tetap",0,1), ("Premi JKK (%)",0,2), ("Premi JKM (%)",0,3), ("Premi Kes (%)",0,4)],
      "e" : [("Masukkan Tunj. Tetap",1,1), ("0.24",1,2), ("0.3",1,3), ("4.0",1,4)]}
PJ = {"f" : (10, 0, 2, 2, ((10,5),5), (2,1), "d"),
      "l" : [("Ph. Neto Sebelumnya",0,0), ("PPh 21 Terbayar",0,1)],
      "e" : [("Masukkan Ph. Neto Sebelumnya",1,0,1,"disable"), ("Masukkan PPh 21 Terbayar",1,1,1,"disable")]}
HS = {"f" : (12, 0,5, 4, (10,5), (4,2), "e"),
      "t" : ("Hasil", 0, 0, 4),
      "l" : [("Ph. Bruto Sebulan",0,1), ("Kategori (Tarif)",2,1), ("Tunjangan Pajak",0,2), ("PPh 21 Bulan ini",2,2), ("Pengurang",0,3), ("PPh Terutang",2,3), ("Gaji Bersih",0,4)],
      "e" : [("",1,1,1), ("",3,1,1), ("Masukkan Tunj. Pajak",1,2,1), ("",3,2,1), ("",1,3,1), ("",3,3,1), ("",1,4,3)]}
BT = {"f" : (16, 0, 1, 2, (20,(5,10)), (2,2), "f"),
      "i" : [(0,"left", "w"," Bersihkan", CTkImage(light_image=Image.open("assets/icon/reset.png"), dark_image=Image.open("assets/icon/reset_light.png"))),
             (1,"right", "e","Rincian ", CTkImage(light_image=Image.open("assets/icon/detail.png"), dark_image=Image.open("assets/icon/detail_light.png"))),
             (0,"left", "w"," Kembali", CTkImage(light_image=Image.open("assets/icon/back.png"), dark_image=Image.open("assets/icon/back_light.png")))]}

# Text
FONT = "Roboto"
TITLE_FS = 16
NORMAL_FS = 12
BUTTON_FS = 12

# Color
TITLE_BAR = {"dark":0x00000000, "light":0x00EEEEEE}
BLACK = "#000000"
WHITE = "#EEEEEE"
FRAME_COLOR = ("#d0d0d0","#181818")

# Methods
def num(data, comma:int=2, default:float=0.0):
    try:
        return round(float(data),ndigits=comma)
    except:
        return default
def toNum(num):
    return float(num.replace("Rp ","").replace(".","").replace(",","."))
def toRp(num):
    x = "Rp {:,.2f}".format(num).replace(",",".")
    a = x[:-3] + x[-3:].replace(".",",")
    return a[:4].replace("Rp -","-Rp ") + a[4:] if a[:4] == "Rp -" else a
def toKat(status="TK/0"): 
    return PTKP["k"][PTKP["s"].index(status)]
def getTer(bruto, status): #Output value int
    x = KATEGORI[toKat(status)]
    a = [x["%"][i] if x["-"][i] <=bruto and x["+"][i] >= bruto else 0 for i in range(len(x["-"]))]
    return sum(a)
def getPph(bruto:float, status, gross:int=0, npwp:int=0):
    a = bruto*getTer(bruto, status) if gross == 0 else bruto*getTer(bruto, status)/(1 - getTer(bruto, status))
    return a*1.2 if npwp == 0 else a
def getPkp(status, neto): # golongan =TK/0
    tarif = PTKP["t"][PTKP["s"].index(status)]
    x = max(neto - tarif, 0)
    return x
def masa(start,end):
    try: 
        a = IK["c"][3][0].index(start)
        b = IK["c"][4][0].index(end)
    except: 
        a = b = 0
    return len(range(a,b+1))
def temp(value,type:Literal["float", "int", "str"]="float"): 
    return DoubleVar(value=value) if type == "float" else IntVar(value=value) if type == "int" else StringVar(value=value)
def value(widget, value, state="normal"): 
    return widget.configure(state=state) if value==None else widget.configure(textvariable=StringVar(value=value), state=state)
def hasil(widget, value): 
    return widget.configure(textvariable=StringVar(value=value))
def text(widget,text): 
    return widget.configure(text=text)
def framing(frame, setting): 
    return frame.grid(column=setting[1], row=setting[0], rowspan= setting[5][0], columnspan=setting[5][1], sticky="nsew",padx=setting[4][0],pady=setting[4][1])
def pph21(pkp, pht, pph:tuple|list, duration, cond=(0,0,0)):#Cond=(npwp, gross, setahun)
    m = 50
    n = 0
    dif = 0.001
    ph = pht + pph[0]
    tp = 0
    lower = 0
    upper = sum([i[1] if (pkp - PKP["+"][i[0]])>0 else 200000 for i in [(0, 3000000), (1, 28500000), (2, 62500000), (3, 1350000000), (4, 300000000000)]])
    while n < m:
        try: 
            jbt = (duration*min(500000, 0.05*pht) if cond[0]==0 else ((duration - 1)*min(500000, 0.05*ph) + min(500000, 0.05*(pht + tp - pph[1] - (duration - 1)*pph[0]))))
        except:
            jbt = (duration*min(500000, 0.05*pht) if cond[0]==0 else ((duration - 1)*min(500000, 0.05*ph) + min(500000, 0.05*(pht + tp - pph[1] - (duration - 1)*pph[0]))))
        tp1 = tp
        x = pkp + (tp if cond[0]==1 else 0) - jbt
        r = (lower + upper)/2
        tp=0
        for i in range(len(PKP["+"])): 
            tp = tp + (min((x - PKP["+"][i-1]),PKP["~"][i])*PKP["%"][i] if (x - PKP["+"][i-1])>=0 else 0)
        tp = tp*(1 if cond[1]==1 else 1.2)*(1 if cond[2]==0 else duration/12)
        a = abs(tp - tp1)
        if a >= dif:
            if tp > r: 
                lower = r
            elif tp < r: 
                upper = r
            n += 1
        else: 
            break
    return tp
# Classes
class Frame(CTkFrame):
    def __init__(self, parent, frame, label:list|tuple=None, title=None, fg = FRAME_COLOR): 
        super().__init__(master=parent, fg_color=fg)# Settings
        self.grid(column=frame[1], row=frame[0], rowspan= frame[5][0], columnspan=frame[5][1], sticky="nsew",padx=frame[4][0],pady=frame[4][1])
        self.rowconfigure(tuple(range(frame[2])), weight=1, uniform=frame[6])
        self.columnconfigure(tuple(range(frame[3])), weight=1, uniform=frame[6])
    # Widgets
        try:
            [Label(self,i) for i in label]
            try:
                Title(self, title)
            except:
                pass
        except:
            pass
class Title(CTkLabel):
    def __init__(self, parent, data):
        super().__init__(master = parent, text = data[0], font = CTkFont(family=FONT,size=TITLE_FS,weight="bold"))
        self.grid(column = data[1], row = data[2], columnspan=data[3], sticky="nsew")
class Label(CTkLabel):
    def __init__(self, parent, data):
        super().__init__(master = parent, text = data[0], font = CTkFont(family=FONT,size=NORMAL_FS))
        self.grid(column = data[1], row = data[2], sticky="w", padx=5, pady=5)
class Entry(CTkEntry):
    def __init__(self, parent, data, var=None, trace_command=None, state="normal", vld=0):
        super().__init__(master = parent, placeholder_text=data[0], state=state, placeholder_text_color="grey", width=140, height=28)
        self.grid(column = data[1], row = data[2], sticky="e", padx=(5,10), pady=5)
        vcmd = (self.register(self.validation if vld==0 else self.validation_2), "%P")
        self.bind('<FocusIn>', lambda event: self.on_focus_in(variable=var,vcmd=vcmd))
        self.bind('<FocusOut>', lambda event: self.on_focus_out(text=data[0]))
        self.bind("<Key>", lambda event: self.on_focus_in(variable=var,vcmd=vcmd))
        if self.cget("state") == "normal":
            self.placeholder(text=data[0])
        if trace_command != None:
            try:
                for i in trace_command: var.trace_add("write",i)  
            except: 
                var.trace_add("write", trace_command)      
    def validation(self,P):
        if (P == ""):
            return True
        else:
            c=0
            i,j,k,l=1,1,1,1
            for x in P:
                if(i==2):
                    if(j==2):
                        if(k==1):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0' or x=='.'):
                                c+=1
                                if(x=='.'):
                                    k=2
                        elif(k==2):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0'):
                                c+=1
                    elif(j==1):
                        if(l==1):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0' or x=='.'):
                                c+=1
                                j=2
                                if(x=='.'):
                                    k=2
                        elif(l==2):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0'):
                                c+=1
                                j=2                        

                elif(i==1):
                    if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                    x=='8' or x=='9' or x=='0'):
                        c+=1
                        i=2
                    else:
                        return False
                else:
                    return False
            if(c==len(P) and float(P)<=9999999999 and float(P)>=0.0):
                return True
            else:
                return False
    def validation_2(self,P):
        if (P == ""):
            return True
        else:
            c=0
            i,j,k,l=1,1,1,1
            for x in P:
                if(i==2):
                    if(j==2):
                        if(k==1):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0' or x=='.'):
                                c+=1
                                if(x=='.'):
                                    k=2
                        elif(k==2):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0'):
                                c+=1
                    elif(j==1):
                        if(l==1):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0' or x=='.'):
                                c+=1
                                j=2
                                if(x=='.'):
                                    k=2
                        elif(l==2):
                            if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                            x=='8' or x=='9' or x=='0'):
                                c+=1
                                j=2                        

                elif(i==1):
                    if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or
                    x=='8' or x=='9' or x=='0'):
                        c+=1
                        i=2
                    else:
                        return False
                else:
                    return False
            if(c==len(P) and float(P)<=6 and float(P)>=0.0):
                return True
            else:
                return False
    def placeholder(self,text):
        self.configure(textvariable=StringVar(value=text), text_color="grey")
    def on_focus_in(self,variable,vcmd):
        self.configure(text_color=("black","white"))
        self.configure(validate="all", validatecommand = vcmd, textvariable=variable)
    def on_focus_out(self,text,*args):
        if self.cget("textvariable").get() == "" or self.cget("textvariable") == "":
            self.configure(validate=None)
            self.icursor(0)
            self.placeholder(text=text)
class Entry_2(CTkEntry):
    def __init__(self, parent, data, var=None, cmd=None):
        super().__init__(master = parent, state="disabled", justify="right", height=28, width=140*data[3]+int(data[3]/2), textvariable=var)
        self.grid(column = data[1], row = data[2], sticky = "e", columnspan=data[3], padx=(5,10), pady=5)
        if cmd != None:
            try:
                for i in cmd: 
                    var.trace_add("write",i)
            except: 
                var.trace_add("write", cmd)
class ComboBox(CTkComboBox):
    def __init__(self, parent, i, var=None, trace_command=None, state="normal"):
        super().__init__(master = parent, values= IK["c"][i][0], font=CTkFont(family=FONT,size=NORMAL_FS), variable=var, state=state)
        self.grid(column = IK["c"][i][1], row = IK["c"][i][2], padx=5, pady=5)
        if trace_command != None:
            try:
                for i in trace_command: 
                    var.trace_add("write",i)  
            except: 
                var.trace_add("write", trace_command) 
class Switch(CTkSwitch):
    def __init__(self, parent, i, var=None, trace_command=None):
        super().__init__(master=parent, font=CTkFont(family=FONT,size=NORMAL_FS), text=IK["s"][i][0], onvalue=IK["s"][i][3][1],offvalue=IK["s"][i][3][0], variable=var)
        self.grid(column=IK["s"][i][1], row=IK["s"][i][2], padx=5, pady=5)
        if trace_command != None:
            try:
                for cmd in trace_command: 
                    var.trace_add("write",cmd)  
            except: 
                var.trace_add("write", trace_command) 
class Label_Img(CTkLabel):
    def __init__(self, parent, data, cmd=None): 
        super().__init__(master=parent, fg_color="transparent", text=data[3], image=data[4], compound=data[1], font=CTkFont(family=FONT, size=BUTTON_FS, weight="bold"))
        self.grid(column=data[0], row = 0, sticky=data[2], padx=5, pady=5)
        self.bind("<Button-1>", cmd)

# Frame 2
class scrollFrame(CTkScrollableFrame): #w 555, h 640
    def __init__(self, parent, frame, row): 
        super().__init__(master=parent, fg_color=FRAME_COLOR, width=555, height=640)# Settings
        self.columnconfigure(tuple(range(1,6)), minsize=16)
        self.columnconfigure(tuple(range(6,9)), minsize=80)
        self.columnconfigure(tuple(range(9,12)), minsize=56)
        self.columnconfigure(0,minsize=7)
        self.columnconfigure(13, minsize=23)
        self.rowconfigure(tuple(range(row)), minsize=30)
        self.grid(column=frame[1], row=frame[0], rowspan= frame[3][0], columnspan=frame[3][1], sticky="nsew",padx=frame[2][0],pady=frame[2][1])
class Label2(CTkLabel):
    def __init__(self, parent, set, txt, row):
        super().__init__(master = parent, text = txt, font = CTkFont(family=FONT,size=NORMAL_FS))
        self.grid(column = set[0], row = row, columnspan = set[1], sticky = set[2], padx=5)

def conv(data, type:Literal["tab", "info"]="tab"):
    ik = data["ik"]
    ph = data["ph"]
    kr = data["kr"]
    pt = data["pt"]
    pj = data["pj"]
    hs = data["hs"]
    dt = data["dt"]
    x = []
    if type=="info": 
        x.append([0, "Informasi Personal Karyawan"])
        [x.append([4] + i) for i in [["Status", f":  {ik[0]}", "Penghitungan PPh", f":  {ik[1]}"], ["Kepemilikan NPWP", f":  {"YA" if ik[5]=="on" else "TIDAK"}", "Metode", f":  {"Gross-up" if ik[6]=="on" else "Gross"}"], ["Kategori", f":  {toKat(ik[0])[-1]}", "Tarif TER", f":  {round(dt[3]*100,2)}%"] if ik[1]!="Final (Des)" else ["Masa Penghasilan", f":  {dt[0]} bulan", "Metode Penghitungan", f":  {ik[2]}"]]]
    else:
        if ik[1]=="Bulanan (Jan-Nov)" :
            x.append([0, "Penghitungan PPh 21 dan Gaji Bersih"])
            x.append([1, "Penghasilan Tetap"])
            [x.append([2] + i[0]) if i[1]!=0.0 else None for i in [(["Gaji Pokok", "", toRp(ph[0])], ph[0]), (["Tunjangan Tetap", "", toRp(pt[0])], pt[0]), (["Premi JKK", f"{pt[1]}% x {toRp(ph[0])}", toRp(ph[0]/100*pt[1])], pt[1]), (["Premi JKM", f"{pt[2]}% x {toRp(ph[0])}", toRp(ph[0]/100*pt[2])], pt[2]), (["Premi Asuransi Kes", f"{pt[3]}% x {toRp(ph[0])}", toRp(ph[0]/100*pt[3])], pt[3]), (["Ph. Lainnya", "", toRp(ph[5])], ph[5])]]
            x.append([2, "Tunjangan Pajak", "", hs[2]]) if hs[2]!= "Rp 0,00" else None
            x.append([1, "Penghasilan Tidak Tetap"]) if dt[2]!=0 else None
            [x.append([2] + i[0]) if i[1]!=0.0 else None for i in [(["Bonus/THR", "", toRp(ph[1])], ph[1]), (["Lembur", "", toRp(ph[2])], ph[2]), (["Natura", "", toRp(ph[3])], ph[3]), (["Honorarium", "", toRp(ph[4])], ph[4])]]
            x.append([3, "Penghasilan Bruto", hs[0]])
            x.append([5, f"PPh 21 TER ({toKat(ik[0])[-1]})", f"{"" if ik[5]=="on" else "120% x "}{round(100*getTer(toNum(hs[0]), ik[0]), 2)}% x {hs[0]}", hs[3]])
            x.append([1, "Pengurang:"])
            [x.append([2] + i[0]) if i[1]!=0.0 else None for i in [(["PPh 21 Terutang", "", hs[5]], 1), (["Iuran Pensiun", f"{kr[0]}% x {toRp(ph[0])}", toRp(kr[0]*ph[0]/100)], kr[0]), (["Iuran Hari Tua", f"{kr[1]}% x {toRp(ph[0])}", toRp(kr[1]*ph[0]/100)], kr[1]), (["Iuran Asuransi Kes", f"{kr[2]}% x {toRp(ph[0])}", toRp(kr[2]*ph[0]/100)], kr[2]), (["Denda/Pinalti", "", toRp(kr[3])], kr[3])]]
            x.append([3, "Total Pengurang", toRp(toNum(hs[4]) + toNum(hs[5]))])
            x.append([6, "Gaji Bersih", hs[6]])
        else:
            x.append([0, f"Penghitungan PPh 21 Masa Terakhir ({ik[3][:3]} - {ik[4][:3]})"])
            x.append([1, "Penghasilan Bruto"])
            [x.append([2] + i[0]) if i[1]!=0 else None for i in [(["Penghasilan\nTetap", f"{dt[0]} x {toRp(dt[1])}", toRp(dt[0]*dt[1])], dt[1]), (["Penghasilan\nTidak Tetap", "", toRp(dt[2])], dt[2]), (["Ph. Neto\nSebelumnya", "", toRp(pj[0])], pj[0]), (["Tunjangan Pajak","", hs[3] if ik[6]=="on" else ""], 1 if ik[6]=="on" else 0)]]
            x.append([3,"Ph. Bruto Setahun",toRp(dt[0]*dt[1]+dt[2]+pj[0]+(dt[6] if ik[6]=="on" else 0))])
            x.append([5,f"Ph. Bruto\nDisetahunkan", f"12/{dt[0]} x {toRp(dt[0]*dt[1]+dt[2]+pj[0]+(dt[6] if ik[6]=="on" else dt[0]*toNum(hs[2])))}", toRp(12/dt[0]*(dt[0]*dt[1]+dt[2]+pj[0]+(dt[6] if ik[6]=="on" else dt[0]*toNum(hs[2]))))]) if ik[2]=="Disetahunkan" else None
            x.append([1, "Pengurang Ph. Bruto:"])
            [x.append([2]+i[0]) if i[1]!=0 else None for i in [(["Biaya Jabatan",f"{str(dt[0])+" x " if dt!=1 and ik[6]=="off" else str(dt[0]-1)+" x " if (dt[0]-1)!=0 else ""}5.0% x {toRp(dt[1] if ik[6]=="off" else (dt[1]+dt[5]) if (dt[0]-1)!=0 else toNum(hs[0]))}{"\n + 5% x "+hs[0] if ik[6]=="on" and dt[0]>1 else ""}", toRp(dt[4])], dt[4]),(["Iuran Pensiun",f"{str(dt[0])+" x " if dt!=1 else ""}{kr[0]}% x {toRp(ph[0])}",toRp(dt[0]/100*kr[0]*ph[0])],kr[0]),(["Iuran Hari Tua",f"{str(dt[0])+" x " if dt!=1 else ""}{kr[1]}% x {toRp(ph[0])}",toRp(dt[0]/100*kr[1]*ph[0])],kr[1])]]
            x.append([3, "Total Pengurang Ph. Bruto", toRp(dt[0]/100*kr[1]*ph[0]+dt[0]/100*kr[0]*ph[0]+dt[4])])
            x.append([5, f"Ph. Neto\n{ik[2]}", "(Ph. Bruto - Pengurang)", hs[1]])
            x.append([5, f"PKP ({ik[0]})", f"Ph. Neto - {toRp(PTKP["t"][PTKP["s"].index(ik[0])])}", toRp(getPkp(ik[0],toNum(hs[1])))])
            x.append([1, f"PPh 21 Setahun:"])
            a=getPkp(ik[0], toNum(hs[1]))
            b=0
            y=[["Tarif 1","5.0% x Rp 60.000.000,00","Rp 3.000.000,00"],["Tarif 2","15.0% x Rp 190.000.000,00","Rp 28.500.000,00"],["Tarif 3","25.0% x Rp 250.000.000,00","Rp 62.500.000,00"],["Tarif 4","30.0% x Rp 4.500.000.000,00","Rp 1.350.000.000,00"]]
            while a>=0: 
                a=a-PKP["~"][b]
            b+=1
            [x.append([2]+y[i]) for i in range(b-2 if (b-2)>=0 else 0)]
            x.append([2,f"Tarif {b-1}",f"{PKP["%"][b-1 if (b-1)>=0 else 0]*100}% x {toRp(getPkp(ik[0],toNum(hs[1]))-PKP["+"][b-2 if (b-2)>=0 else 0])}", toRp(PKP["%"][b-1 if (b-1)>=0 else 0]*(getPkp(ik[0],toNum(hs[1]))-PKP["+"][b-2 if (b-2)>=0 else 0]))])
            x.append([3, "Total PPh 21 Setahun", toRp(dt[6]/(1.2 if ik[5]=="off" else 1)*(12/dt[0] if ik[2]=="Disetahunkan" else 1))])
            x.append([2, "Tidak Memiliki\nNPWP", f"120% x {toRp(dt[6]/1.2*(12/dt[0] if ik[2]=="Disetahunkan" else 1))}", toRp(dt[6]*(12/dt[0] if ik[2]=="Disetahunkan" else 1))]) if ik[5]=="off" else None
            x.append([5, "PPh 21\nDisetahunkan", f"{dt[0]}/12 x {toRp(dt[6]*(12/dt[0] if ik[2]=="Disetahunkan" else 1))}", hs[3]]) if ik[2]=="Disetahunkan" else None
            x.append([1, "PPh Terbayar:"]) if dt[0]>1 else None
            x.append([2, "PPh Bulanan\nTerbayar", str(dt[0]-1)+" x "+toRp(dt[5]) if dt[0]>1 else "", toRp((dt[0]-1)*dt[5])]) if dt[0]>1 else None
            x.append([2, "PPh Terbayar\nPerusahaan\nSebelumnya", "", toRp(pj[1])]) if pj[1]!=0 else None
            x.append([3, "Total PPh Terbayar", toRp((dt[0]-1)*dt[5]+pj[1])]) if toRp((dt[0]-1)*dt[5]+pj[1])!=0 else None
            x.append([5, "PPh Bulan\nTerakhir", "", hs[5]])
            #Gaji Bersih
            x.append([0, f"Penghitungan Gaji Bersih Masa Terakhir ({ik[4]})"])
            x.append([1, "Penghasilan"])
            [x.append([2] + i[0]) if i[1]!=0.0 else None for i in [(["Gaji Pokok", "", toRp(ph[0])], ph[0]), (["Tunjangan Tetap", "", toRp(pt[0])], pt[0]), (["Premi JKK", f"{pt[1]}% x {toRp(ph[0])}", toRp(ph[0]/100*pt[1])], pt[1]), (["Premi JKM", f"{pt[2]}% x {toRp(ph[0])}", toRp(ph[0]/100*pt[2])], pt[2]), (["Premi Asuransi Kes", f"{pt[3]}% x {toRp(ph[0])}", toRp(ph[0]/100*pt[3])], pt[3]), (["Ph. Lainnya", "", toRp(ph[5])], ph[5])]]
            x.append([2, "Tunjangan Pajak", "", hs[2]]) if hs[2]!= "Rp 0,00" else None
            x.append([3, "Total Penghasilan", hs[0]])
            x.append([1, "Pengurang"])
            [x.append([2] + i[0]) if i[1]!=0.0 else None for i in [(["PPh 21 Terutang", "", hs[5]], 1), (["Iuran Pensiun", f"{kr[0]}% x {toRp(ph[0])}", toRp(kr[0]*ph[0]/100)], kr[0]), (["Iuran Hari Tua", f"{kr[1]}% x {toRp(ph[0])}", toRp(kr[1]*ph[0]/100)], kr[1]), (["Iuran Asuransi Kes", f"{kr[2]}% x {toRp(ph[0])}", toRp(kr[2]*ph[0]/100)], kr[2]), (["Denda/Pinalti", "", toRp(kr[3])], kr[3])]]
            x.append([3, "Total Pengurang", toRp(toNum(hs[4]) + toNum(hs[5]))])
            x.append([6, "Gaji Bersih", hs[6]])
    return x

def packedLabel(parent, data, row):
    if data[0] == 0: #title1
        Label2(parent, TAB["l"][0][0], data[1], row).configure(font = CTkFont(size = TITLE_FS, weight = "bold"))
    elif data[0] == 1: #title2
        Label2(parent, TAB["l"][0][1], data[1], row).configure(font = CTkFont(weight = "bold", underline = True))
    elif data[0] == 2: #point
        Label2(parent, TAB["l"][1][0], data[1], row)
        Label2(parent, TAB["l"][1][1], data[2], row)
        Label2(parent, TAB["l"][1][2], data[3], row)
    elif data[0] == 3: #result
        Label2(parent, TAB["l"][2][0], data[1], row).configure(font = CTkFont(weight = "bold"))
        Label2(parent, TAB["l"][2][1], data[2], row).configure(font = CTkFont(weight = "bold", underline = True))
    elif data[0] == 4: #info
        a=Label2(parent, INF["l"][0], data[1], row)
        a.grid(pady=5, padx=10)
        a.configure(font = CTkFont(weight = "bold", underline = True))
        b=Label2(parent, INF["l"][1], data[2], row)
        b.grid(pady=5, padx=10)
        c=Label2(parent, INF["l"][2], data[3], row)
        c.grid(pady=5, padx=10)
        c.configure(font = CTkFont(weight = "bold", underline = True))
        d=Label2(parent, INF["l"][3], data[4], row)
        d.grid(pady=5, padx=10)
    elif data[0] == 5: #highlight1
        a=Label2(parent, TAB["l"][3][0], data[1], row)
        a.configure(font=CTkFont(weight="bold", underline=True))
        a.grid(pady=10)
        b=Label2(parent, TAB["l"][3][1], data[2], row)
        b.grid(pady=10)
        c=Label2(parent, TAB["l"][3][2], data[3], row)
        c.configure(font=CTkFont(weight="bold", underline=True))
        c.grid(pady=10)
    elif data[0] == 6: #highlight1
        a= Label2(parent, TAB["l"][4][0], data[1], row)
        a.configure(font=CTkFont(size=TITLE_FS, weight="bold", underline=True))
        a.grid(pady=15)
        b= Label2(parent, TAB["l"][4][1], data[2], row)
        b.configure(font=CTkFont(size=TITLE_FS, weight="bold", underline=True))
        b.grid(pady=15)