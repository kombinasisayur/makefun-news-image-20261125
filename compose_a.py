#!/usr/bin/env python3
# THE CONTINENTAL - NI25 Akun 16 - Variant A (lead trio top, grid 5x2)
import os
from PIL import Image, ImageDraw, ImageFont
W=1024; H=1024
RICE=(243,236,216); INK=(18,18,16); GREEN=(20,83,45); DGREEN=(13,54,30); LGREEN=(46,125,72)
GOLD=(176,141,62); WHITE=(250,248,240); GREY=(90,88,80)
FD="/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
def font(names,size):
    for n in names:
        p=FD+n
        if os.path.exists(p):
            try: return ImageFont.truetype(p,size)
            except Exception: pass
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(p): return ImageFont.truetype(p,size)
    return ImageFont.load_default()
def FB(s): return font(["PlayfairDisplay-Black.ttf","Playfair-Black.ttf","PlayfairDisplay-Bold.ttf"],s)
def FBD(s): return font(["DejaVuSans-Bold.ttf"],s)
def FR(s): return font(["DejaVuSans.ttf"],s)
img=Image.new("RGB",(W,H),RICE); d=ImageDraw.Draw(img)
import random as _r
_r.seed(16)
for _ in range(45000):
    _px=_r.randint(0,W-1); _py=_r.randint(0,H-1)
    d.point((_px,_py),fill=(226,216,188) if _r.random()<0.5 else (214,204,172))
def rect(x,y,w,h,fill=None,outline=None,width=1):
    d.rectangle([x,y,x+w,y+h],fill=fill,outline=outline,width=width)
def txt(x,y,s,f,fill=INK,anchor=None):
    d.text((x,y),s,font=f,fill=fill,anchor=anchor)
def wrap(s,f,maxw):
    out=[]; cur=""
    for w_ in s.split():
        t=(cur+" "+w_).strip()
        if d.textlength(t,font=f)<=maxw: cur=t
        else:
            if cur: out.append(cur)
            cur=w_
    if cur: out.append(cur)
    return out
def scene(x,y,w,h,kind,seed):
    # layered flat illustration, clipped to the strip via an offscreen layer
    global d
    _saved=d; _layer=Image.new("RGB",(W,H),RICE); d=ImageDraw.Draw(_layer)
    skies=[(198,224,205),(210,228,214),(188,216,196)]
    sky=skies[seed%3]; rect(x,y,w,h,fill=sky)
    d.ellipse([x+w-34,y+6,x+w-10,y+30],fill=(240,205,90))
    gy=y+h-18; rect(x,gy,w,18,fill=(120,150,110))
    cx=x+w//2
    if kind=="ship":
        d.polygon([(x+18,gy-8),(x+w-18,gy-8),(x+w-34,gy+6),(x+30,gy+6)],fill=(30,30,30))
        rect(cx-26,gy-26,52,16,fill=(200,60,50)); rect(cx-6,gy-38,12,12,fill=GREY)
        for i in range(3): d.ellipse([x+22+i*36,gy+2,x+34+i*36,gy+12],outline=INK,width=2)
    elif kind=="chart":
        for i,v in enumerate([14,24,36,48]):
            rect(x+22+i*30,gy-v,18,v,fill=GREEN if i<3 else (200,60,50))
        d.line([x+14,gy-52,x+w-14,gy-52],fill=INK,width=2)
    elif kind=="eu":
        for i in range(6):
            import math; a=i/6*6.283; sx=cx+int(22*math.cos(a)); sy=y+26+int(14*math.sin(a))
            d.polygon([(sx,sy-5),(sx+2,sy+2),(sx-2,sy+2)],fill=GOLD)
        d.ellipse([cx-10,y+16,cx+10,y+36],outline=GREEN,width=3)
    elif kind=="plane":
        d.polygon([(cx-42,gy-22),(cx+30,gy-22),(cx+46,gy-14),(cx+30,gy-10),(cx-30,gy-10)],fill=(70,80,90))
        d.polygon([(cx+18,gy-22),(cx+34,gy-36),(cx+42,gy-22)],fill=(50,60,70))
    elif kind=="oil":
        for ox in [x+26,cx,x+w-44]:
            d.line([ox,gy,ox,gy-34],fill=INK,width=4); d.line([ox,gy-34,ox+16,gy-22],fill=INK,width=3)
        rect(x+14,gy-10,w-28,8,fill=(90,70,40))
    elif kind=="bomb":
        rect(cx-28,gy-30,56,28,fill=(160,50,40)); rect(cx-28,gy-30,56,8,fill=(90,30,25))
        for dx in (-14,12): d.ellipse([cx+dx,gy-14,cx+dx+10,gy-4],fill=INK)
        d.polygon([(x+16,y+10),(x+28,y+22),(x+16,y+34),(x+10,y+22)],fill=(240,180,60))
    elif kind=="coral":
        for i in range(5):
            bx=x+20+i*((w-40)//4); d.line([bx,gy,bx,gy-16-(i%3)*6],fill=(220,110,90),width=4)
            d.line([bx,gy-12,bx-8,gy-20],fill=(220,110,90),width=3); d.line([bx,gy-12,bx+8,gy-22],fill=(240,140,110),width=3)
    elif kind=="flag":
        rect(cx-30,gy-38,60,26,fill=(240,200,60)); rect(cx-30,gy-38,60,9,fill=GREEN); rect(cx-30,gy-21,60,9,fill=(200,50,50))
        d.line([cx-30,gy,cx-30,gy-44],fill=INK,width=3)
    elif kind=="hands":
        d.ellipse([cx-34,gy-36,cx-10,gy-12],fill=(210,170,130)); d.ellipse([cx+10,gy-36,cx+34,gy-12],fill=(180,140,100))
        rect(cx-14,gy-18,28,10,fill=WHITE,outline=INK)
    elif kind=="chip":
        rect(cx-30,gy-36,60,30,fill=DGREEN,outline=GOLD,width=2)
        for i in range(4): d.line([cx-20+i*12,gy-30,cx-20+i*12,gy-12],fill=GOLD,width=2)
    elif kind=="graph":
        pts=[(x+16,gy-8),(x+40,gy-20),(x+64,gy-14),(x+88,gy-30),(x+w-16,gy-36)]
        d.line(pts,fill=(200,50,40),width=3)
        for px,py in pts: d.ellipse([px-3,py-3,px+3,py+3],fill=INK)
    else:
        d.polygon([(x+14,gy),(cx, y+12),(x+w-14,gy)],fill=LGREEN)
    img.paste(_layer.crop((x,y,x+w,y+h)),(x,y)); d=_saved
    rect(x,y,w,h,outline=INK,width=1)
# ---------- header ----------
txt(512,8,"37 STORIES - EVERY ONE DATED - 9 REGIONS - TUESDAY'S WORLD ON ONE PAGE",FBD(13),GREEN,"ma")
txt(512,26,"THE CONTINENTAL",FB(58),INK,"ma")
rect(16,92,992,3,fill=GREEN); rect(16,98,992,1,fill=INK)
txt(512,102,"TUESDAY 25 NOVEMBER 2026",FB(44),DGREEN,"ma")
rect(16,152,992,2,fill=INK)
# numbers strip
nums=[("3","TANKERS HIT - IRAN SAYS #2"),("700,000+","RUSSIAN DEAD #6"),("50","BOEING 737-8 JETS #10"),("12","CORAL SPECIES BACK #13"),("23","INJURED, COLOMBIA #8"),("+31.5%","NVIDIA MONDAY #36")]
rect(16,158,992,34,fill=DGREEN)
x=24
for v,l in nums:
    txt(x,163,v,FBD(15),WHITE); txt(x,180,l,FR(7),WHITE); x+= 164 if len(v)<7 else 172
# region strip
regs=[("EUROPE",GREEN),("MIDDLE EAST",(170,80,30)),("AFRICA",(150,110,20)),("AMERICAS",(40,90,160)),("ASIA",(170,50,80)),("SOUTH ASIA",(110,60,160)),("ASIA-PACIFIC",(20,130,130)),("OCEANIA",(60,140,60)),("WORLD",INK)]
x=16; y=196
for name,c in regs:
    w_=992//9; rect(x,y,w_-2,20,fill=c); txt(x+w_//2,y+5,name,FBD(8),WHITE,"ma"); x+=w_
# timeline
txt(16,220,"THE DAY IN ORDER:",FBD(9),GREEN)
tl="22 NOV gas rationing began in Iran (#16 brief)  -  MONDAY CLOSE Nvidia +31.5% (#36)  -  TUESDAY PCE report due today (#33)  -  TUESDAY Madrid 5-1 PSV (#11 brief)  -  AHEAD Thanksgiving travel storms (#37 brief)  -  2027 Punjab alliance announced (#23)"
for i,ln in enumerate(wrap(tl,FR(8),980)): txt(16,232+i*11,ln,FR(8),INK)
# ---------- cards ----------
LEADS=[
 (2,"MIDDLE EAST - SEA","Strait of Hormuz","Iran says 3 tankers hit by mines","IRGC Navy claims three oil tankers were hit by naval mines in the Strait of Hormuz. Shipping concerns rise as the claim spreads. The claim is labelled CLAIMED on this page - it is Iran's account, reported as such, not confirmed fact.","3 TANKERS HIT - IRAN SAYS","Iranian claim via wires - CLAIMED","ship"),
 (6,"WORLD - WAR DATA","Ukraine war","700,000 Russian dead, new count finds","New analysis finds more than 700,000 Russian soldiers killed - 700000 in all - in the nearly five-year war on Ukraine. RFE/RL reports the count as a new analysis published on Tuesday, the largest single figure on this page.","700,000+ KILLED","RFE/RL - REPORTED","chart"),
 (5,"EUROPE - DIPLOMACY","Brussels","EU unveils new Russia sanctions","The European Union announced further restrictive measures and new sanctions against Russia amid the war in Ukraine. Brussels acts on the same day NATO moves early-warning jets to Poland - card 1 on this page.","NEW EU SANCTIONS","Wire roundups - REPORTED","eu"),
]
GRID=[
 (1,"EUROPE - DEFENCE","Poland","NATO sends early-warning jets to Poland","NATO plans AWACS deployment in Poland after Russian missiles landed in Poland. Chancellor Merz vows complete support.","AWACS TO POLAND","Wire reports - REPORTED","plane"),
 (3,"MIDDLE EAST - OIL","Iraq","Baghdad orders Kurdish oilfields seized","PM Ali al-Zaidi directs federal units to seize oilfields and crossings. President Barzani: Kurdistan will not submit, says Zaidi order is unconstitutional.","OILFIELDS ORDER","Starlit / wires - REPORTED","oil"),
 (8,"AMERICAS - CRIME","Colombia","Car bomb injures at least 23","A car bomb in Colombia injured at least 23 people, wires report.","23 INJURED","Wires - REPORTED","bomb"),
 (10,"ASIA - AVIATION","China","Xiamen Airlines orders 50 Boeing jets","Xiamen Airlines, a China Southern unit, agreed to acquire 50 Boeing 737-8 jets - a Boeing 737 order of 50.","50 JETS ORDERED","Wires - REPORTED","plane"),
 (13,"OCEANIA - SCIENCE","Australia","12 coral species brought back","Great Barrier Reef genetic analysis resurrects 12 Acropora coral species. Reef diversity is wider than known.","12 SPECIES BACK","Science wires - REPORTED","coral"),
 (18,"AFRICA - SPORT","Senegal","Senegal's AFCON title restored","A CAS ruling gives Senegal its 2025 Africa Cup of Nations title back - cas ruling restores the AFCON crown.","TITLE RESTORED","Wires - REPORTED","flag"),
 (23,"SOUTH ASIA - POLITICS","Punjab","Old allies reunite in Punjab","BJP and Shiromani Akali Dal announce an alliance for the 2027 Punjab elections, ending a six-year split. Akali Dal returns.","ALLIANCE AGAIN","Indian wires - REPORTED","hands"),
 (25,"ASIA-PACIFIC - POLITICS","Indonesia","Indonesia's vice-president resigns","Indonesia's Vice-President resigns amid political strain, one source reports.","VP RESIGNS","Starlit - REPORTED","flag"),
 (33,"WORLD - MARKETS","Washington","PCE inflation report due today","The US PCE inflation report is due Tuesday 25 November. Markets watch for the Fed's next signal; no figure is published yet.","PCE DUE TODAY","Scheduled - SCHEDULED","graph"),
 (36,"WORLD - MARKETS","Nvidia","Nvidia's $1 trillion Monday","MONDAY CLOSE: Nvidia shares +31.5% - 31.5 on Monday - nearly $1 trillion of market value clawed back as Huang returns as CEO, +$34 billion in a day (Forbes)."," +31.5% MONDAY CLOSE","Forbes via wires - REPORTED","chip"),
]
def card(x,y,w,h,c,lead=False):
    num,reg,place,head,deck,chip,src,kind=c
    rect(x,y,w,h,fill=WHITE,outline=INK,width=2 if lead else 1)
    sh=92 if lead else 40
    scene(x+3,y+3,w-6,sh,kind,num)
    txt(x+8,y+sh+7,f"#{num}  {reg} - {place}",FBD(8 if lead else 7),GREEN)
    yy=y+sh+20
    for ln in wrap(head,FB(17 if lead else 12),w-14)[:3 if lead else 2]:
        txt(x+8,yy,ln,FB(17 if lead else 12),INK); yy+= (19 if lead else 14)
    for ln in wrap(deck,FR(9 if lead else 7),w-14)[:6 if lead else 3]:
        txt(x+8,yy,ln,FR(9 if lead else 7),INK); yy+= (11 if lead else 9)
    rect(x+6,y+h-30,w-12,11,fill=(230,224,200))
    txt(x+9,y+h-28,src,FR(7),GREY)
    rect(x+6,y+h-17,w-12,13,fill=GREEN); txt(x+w//2,y+h-15,chip,FBD(8),WHITE,"ma")
# leads row
lx=16
for c in LEADS:
    card(lx,262,322,238,c,lead=True); lx+=335
# grid 5 x 2
gx=16; gy=506
for i,c in enumerate(GRID):
    card(gx+(i%5)*199,gy+(i//5)*150,192,144,c)
# ---------- bottom: map + date check + also on ----------
by=812; rect(16,by,992,168,fill=(238,231,205),outline=INK,width=1)
txt(24,by+6,"DOTTED MAP - PINS = CARD NUMBERS",FBD(9),GREEN)
# dotted world (stylised dot grid land blobs)
import random
random.seed(7)
blobs=[(40,by+40,70,26),(120,by+30,60,30),(95,by+78,34,26),(190,by+36,80,30),(225,by+72,44,30),(300,by+42,60,24)]
for bx,bb_y,bw,bh in blobs:
    for _ in range(90):
        px=bx+random.randint(0,bw); py=bb_y+random.randint(0,bh)
        d.ellipse([px,py,px+2,py+2],fill=GREY)
pins=[(2,205,by+52),(6,245,by+44),(5,215,by+40),(1,225,by+36),(10,315,by+50),(13,330,by+92),(36,60,by+48)]
for n,px,py in pins:
    d.ellipse([px-8,py-8,px+8,py+8],fill=(200,50,40)); txt(px,py-6,str(n),FBD(8),WHITE,"ma")
txt(24,by+118,"Legend: red pins are numbered as the cards above.",FR(7),INK)
txt(24,by+130,"Gaza and Hamas (#4 brief), Lynx KF41 (#7 brief) also pinned by region.",FR(7),INK)
# date check
dx=380; txt(dx,by+6,"DATE CHECK - NOT TODAY'S NEWS",FBD(9),GREEN)
dc=["Merkury mission report - 23 Nov, not today","COP31 talks - earlier summit, not today","Liverpool 4-0 - earlier fixture, not today","GTA VI launch - not a 25 Nov event","Senegal 2025 AFCON final - title restored today, match was not"]
yy=by+22
for s in dc:
    for ln in wrap("X "+s,FR(8),250): txt(dx,yy,ln,FR(8),INK); yy+=11
    yy+=2
# also on
ax=650; txt(ax,by+6,"ALSO ON THIS PAGE - BRIEFS 14-37",FBD(9),GREEN)
briefs=["4 Gaza: Hamas chief killed, 7 dead - gaza, hamas","7 Lynx KF41 IFVs arrive Ukraine - lynx kf41","9 Cartagena: dozens held in market - cartagena","11 Madrid 5-1 PSV - mbappe, bellingham","12 T20I: Fraser-McGurk 27 off 13 - fraser-mcgurk, t20i","14 Fiji disaster, El Nino dry - fiji, el nino","15 Iran pharmacies run dry - pharmacies","16 Iran braces for winter gas shortage","17 Britain sanctions Houthi leaders - houthis","19 Rebels pull back in DR Congo - congo","20 Nigerian emir suspended - emir","21 Sudan RSF commander defects - sudan rsf","22 Cameroon leader in Norway court - cameroon","24 Bangladesh opens Guangzhou office - guangzhou","26 Solomon Islands eye treaty - solomon islands","27 North Korea touts China ties","28 Denmark upholds ghetto law - denmark, ghetto","29 Sarkozy for Libya-case trial - sarkozy","30 Black Sea clash at UN - black sea","31 Shortwave for Afghan girls - shortwave, afghan girls","32 Dimorphos shadows Didymos - didymos, dimorphos","34 US targets 7 firms, Alibaba one - alibaba","35 Moscow buys inflatable decoys - decoys","37 Thanksgiving storms both coasts - thanksgiving"]
yy=by+22
for b in briefs:
    txt(ax,yy,b,FR(5),INK); yy+=6
# footer
txt(512,986,"Sources: RFE/RL - Al Jazeera - DW - Starlit Daily - Forbes via wires - wire roundups  -  Original drawings",FR(8),GREY,"ma")
txt(512,1000,"THE CONTINENTAL - one day, one page - every story dated Tuesday 25 November 2026",FBD(8),GREEN,"ma")
img.save("/home/hatch/workspace/makefun/ni25-akun16-build/entry_a.png")
print("saved A")
