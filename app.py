from customtkinter import CTk, set_appearance_mode
from assets.reference import *
import darkdetect
try:from ctypes import windll, byref, sizeof, c_int
except:pass

class App(CTk):
    def __init__(self, is_dark):
        # 0.0 Window setup
        super().__init__(fg_color=(WHITE,BLACK))
        self.title("PPh 21 TER 2024 (@rdwinr_)")
        self.iconbitmap('assets/icon/tax.ico')
        self.geometry("575x850")
        self.resizable(False,False)
        set_appearance_mode(f"{"dark" if is_dark else "light"}")
        self.title_color_bar(is_dark)
        # 1.0 Layout
        self.rowconfigure(tuple(range(17)), weight=1, uniform="a")
        self.columnconfigure((0,1), weight=1, uniform="a")
        # 2.0 Widget
        self.window1()
        self.frame1 = [self.ik, self.ph, self.pj, self.pt, self.kr, self.hs, self.op]
        # 3.0 Run
        self.mainloop()
# Appearance
    def title_color_bar(self,is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTR = 35
            COLOR = TITLE_BAR["dark"] if is_dark else TITLE_BAR["light"]
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTR, byref(c_int(COLOR)), sizeof(c_int))
        except:pass
    def window1(self):
        #Data
        self.i1=StringVar(); self.i2=StringVar(); self.i3=StringVar(); self.i4=StringVar(); self.i5=StringVar(); self.i6=StringVar(); self.i7=StringVar()
        self.p1=StringVar(); self.p2=StringVar(); self.p3=StringVar(); self.p4=StringVar(); self.p5=StringVar(); self.p6=StringVar()
        self.pj1=StringVar(); self.pj2=StringVar(); self.tp=StringVar()
        self.t1=StringVar(); self.t2=StringVar(); self.t3=StringVar(); self.t4=StringVar()
        self.m1=StringVar(); self.m2=StringVar(); self.m3=StringVar(); self.m4=StringVar()
        #Frame 1: Informasi
        self.ik=Frame(self,IK["f"],IK["l"],IK["t"])
        self.wi1=ComboBox(self.ik,0,self.i1,self.main_cmd)
        self.wi2=ComboBox(self.ik,1,self.i2,(self.act_cmd,self.main_cmd))
        self.wi3=ComboBox(self.ik,2,self.i3,(self.method_cmd,self.main_cmd),"disabled")
        self.wi4=ComboBox(self.ik,3,self.i4,(self.range_cmd,self.main_cmd),"disabled")
        self.wi5=ComboBox(self.ik,4,self.i5,self.main_cmd,"disabled")
        self.wi6=Switch(self.ik,0,self.i6,self.main_cmd)
        self.wi7=Switch(self.ik,1,self.i7,(self.gross_cmd,self.main_cmd))
        #Frame 2: Penghasilan
        self.ph=Frame(self,PH["f"],PH["l"],PH["t"])
        self.wp1=Entry(self.ph,PH["e"][0],self.p1,self.main_cmd)
        self.wp2=Entry(self.ph,PH["e"][1],self.p2,self.main_cmd)
        self.wp3=Entry(self.ph,PH["e"][2],self.p3,self.main_cmd)
        self.wp4=Entry(self.ph,PH["e"][3],self.p4,self.main_cmd)
        self.wp5=Entry(self.ph,PH["e"][4],self.p5,self.main_cmd)
        self.wp6=Entry(self.ph,PH["e"][5],self.p6,self.main_cmd)
        #Frame 3: Pajak Sebelumnya
        self.pj=Frame(self,PJ["f"],PJ["l"])
        self.wpj1=Entry(self.pj,PJ["e"][0],self.pj1,self.main_cmd,"disable")
        self.wpj2=Entry(self.pj,PJ["e"][1],self.pj2,self.main_cmd,"disable")
        #Frame 4: Tunjangan
        self.pt=Frame(self,PT["f"],PT["l"],PT["t"])
        self.wt1=Entry(self.pt,PT["e"][0],self.t1,self.main_cmd)
        self.wt2=Entry(self.pt,PT["e"][1],self.t2,self.main_cmd,vld=1)
        self.wt3=Entry(self.pt,PT["e"][2],self.t3,self.main_cmd,vld=1)
        self.wt4=Entry(self.pt,PT["e"][3],self.t4,self.main_cmd,vld=1)
        #Frame 5: Pengurang
        self.kr=Frame(self,KR["f"],KR["l"],KR["t"])
        self.wm1=Entry(self.kr,KR["e"][0],self.m1,self.main_cmd,vld=1)
        self.wm2=Entry(self.kr,KR["e"][1],self.m2,self.main_cmd,vld=1)
        self.wm3=Entry(self.kr,KR["e"][2],self.m3,self.main_cmd,vld=1)
        self.wm4=Entry(self.kr,KR["e"][3],self.m4,self.main_cmd)
        #Frame 6: Hasil
        self.hs=Frame(self,HS["f"],title=HS["t"])
        #Label
        self.lh1=Label(self.hs,HS["l"][0])
        self.lh2=Label(self.hs,HS["l"][1])
        self.lh3=Label(self.hs,HS["l"][2])
        self.lh4=Label(self.hs,HS["l"][3])
        self.lh5=Label(self.hs,HS["l"][4])
        self.lh6=Label(self.hs,HS["l"][5])
        self.lh7=Label(self.hs,HS["l"][6])
        #Entry
        self.wh1=Entry_2(self.hs,HS["e"][0])
        self.wh2=Entry_2(self.hs,HS["e"][1])
        self.wh4=Entry_2(self.hs,HS["e"][3])
        self.wh5=Entry_2(self.hs,HS["e"][4])
        self.wh6=Entry_2(self.hs,HS["e"][5])
        self.wh7=Entry_2(self.hs,HS["e"][6])
        self.wh3 = Entry(self.hs, HS["e"][2], self.tp, self.main_cmd)
        #Frame 7: Navigasi
        self.op=Frame(self,BT["f"],fg="transparent")
        Label_Img(self.op,BT["i"][0],self.clear_cmd)
        Label_Img(self.op,BT["i"][1],self.detail_cmd)
    def window2(self, data):
        #Frame 1: Informasi
        x=conv(data,"info")
        self.ik2=Frame(self,INF["f"])
        [packedLabel(self.ik2,x[i],i) for i in range(len(x))]
        #Frame 2: Slip
        x=conv(data)
        self.tab1=scrollFrame(self,TAB["f"],len(x))
        [packedLabel(self.tab1,x[i],i) for i in range(len(x))]
        #Frame 3: Navigasi
        self.op1=Frame(self,BT["f"],fg="transparent")
        Label_Img(self.op1,BT["i"][2],self.home_cmd)
# Function: Trace
    def method_cmd(self, *args):
        if self.wi3.cget("state") == "normal" and self.i3.get() == "Setahun":
            text(self.lh2, "Ph. Neto Setahun")
            self.wpj1= Entry(self.pj, PJ["e"][0], self.pj1, self.main_cmd)
            self.wpj2= Entry(self.pj, PJ["e"][1], self.pj2, self.main_cmd)
            self.pj1.set("")
            self.pj2.set("")
            if self.i4.get() == "Januari": 
                self.wpj1= Entry(self.pj, PJ["e"][0], self.pj1, self.main_cmd, "disable")
                self.wpj2= Entry(self.pj, PJ["e"][1], self.pj2, self.main_cmd, "disable")
        elif self.i3.get() == "Disetahunkan" or self.wi4.cget("state")=="disabled":
            for widget in [self.wpj1, self.wpj2]:
                widget.delete(0,"end")
                value(widget,None,"disable")
            text(self.lh2, "Ph. Neto Disetahunkan")
            self.pj1.set("")
            self.pj2.set("")
        else: 
            self.wpj1= Entry(self.pj, PJ["e"][0], self.pj1, self.main_cmd, "disable")
            self.wpj2= Entry(self.pj, PJ["e"][1], self.pj2, self.main_cmd, "disable")
    def gross_cmd(self, *args):
        if self.wi7.get() == "on": 
            self.wh3 = Entry_2(self.hs, HS["e"][2])
            self.wh3.configure(text_color="grey")
            self.tp.set("")
        else: 
            self.wh3 = Entry(self.hs, HS["e"][2], self.tp, self.main_cmd)
    def range_cmd(self, *args):
        index = IK["c"][3][0].index(self.i4.get() if self.i4.get()!="" else "Januari")
        self.wi5.configure(state="normal", values=IK["c"][4][0][index:]) if self.wi4.cget("state")=="normal" else self.wi5.configure(state="normal")
        if self.i4.get() == "Januari" or self.i3.get() == "Disetahunkan": 
            self.wpj1= Entry(self.pj, PJ["e"][0], self.pj1, self.main_cmd, "disable")
            self.wpj2= Entry(self.pj, PJ["e"][1], self.pj2, self.main_cmd, "disable")
            self.pj1.set("")
            self.pj2.set("")
    def act_cmd(self, *args):
        if self.wi2.get()=="Bulanan (Jan-Nov)": 
            [i.set("") for i in [self.i3, self.i4, self.i5, self.pj1, self.pj2]]
            [value(i,None,"disabled") for i in [self.wi3, self.wi4, self.wi5]]
            [text(i[1],i[0]) for i in [("Ph. Bruto Sebulan", self.lh1), ("Kategori (Tarif)", self.lh2), ("PPh 21 Bulan ini", self.lh4), ("PPh Terutang", self.lh6)]]
            for i in [("Masukkan Bonus/THR", self.wp2), ("Masukkan Lembur", self.wp3), ("Masukkan Natura", self.wp4), ("Masukkan Honorarium", self.wp5), ("Masukkan Denda/Pinalti", self.wm4)]: 
                i[1].delete(0, "end")
                value(i[1],i[0])
                i[1].configure(text_color="grey")
        elif self.wi2.get()=="Final (Des)":
            [value(i, None) for i in [self.wi3, self.wi4]]; [text(i[1],i[0]) for i in [("Ph. Bruto Bulan Ini", self.lh1), ("Ph. Neto Setahun", self.lh2),("PPh 21 Setahun", self.lh4), ("PPh 21 Bulan Ini", self.lh6)]]
            self.wpj1= Entry(self.pj, PJ["e"][0], self.pj1, self.main_cmd)
            self.wpj2= Entry(self.pj, PJ["e"][1], self.pj2, self.main_cmd)
            for i in [(self.wp2, self.p2), (self.wp3, self.p3), (self.wp4, self.p4), (self.wp5, self.p5), (self.wm4, self.m4)]:
                i[0].delete(0,"end")
                value(i[0],None,"disable")
                i[1].set("")
    def main_cmd(self, *args):
        #Kalkulasi
        self.ph1 = temp(sum([num(i.get()) for i in [self.p1, self.p6, self.t1, self.tp]]) + sum([num(i[0].get()) if i[0].get()!="" else i[1] for i in [(self.t2, 0.24),(self.t3, 0.3),(self.t4, 4.0)]])/100*num(self.p1.get()))
        self.ph2 = temp(sum([num(i.get()) for i in [self.p2, self.p3, self.p4, self.p5]]))
        npwp = temp(1 if self.i6.get()=="on" else 0,"int")
        gros = temp(1 if self.i7.get()=="on" else 0,"int")
        stat = temp(self.i1.get() if self.i1.get()!="" else "TK/0","str")
        seth = temp(0 if self.i3.get()!="Disetahunkan" else 1,"int")
        self.tp1 = temp(getPph(self.ph1.get() + self.ph2.get(), stat.get(), gros.get(), npwp.get()))
        self.tp2 = temp(getPph(self.ph1.get(), stat.get(), gros.get(), npwp.get()))
        brt = temp(self.ph1.get() + self.ph2.get() + (self.tp1.get() if gros.get()==1 else 0))
        krg = temp(num(self.m4.get()) + sum([num(i[0].get()) if i[0].get()!="" else i[1] for i in [(self.m1,1),(self.m2,2),(self.m3,1)]])/100*num(self.p1.get()))
        self.ter = temp(getTer(brt.get(), stat.get()))
        self.rng = temp(masa(self.i4.get(), self.i5.get()), type= "int")
        pen = temp((num(self.m1.get()) if self.m1.get()!="" else 1)/100*num(self.p1.get())*self.rng.get())
        jht = temp((num(self.m2.get()) if self.m2.get()!="" else 2)/100*num(self.p1.get())*self.rng.get())
        nto = temp((self.ph1.get()*self.rng.get() + num(self.pj1.get()))*(1 if seth.get()==0 else 12/self.rng.get()) - pen.get() - jht.get())
        self.pkp = temp(getPkp(stat.get(), nto.get()))
        self.pph21 = temp(pph21(self.pkp.get(), self.ph1.get(), (self.tp2.get(), num(self.pj2.get())), self.rng.get(), (gros.get(), npwp.get(), seth.get())))
        self.pjf = temp(self.pph21.get() - (self.rng.get() - 1)*self.tp2.get() - num(self.pj2.get()) - (self.rng.get() - 1)*num(self.tp.get()))
        self.jbt = temp(self.rng.get()*min(500000, 0.05*self.ph1.get()) if self.i7.get()=="off" else ((self.rng.get() - 1)*min(500000, 0.05*(self.ph1.get() + self.tp2.get())) + min(500000, 0.05*(self.ph1.get() + self.pjf.get()))))
        #Entry Hasil
        hasil(self.wh1, toRp(brt.get()))
        hasil(self.wh2, f"{toKat(stat.get())} ({round(self.ter.get()*100,2)}%)")
        None if gros.get()==0 else hasil(self.wh3, toRp(self.tp1.get()))
        hasil(self.wh4, toRp(self.tp1.get()))
        hasil(self.wh5, toRp(krg.get()))
        hasil(self.wh6, toRp(self.tp1.get() - (self.tp1.get() if gros.get()==1 else num(self.tp.get()))))
        hasil(self.wh7, toRp(brt.get() - (krg.get() + (toNum(self.wh6.get()) if gros.get()==0 else self.tp1.get()))))
        [hasil(i,"") for i in [self.wh1, self.wh2, self.wh4, self.wh5, self.wh6, self.wh7]] if brt.get() == 0.0 else None
        if self.i2.get() == "Final (Des)": 
            hasil(self.wh1, toRp(self.ph1.get() + (0 if gros.get()==0 else self.pjf.get())))
            hasil(self.wh2, toRp(nto.get() - self.jbt.get() + (0 if gros.get()==0 else self.pph21.get())*(12/self.rng.get() if seth.get()==1 else 1)))
            None if gros.get()==0 else hasil(self.wh3, toRp(self.pjf.get()))
            hasil(self.wh4, toRp(self.pph21.get()))
            hasil(self.wh5, toRp(krg.get()))
            hasil(self.wh6, toRp(self.pjf.get()))
            hasil(self.wh7, toRp(toNum(self.wh1.get()) - krg.get() - toNum(self.wh6.get())))
            [hasil(i,"") for i in [self.wh1,self.wh2,self.wh4,self.wh5,self.wh6,self.wh7]] if nto.get() == 0.0 else None
# Function: Button
    def clear_cmd(self, *args):
        entry = [("Masukkan Gaji", self.wp1), ("Masukkan Bonus/THR", self.wp2), ("Masukkan Lembur", self.wp3), ("Masukkan Natura", self.wp4), ("Masukkan Honorarium", self.wp5), ("Masukkan Ph. Lainnya", self.wp6), ("1.0", self.wm1), ("2.0", self.wm2), ("1.0", self.wm3), ("Masukkan Denda/Pinalti", self.wm4), ("Masukkan Tunj. Tetap", self.wt1), ("0.24", self.wt2), ("0.3", self.wt3), ("4.0", self.wt4), ("Masukkan Tunj. Pajak", self.wh3)]
        for i in entry:
            i[1].delete(0, "end")
            value(i[1], i[0])
            i[1].configure(text_color="grey")
        info = {"":(self.i1, self.i2, self.i3, self.i4, self.i5, self.pj1, self.pj2), "off":(self.i6, self.i7)}
        for i, j in info.items():
            [k.set(i) if k.get() != "" or k.get() != "off" else None for k in j]
        self.wpj1= Entry_2(self.pj, PJ["e"][1])
        self.wpj2= Entry_2(self.pj, PJ["e"][2])
        [text(i[1],i[0]) for i in [("Ph. Bruto Sebulan", self.lh1), ("Kategori (Tarif)", self.lh2), ("PPh 21 Bulan ini", self.lh4), ("PPh Terutang", self.lh6)]]
        [hasil(i,"") for i in [self.wh1, self.wh2, self.wh4, self.wh5, self.wh6, self.wh7]]

    def detail_cmd(self, *args):
        global data
        data = {"ik": [i[0].get() if i[0].get()!="" else i[1] for i in [(self.i1, "TK/0"),(self.i2, "Bulanan (Jan-Nov)"),(self.i3,"Setahun"),(self.i4, "Januari"),(self.i5, self.i4.get() if self.i4.get()!="" else "Januari"),(self.i6,"off"),(self.i7,"off")]],
                "ph": [num(i.get()) if i.get()!= "" else 0.0 for i in [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]],
                "kr": [num(i[0].get()) if i[0].get()!= "" else i[1] for i in [(self.m1,1.0),(self.m2,2.0),(self.m3,1.0),(self.m4,0.0)]],
                "pt": [num(i[0].get()) if i[0].get()!= "" else i[1] for i in [(self.t1,0.0),(self.t2,0.24),(self.t3,0.3),(self.t4,4.0)]],
                "pj": [num(i.get()) if i.get()!= "" else 0.0 for i in [self.pj1, self.pj2]],
                "hs": [i if i!= "" else "Rp 0,00" for i in [self.wh1.get(), self.wh2.get(), toRp(num(self.wh3.get())) if self.i7.get()!="on" else self.wh3.get(), self.wh4.get(), self.wh5.get(), self.wh6.get(), self.wh7.get()]],
                "dt": [self.rng.get(), self.ph1.get(), self.ph2.get(), self.ter.get(), self.jbt.get(), self.tp2.get(), self.pph21.get()]}
        [i.grid_forget() for i in self.frame1]
        self.window2(data)
        self.frame2 = [self.ik2,self.tab1, self.op1]
    def home_cmd(self, *args):
        setting = (IK["f"], PH["f"], PJ["f"], PT["f"], KR["f"], HS["f"], BT["f"])
        [framing(self.frame1[i], setting[i]) for i in range(len(self.frame1))]
        [i.grid_forget() for i in self.frame2]
App(darkdetect.isDark())