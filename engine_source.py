import json,os,random,urllib.request as u
class AB(Exception):pass
I=1e9;M=1e7
ad=lambda v,p:v+(p if v>1e5 else-p if v<-1e5 else 0)
T='::::NNNPFFFKAAAH>>>C<<<<::::::::0369369<69<?9<?B9<?B69<?369<036968:<8:<>:<>@<>@B<>@B:<>@8:<>68:<::::BBBB:::::::::::::::::::::::<789:89:;9:;<:;<=:;<=9:;<89:;789:!!!!!!!!!!!!!!!!$$$$++++2222DF?:'
Y=[0,5,10,20,40,80,150,0];V=[0,100,320,330,500,900,0];J=(-33,-31,-18,-14,14,18,31,33);X=(-17,-16,-15,-1,1,15,16,17);D=(-17,-15,15,17);R=(-16,-1,1,16);DT=(0,0,J,D,R,X,X)
CR={7:1,0:2,119:4,112:8,4:3,116:12};CS={6:7,2:0,118:119,114:112}
BG='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
MT=[[0]*128 for _ in range(15)];ET=[[0]*128 for _ in range(15)]
for p in range(1,7):
 for s in range(128):
  if s&136:continue
  r=s>>4;f=s&7;c=min(f,7-f);x=(ord(T[(p-1)*32+(7-r)*4+c])-58)*2;y=x if p<6 else 8*(c+min(r,7-r))-24;z=V[p]+x;w=V[p]+y
  MT[p][s]=z;ET[p][s]=w;MT[p+8][s^112]=-z;ET[p+8][s^112]=-w
O='AGVzjOW+tFOyi:LTYTaYFkIoCVWQAnJEsmWtl;ALbzjKayqBS+t:AjBgBjAJCCcBhBbeNiH;CLb+tKa0sOWzj:iQPADcSeCklWFRPRaLVWASUOZLNVDJQHVW;DMc0kGV5qFhwo:NAKIfcQfBYgYGOGObNgPPcJeJK;DMcyiGVzrLbib:AGGABIGMAUGOAkBAB;ELb1lOW+tFO0s:MAbTDjfQcGjgPWhkjjLZaQYCSCWICKGcDYQDDQMIj;EMc0kGV5qFa9i:EGYbDGBTNMYIURXW;FMczjcj7jBSjg:gSDcQIfcJBbAdUkXCfKUWOGWNSQbbXXSJKBBDCvNpQC;GMc0kGV5qFhwo:NhRCNGYMbBXWmIkaQACn;HMc0kGV5qFh+t:BCBSJJAJMDOAMFYCXFJBOScKLJQOFPBLMSEDBFGDJDJPFFPJDLAMAAPtf;HNdzjGV+tMU2u:TfJWMYKMBFJSITLUBIBAaAEkbUANffl;IKa0kBS+tGV5q:dOUBJOMJXYWUKmodgAXSFUBPYODdMXZKLTQYYHPZKJTMZ;ILbzjKayqGV+t:SlTURbQGTSYOkbXIAEsUghXlaXTmtU;JKa0kBS+tGV5q:JEXLCmSDXXTLABCBEHLUMVAWKBCBaMGcGCbNSBDCQRDRQDTCEHWWEABCQFCPEECDDVSLS;KLbzjKayqBS+t:QWYUKQQNaYVYOmjbNHolOQc;LMc0kGVzrLb+t:MTNcBYRbXQNSDGLGNHHTTTZcNcFLATBJTMiBUMdGBOEWhgHAFGKBFAAIfDgeb;LMcyiKS+tcktj:LUGbaWkcFCFHoilVuGDqjdGYQGGbLBOJOLQSKLNMGcDYQQBKAIAAZAF'
BK=dict(x.split(':')for x in O.split(';'))
Rr=random.Random(7);Z=[Rr.getrandbits(64)for _ in range(2065)]
U=[];TT={};KL={};HS=set()
URL=os.getenv('MAKEFUN_ENV_URL')
def F(fen):
 global B,S,C,K,P,MG,EG,N,H
 B=[0]*128;P=[[],[]];K=[0,0];MG=0;EG=0;N=[0,0];H=0
 w=fen.split();s=112
 for ch in w[0]:
  if ch=='/':s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   pc='PNBRQK'.index(ch.upper())+1+8*ch.islower()
   B[s]=pc;P[pc>>3].append(s)
   if(pc&7)==6:K[pc>>3]=s
   MG+=MT[pc][s];EG+=ET[pc][s]
   if(pc&7)!=1:N[pc>>3]+=V[pc&7]
   H^=Z[pc<<7|s];s+=1
 S=w[1]=='b'
 C=('K'in w[2])+2*('Q'in w[2])+4*('k'in w[2])+8*('q'in w[2])
 H^=Z[2048+C]
 if S:H^=Z[2064]
def W(s,by):
 for d in(15,17):
  t=s+d*(2*by-1)
  if not t&136 and B[t]==1+by*8:return 1
 for d in J:
  t=s+d
  if not t&136 and B[t]==2+by*8:return 1
 for d in X:
  t=s+d
  if not t&136 and B[t]==6+by*8:return 1
 for d in X:
  t=s+d
  while not t&136:
   q=B[t]
   if q:
    if q>>3==by and(q&7==5 or(d in D and q&7==3)or(d in R and q&7==4)):return 1
    break
   t+=d
 return 0
def G(cp=False):
 ms=[];A=ms.append;pd=16-32*S;sr=1+5*S;lr=7-7*S
 for s in P[S]:
  pc=B[s];t=pc&7
  if t==1:
   t1=s+pd
   if not t1&136 and not B[t1]:
    p5=(5<<14)if(t1>>4)==lr else 0
    if p5 or not cp:A(s|(t1<<7)|p5)
    if not cp and(s>>4)==sr and not B[t2:=s+2*pd]:A(s|(t2<<7))
   for e in(pd-1,pd+1):
    t1=s+e
    if not t1&136 and B[t1]and B[t1]>>3!=S:A(s|(t1<<7)|((5<<14)if(t1>>4)==lr else 0))
  else:
   for d in DT[t]:
    t1=s+d
    while not t1&136:
     q=B[t1]
     if q:
      if q>>3!=S:A(s|(t1<<7))
      break
     if not cp:A(s|(t1<<7))
     if t==2 or t==6:break
     t1+=d
 if not cp:
  ks=116 if S else 4
  if B[ks]==6+S*8:
   for z in(1,-1):
    ds=ks+2*z
    if C>>(2*S+(z<0))&1 and B[CS[ds]]==4+S*8 and not(B[ks+z]or B[ds])and(z>0 or not B[ks-3])and all(not W(ks+i*z,1-S)for i in(0,1,2)):A(ks|(ds<<7)|(1<<18))
 return ms
def Mk(m):
 global S,C,H,MG,EG
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;pc=B[f];c=B[t]
 U.append((m,pc,c,C,H,MG,EG,N[0],N[1]))
 npc=pr+(S<<3)if pr else pc
 H^=Z[pc<<7|f]^Z[npc<<7|t]^(Z[c<<7|t]if c else 0)
 MG+=MT[npc][t]-MT[pc][f];EG+=ET[npc][t]-ET[pc][f]
 if c:
  MG-=MT[c][t];EG-=ET[c][t]
  if(c&7)!=1:N[c>>3]-=V[c&7]
  P[1-S].remove(t)
 if pr:N[S]+=V[pr]
 B[f]=0;B[t]=npc
 P[S].remove(f);P[S].append(t)
 if(pc&7)==6:K[S]=t
 if(m>>18)&1:
  rt=CS[t];rd=t-1 if t>f else t+1;rk=B[rt]
  H^=Z[rk<<7|rt]^Z[rk<<7|rd]
  MG+=MT[rk][rd]-MT[rk][rt];EG+=ET[rk][rd]-ET[rk][rt]
  B[rt]=0;B[rd]=rk;P[S].remove(rt);P[S].append(rd)
 nc=C&~(CR.get(f,0)|CR.get(t,0))
 H^=Z[2048+C]^Z[2048+nc];C=nc
 S^=1;H^=Z[2064]
def Uk():
 global S,C,H,MG,EG
 m,pc,c,oc,oh,omg,oeg,n0,n1=U.pop()
 S^=1
 f=m&127;t=(m>>7)&127
 B[f]=pc;B[t]=c
 P[S].remove(t);P[S].append(f)
 if c:P[1-S].append(t)
 if(pc&7)==6:K[S]=f
 if(m>>18)&1:
  rt=CS[t];rd=t-1 if t>f else t+1
  B[rt]=4+S*8;B[rd]=0;P[S].remove(rd);P[S].append(rt)
 C=oc;H=oh;MG=omg;EG=oeg;N[:]=n0,n1
def Nm():
 global S,H
 S^=1;H^=Z[2064]
def E():
 np=N[0]+N[1]
 s=MG if np>=6400 else(MG*np+EG*(6400-np))//6400
 mx=[-1]*10;mn=[8]*10;bw=0;bb=0
 for q in P[0]+P[1]:
  pc=B[q]
  if pc==1:mn[(q&7)+1]=min(mn[(q&7)+1],q>>4)
  elif pc==9:mx[(q&7)+1]=max(mx[(q&7)+1],q>>4)
  elif pc==3:bw+=1
  elif pc==11:bb+=1
 for q in P[0]+P[1]:
  pc=B[q]
  if pc==1:
   f=q&7;r=q>>4
   if r>max(mx[f:f+3]):s+=Y[r]
  elif pc==9:
   f=q&7;r=q>>4
   if r<min(mn[f:f+3]):s-=Y[7-r]
 s+=30*(bw>1)-30*(bb>1)
 return s*(1-S*2)
def So(ms,tm,ply):
 kl=KL.get(ply)or[0,0]
 ms.sort(key=lambda m:(m==tm)<<20|((m>>14)&7)<<17|(m in kl)<<14|((c:=B[(m>>7)&127])and V[c&7]*10-V[B[m&127]&7]),reverse=True)
def Sc(d,a,b,ply):
 global ND,BT
 ND+=1
 if LM and ND>LM:raise AB
 if ply and H in HS:return 0
 if d<=0:
  ck=W(K[S],1-S)
  if ck:
   ms=G();So(ms,0,ply);n=0
   for m in ms:
    Mk(m)
    if W(K[1-S],S):Uk();continue
    n+=1;v=-Sc(0,-b,-a,ply+1);Uk()
    if v>a:a=v
    if a>=b:return a
   if n==0:return -M+ply
   return a
  st=E()
  if st>=b:return st
  if st>a:a=st
  ms=G(True)
  if not ms:return 0 if not G()else a
  So(ms,0,ply)
  for m in ms:
   Mk(m)
   if W(K[1-S],S):Uk();continue
   v=-Sc(0,-b,-a,ply+1);Uk()
   if v>a:a=v
   if a>=b:return a
  return a
 a0=a;ck=W(K[S],1-S)
 e=TT.get(H);tm=e[3]if e else 0
 if ply and e and e[0]>=d:
  s2=ad(e[1],-ply)
  if e[2]==0 or(e[2]==1 and s2>=b)or(e[2]==2 and s2<=a):return s2
 if ply and d>2 and not ck and N[S]>0 and E()>=b:
  Nm();v=-Sc(d-3,-b,-b+1,ply+1);Nm()
  if v>=b:return b
 ms=G()
 ms.sort(key=lambda m:PV.get(m,0),reverse=True)if ply==0 else So(ms,tm,ply)
 bt=-I;n=0;kl=KL.get(ply)or[0,0]
 for m in ms:
  qt=B[(m>>7)&127]==0 and not(m>>14)&7 and not(m>>18)
  Mk(m)
  if W(K[1-S],S):Uk();continue
  n+=1;rd=d-1
  if n>1:
   if ply and d>2 and n>3 and qt and m not in kl:rd=d-2
   v=-Sc(rd,-a-1,-a,ply+1)
   if rd<d-1 and v>a:v=-Sc(d-1,-a-1,-a,ply+1)
   if a<v<b:v=-Sc(d-1,-b,-a,ply+1)
  else:v=-Sc(d-1,-b,-a,ply+1)
  Uk()
  if ply==0:PV[m]=v
  if v>bt:bt=v;bm=m
  if v>a:a=v
  if a>=b:
   if qt and kl[0]!=m:KL[ply]=[m,kl[0]]
   break
 if n==0:return -M+ply if ck else 0
 if len(TT)>3e5:TT.clear()
 TT[H]=(d,ad(bt,ply),2 if bt<=a0 else 1 if bt>=b else 0,bm)
 if ply==0:BT=bm
 return bt
def Rt(fen):
 global ND,LM,PV,BT
 PV={};BT=0;d=1;ND=0
 while True:
  LM=50000*(d>1)
  try:bs=Sc(d,-I,I,0)
  except AB:F(fen);U.clear();break
  if abs(bs)>1e5:break
  d+=1
 return BT
def Ky(v):
 return int(v[6:])-2 if v[0]=='d' else 3+['100k','250k','500k','1M','2M'].index(v[6:])
def En(u):
 a=lambda x:ord(x[0])+int(x[1])*8-105;v=a(u[:2])*64+a(u[2:]);return BG[v//64]+BG[v%64]
def Bk():
 d={}
 for l in open(os.getenv('MAKEFUN_PROMPT_FILE')):
  w=l.split()
  if w and w[0]=='game':
   k=chr(65+2*Ky(w[2])+(w[6][:-1]=='black'))
   for m in w[-8:-2]:k+=En(m)
   d[int(w[1])]=k
 return d
def Uc(m):
 return'%c%d%c%d%s'%(97+(m&7),1+((m>>4)&7),97+((m>>7)&7),1+((m>>11)&7),'q'if(m>>14)&7 else'')
def Ch(g):
 F(g['fen']);HS.add(H)
 v=BK.get(GK.get(g['game']))
 if v:
  i=g['plies']//2-4
  if i<len(v):return g['legal_moves'][BG.index(v[i])]
 m=Rt(g['fen']);u=Uc(m);lm=g['legal_moves']
 return u if u in lm else lm[0]
def Pt(p,o):
 return json.loads(u.urlopen(URL+p,json.dumps(o).encode()).read())
def main():
 global GK
 GK=Bk()
 while 1:
  g=Pt('/game',{})
  if g['status']=='done':break
  if g['status']=='your_move':Pt('/move',{'game':g['game'],'move':Ch(g)})
main()
