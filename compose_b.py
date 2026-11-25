#!/usr/bin/env python3
# THE CONTINENTAL - NI25 Akun 16 - Variant B (lead column left, grid right)
import os, sys
sys.path.insert(0,"/home/hatch/workspace/makefun/ni25-akun16-build")
# B reuses A's drawing primitives by executing A up to header would be wasteful;
# instead B is a compact standalone variant with a left lead rail.
from PIL import Image, ImageDraw, ImageFont
W=1024; H=1024
RICE=(240,232,208); INK=(18,18,16); GREEN=(20,83,45); DGREEN=(13,54,30); WHITE=(250,248,240); GREY=(90,88,80)
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
def FB(s): return font(["PlayfairDisplay-Black.ttf","Playfair-Black.ttf"],s)
def FBD(s): return font(["DejaVuSans-Bold.ttf"],s)
def FR(s): return font(["DejaVuSans.ttf"],s)
img=Image.new("RGB",(W,H),RICE); d=ImageDraw.Draw(img)
def rect(x,y,w,h,fill=None,outline=None,width=1): d.rectangle([x,y,x+w,y+h],fill=fill,outline=outline,width=width)
def txt(x,y,s,f,fill=INK,anchor=None): d.text((x,y),s,font=f,fill=fill,anchor=anchor)
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
txt(16,8,"TUESDAY'S WORLD - 37 STORIES - 9 REGIONS - EVERY ONE DATED",FBD(12),GREEN)
txt(16,24,"THE CONTINENTAL",FB(46),INK)
txt(990,30,"TUESDAY",FB(38),DGREEN,"ra"); txt(990,72,"25 NOVEMBER 2026",FB(30),DGREEN,"ra")
rect(16,118,992,3,fill=GREEN)
nums="NUMBERS: 3 tankers hit - Iran says (#2) - 700,000+ Russian dead (#6) - 50 Boeing 737-8 jets (#10) - 12 coral species back (#13) - 23 injured Colombia (#8) - +31.5% Nvidia Monday (#36)"
for i,ln in enumerate(wrap(nums,FBD(10),980)): txt(16,126+i*14,ln,FBD(10),INK)
regs="REGIONS: EUROPE - MIDDLE EAST - AFRICA - AMERICAS - ASIA - SOUTH ASIA - ASIA-PACIFIC - OCEANIA - WORLD"
txt(16,156,regs,FBD(10),GREEN)
tl="ORDER: 22 Nov Iran gas rationing began - MONDAY CLOSE Nvidia - TUESDAY PCE due today - TUESDAY Madrid 5-1 PSV - AHEAD Thanksgiving storms - 2027 Punjab alliance"
for i,ln in enumerate(wrap(tl,FR(8),980)): txt(16,174+i*11,ln,FR(8),INK)
LEADS=[
 (2,"HORMUZ - IRAN SAYS","Iran says 3 tankers hit by mines","IRGC claims three oil tankers hit by naval mines in the Strait of Hormuz; shipping concerns rise.","3 TANKERS - IRAN SAYS","Iranian claim via wires - CLAIMED"),
 (6,"UKRAINE WAR DATA","700,000 Russian dead, new count finds","New analysis finds more than 700,000 Russian soldiers killed in the nearly five-year war on Ukraine.","700,000+ KILLED","RFE/RL - REPORTED"),
 (5,"BRUSSELS - EU","EU unveils new Russia sanctions","The EU announced further restrictive measures against Russia amid the war in Ukraine.","NEW EU SANCTIONS","Wire roundups - REPORTED"),
]
GRID=[
 (1,"POLAND - NATO","NATO sends AWACS jets to Poland","AWACS to Poland after Russian missiles landed there; Merz vows complete support.","AWACS TO POLAND","Wires - REPORTED"),
 (3,"IRAQ - OIL","Baghdad orders Kurdish oilfields seized","Zaidi directs units to seize oilfields; Barzani says Kurdistan will not submit.","OILFIELDS ORDER","Starlit - REPORTED"),
 (8,"COLOMBIA","Car bomb injures at least 23","A car bomb in Colombia injured at least 23 people.","23 INJURED","Wires - REPORTED"),
 (10,"CHINA - XIAMEN","Xiamen orders 50 Boeing 737-8 jets","Xiamen Airlines agreed to acquire 50 Boeing 737-8 jets.","50 JETS ORDERED","Wires - REPORTED"),
 (13,"AUSTRALIA - CORAL","12 coral species brought back","GBR genetic analysis resurrects 12 Acropora coral species.","12 SPECIES BACK","Science wires - REPORTED"),
 (18,"SENEGAL - AFCON","Senegal AFCON title restored","CAS ruling gives Senegal its 2025 AFCON title back.","TITLE RESTORED","Wires - REPORTED"),
 (23,"PUNJAB","Old allies reunite in Punjab","BJP and Akali Dal announce alliance for 2027 Punjab elections.","ALLIANCE AGAIN","Indian wires - REPORTED"),
 (25,"INDONESIA","Indonesia's vice-president resigns","Indonesia's Vice-President resigns amid political strain.","VP RESIGNS","Starlit - REPORTED"),
 (33,"WASHINGTON - PCE","PCE inflation report due today","US PCE report due Tuesday 25 Nov; no figure published yet.","PCE DUE TODAY","Scheduled - SCHEDULED"),
 (36,"NVIDIA - MONDAY CLOSE","Nvidia's $1 trillion Monday","MONDAY CLOSE +31.5%: nearly $1tn back, Huang CEO again, +$34bn a day.","+31.5% MONDAY CLOSE","Forbes - REPORTED"),
]
def card(x,y,w,h,num,reg,head,deck,chip,src,lead=False):
    rect(x,y,w,h,fill=WHITE,outline=INK,width=2 if lead else 1)
    rect(x+3,y+3,w-6,26 if lead else 18,fill=(198,224,205))
    d.ellipse([x+w-26,y+7,x+w-10,y+23],fill=(240,205,90))
    txt(x+8,y+34,f"#{num} {reg}",FBD(8),GREEN); yy=y+48
    for ln in wrap(head,FB(16 if lead else 11),w-14)[:3]:
        txt(x+8,yy,ln,FB(16 if lead else 11),INK); yy+=18 if lead else 13
    for ln in wrap(deck,FR(8 if lead else 7),w-14)[:4]:
        txt(x+8,yy,ln,FR(8 if lead else 7),INK); yy+=10 if lead else 9
    txt(x+8,y+h-26,src,FR(7),GREY)
    rect(x+6,y+h-16,w-12,12,fill=GREEN); txt(x+w//2,y+h-14,chip,FBD(7),WHITE,"ma")
y=200
for c in LEADS: card(16,y,300,150,*c,lead=True); y+=156
gx=330; gy=200
for i,c in enumerate(GRID): card(gx+(i%2)*340,gy+(i//2)*92,332,86,*c)
by=812; rect(16,by,992,168,fill=(238,231,205),outline=INK)
txt(24,by+6,"MAP PINS = CARD NUMBERS: 2 Hormuz - 6 Ukraine - 5 Brussels - 1 Poland - 10 China - 13 Reef - 36 Nvidia",FBD(9),GREEN)
txt(24,by+24,"DATE CHECK - NOT TODAY: Merkury 23 Nov - COP31 earlier - Liverpool 4-0 earlier - GTA VI launch not 25 Nov",FR(9),INK)
briefs=["4 Gaza Hamas chief killed","7 Lynx KF41 IFVs Ukraine","9 Cartagena dozens held","11 Madrid 5-1 PSV Mbappe Bellingham","12 T20I Fraser-McGurk 27 off 13","14 Fiji El Nino disaster","15 Iran pharmacies dry","16 Iran winter gas shortage","17 Houthis sanctioned by UK","19 DR Congo rebels pull back","20 Emir suspended Nigeria","21 Sudan RSF defection","22 Cameroon Norway court","24 Guangzhou office opens","26 Solomon Islands treaty","27 North Korea China ties","28 Denmark ghetto law upheld","29 Sarkozy Libya trial","30 Black Sea UN clash","31 Shortwave Afghan girls","32 Dimorphos Didymos eclipse","34 Alibaba firm among 7 targeted","35 Inflatable decoys bought","37 Thanksgiving storms"]
yy=by+44
for i,b in enumerate(briefs): txt(24+(i%3)*330,yy+(i//3)*13,b,FR(8),INK)
txt(512,986,"Sources: RFE/RL - Al Jazeera - DW - Starlit - Forbes via wires - Original drawings",FR(8),GREY,"ma")
txt(512,1000,"THE CONTINENTAL - Tuesday 25 November 2026 - every story dated",FBD(8),GREEN,"ma")
img.save("/home/hatch/workspace/makefun/ni25-akun16-build/entry_b.png")
print("saved B")
