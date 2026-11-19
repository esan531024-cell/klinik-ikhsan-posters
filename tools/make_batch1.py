from PIL import Image, ImageDraw, ImageFont
import textwrap
W,H=1080,1920
F="/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf"
def f(w,s):
    w={"ExtraBold":"Bold","SemiBold":"Medium"}.get(w,w)
    return ImageFont.truetype(F%w,s)
TEAL=(0,121,128); DARK=(6,52,58); YEL=(255,200,40); WHITE=(255,255,255); RED=(214,40,57); LIGHT=(232,246,246)
posters=[
 dict(tag="MITOS atau FAKTA?",stamp="MITOS",head="Berpeluh banyak = lemak terbakar?",body="Peluh hanya cara badan mengawal suhu. Ia bukan ukuran lemak yang terbakar.",tips=["Minum air secukupnya","Bergerak 30 minit, 5 hari seminggu","Tidur cukup setiap malam"]),
 dict(tag="TAHUKAH ANDA?",stamp="FAKTA",head="Tekanan darah tinggi sering tiada simptom",body="Ramai tidak sedar sehingga membuat pemeriksaan. Semak tekanan darah secara berkala.",tips=["Kurangkan garam","Bergerak aktif setiap hari","Semak tekanan darah di klinik"]),
 dict(tag="MITOS atau FAKTA?",stamp="MITOS",head="Demam mesti makan antibiotik?",body="Kebanyakan demam disebabkan virus dan antibiotik tidak membantu. Jumpa doktor untuk penilaian.",tips=["Rehat & banyak minum air","Pantau suhu badan","Jumpa doktor jika demam lebih 3 hari"]),
 dict(tag="TAHUKAH ANDA?",stamp="FAKTA",head="Cuci tangan 20 saat boleh kurangkan jangkitan",body="Cuci dengan sabun dan air mengalir, terutama sebelum makan dan selepas ke tandas.",tips=["Basahkan & sabun tangan","Gosok 20 saat","Bilas & keringkan"]),
 dict(tag="TIP KESIHATAN",stamp="TIP",head="Gula darah: bila perlu disemak?",body="Semakan berkala membantu mengesan masalah lebih awal, terutama jika ada sejarah keluarga.",tips=["Umur 30 tahun ke atas","Ada sejarah keluarga diabetes","Berat badan berlebihan"]),
 dict(tag="MITOS atau FAKTA?",stamp="MITOS",head="Sakit belakang? Rehat total paling baik?",body="Bergerak ringan biasanya lebih membantu daripada berbaring lama. Teruk atau berpanjangan? Jumpa doktor.",tips=["Kekal bergerak ringan","Postur duduk yang betul","Jangan angkat berat tiba-tiba"]),
 dict(tag="TAHUKAH ANDA?",stamp="FAKTA",head="Tidur 7-9 jam penting untuk orang dewasa",body="Tidur yang cukup membantu tumpuan, mood dan daya tahan badan.",tips=["Waktu tidur tetap","Kurangkan skrin sebelum tidur","Elak kafein lewat petang"]),
]
def center(d,text,font,y,fill,maxw=900,lh=1.25):
    lines=[]
    for para in text.split("\n"):
        cur=""
        for w in para.split():
            t=(cur+" "+w).strip()
            if d.textlength(t,font=font)<=maxw: cur=t
            else: lines.append(cur); cur=w
        lines.append(cur)
    for l in lines:
        d.text(((W-d.textlength(l,font=font))/2,y),l,font=font,fill=fill); y+=int(font.size*lh)
    return y
for i,p in enumerate(posters,1):
    im=Image.new("RGB",(W,H),TEAL); d=ImageDraw.Draw(im)
    d.ellipse((-300,-300,500,500),fill=(0,98,105)); d.ellipse((700,1100,1500,1900),fill=(0,98,105))
    # safe zones: keep content y 170..1650
    d.rounded_rectangle((60,190,1020,1560),radius=48,fill=WHITE)
    tw=d.textlength(p["tag"],font=f("Bold",44)); d.rounded_rectangle((540-tw/2-36,230,540+tw/2+36,310),radius=40,fill=YEL)
    d.text((540-tw/2,236),p["tag"],font=f("Bold",44),fill=DARK)
    y=center(d,p["head"],f("ExtraBold",78),360,DARK,maxw=860,lh=1.15)
    # stamp
    st=Image.new("RGBA",(420,150),(0,0,0,0)); sd=ImageDraw.Draw(st)
    col=RED if p["stamp"]=="MITOS" else (20,150,90)
    sd.rounded_rectangle((4,4,416,146),radius=18,outline=col,width=10); sd.text((210-sd.textlength(p["stamp"],font=f("ExtraBold",92))/2,10),p["stamp"],font=f("ExtraBold",92),fill=col)
    st=st.rotate(-6,expand=True,resample=Image.BICUBIC); im.paste(st,(330,y+10),st); d=ImageDraw.Draw(im)
    y=center(d,p["body"],f("Medium",42),y+210,(40,60,64),maxw=860,lh=1.35)+20
    for k,t in enumerate(p["tips"],1):
        d.rounded_rectangle((110,y,970,y+110),radius=28,fill=LIGHT)
        d.ellipse((130,y+17,206,y+93),fill=TEAL); d.text((168-d.textlength(str(k),font=f("Bold",44))/2,y+22),str(k),font=f("Bold",44),fill=WHITE)
        d.text((232,y+30),t,font=f("SemiBold",36),fill=DARK) if d.textlength(t,font=f("SemiBold",36))<720 else d.text((232,y+34),t,font=f("SemiBold",30),fill=DARK)
        y+=130
    d.text((540-d.textlength("Klinik Ikhsan Chendor",font=f("ExtraBold",46))/2,1380),"Klinik Ikhsan Chendor",font=f("ExtraBold",46),fill=TEAL)
    s="Walk-in 8pg-10mlm setiap hari  |  WhatsApp 011-6058 1625"
    d.text((540-d.textlength(s,font=f("Medium",29))/2,1445),s,font=f("Medium",29),fill=DARK)
    s2="Bandar Baru Chendor, Kuantan  |  klinikikhsan.com"
    d.text((540-d.textlength(s2,font=f("Medium",29))/2,1488),s2,font=f("Medium",29),fill=DARK)
    d.text((540-d.textlength("Maklumat am sahaja, bukan pengganti nasihat doktor.",font=f("Regular",26))/2,1600),"Maklumat am sahaja, bukan pengganti nasihat doktor.",font=f("Regular",26),fill=WHITE)
    im.save(f"posters/poster{i}.png")
