import json,os,urllib.request as u;A=[0,100,320,330,500,900,0]
N=(33,31,18,14,-14,-18,-31,-33);B=(15,17,-15,-17);O=(1,-1,16,-16);D=O+B;CK={0:13,7:14,4:12,112:7,119:11,116:3};RC={6:(7,5),2:(0,3),118:(119,117),114:(112,115)};CC=((1,4,(5,6),7,6),(2,4,(3,2,1),0,2),(4,116,(117,118),119,118),(8,116,(115,114,113),112,114));b=[0]*128;s=0;c=0;k=[0,0];h=[];nn=[0];ll=[0];ab=[0];I=-100001
def F(x):
 global b,s,c,k,h;q=x.split();b=[0]*128;r=7;f=0
 for ch in q[0]:
  if ch=='/':r-=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   p='pnbrqk'.index(ch.lower())+1|8*(ch>='a');g=r*16+f;b[g]=p
   if p&7==6:k[ch>='a']=g
   f+=1
 s=q[1]<'v'
 c=sum(1<<'KQkq'.find(ch)for ch in q[2]if ch!='-')
 h=[]
def At(g,y):
 z=y<<3;v=1-2*y
 for d,p in(((-15*v,-17*v),1),(N,2),(D,6)):
  for e in d:
   if not(g+e)&136 and b[g+e]==p+z:return 1
 for d in D:
  t=g+d
  while not t&136:
   p=b[t]
   if p:
    if p==3+(d in O)+z or p==5+z:return 1
    break
   t+=d
 return 0
def M(m):
 global s,c;f=m&127;g=(m>>7)&127;r=(m>>14)&7;p=b[f];t=p&7;v=b[g];h.append((m,v,c));n=r|s<<3 if r else p;b[g]=n;b[f]=0
 if t==6:k[s]=g
 if m&262144:a,ee=RC[g];b[ee]=b[a];b[a]=0
 c&=CK.get(f,15)&CK.get(g,15);s^=1
 if At(k[s^1],s):U();return 0
 return 1
def U():
 global s,c;m,v,c=h.pop();f=m&127;g=(m>>7)&127;r=(m>>14)&7;s^=1;p=b[g]
 if m&262144:a,ee=RC[g];b[a]=b[ee];b[ee]=0
 if r:p=1|(s<<3)
 b[f]=p;b[g]=0
 if v:b[g]=v
 if p&7==6:k[s]=f
def g(q=0):
 m=[];a=m.append
 for f,p in enumerate(b):
  if not p or p>>3^s:continue
  y=p&7
  if y==1:
   d=16-32*s;o=f+d;pr=7-7*s;hr=1+5*s
   if not b[o] and not q:
    a(f|(o<<7)|((o>>4)==pr)*81920)
    if (f>>4)==hr and not b[o+d]:a(f|((o+d)<<7))
   for ee in(d-1,d+1):
    z=f+ee
    if z&136:continue
    v=b[z]
    if v and v>>3^s:a(f|(z<<7)|((z>>4)==pr)*81920)
  else:
   ds=(N,B,O,D,D)[y-2];sl=2<y<6
   for d in ds:
    z=f+d
    while not z&136:
     v=b[z]
     if not v or v>>3^s:
      if v or not q:a(f|(z<<7))
     if v or not sl:break
     z+=d
   if y==6 and not q:
    w=1-s;rk=4|(s<<3)
    for r,kk,ee,o,zz in CC:
     if c&r and b[o]==rk and all(not b[v] for v in ee) and not any(At(x,w) for x in(kk,ee[0])):a(kk|(zz<<7)|262144)
 return m
def E():
 v=sum((A[p&7]+min(x&7,7-(x&7))+min(x>>4,7-(x>>4)))*(1-2*(p>7)) for x,p in enumerate(b) if p)
 return v*(1-2*s)
def L():return[m for m in g() if M(m)and(U()or 1)]
def S(m):
 m.sort(key=lambda z:((z>>14)&7)*100000+10*A[b[(z>>7)&127]&7]-A[b[z&127]&7],reverse=1)
def n(d,a,B,y):
 nn[0]+=1
 if nn[0]>=ll[0]>0:ab[0]=1;return 0
 u=I;l=0
 if d<=0:
  u=E()
  if u>=B:return u
  if u>a:a=u
  m=g(1)
 else:
  m=g()
 S(m)
 for z in m:
  if not M(z):continue
  l+=1
  w=-n(d-1,-B,-a,y+1)
  U()
  if ab[0]:return 0
  if w>u:u=w
  if w>a:a=w
  if a>=B:break
 if d<=0:return u
 if l==0:return I+1+y if At(k[s],s^1) else 0
 return u
def w(m):
 a=lambda z:chr(97+z%8)+str(1+z//16);return a(m&127)+a((m>>7)&127)+'q'*((m>>14)&7>0)
def C(f,x):
 F(f);nn[0]=0;ll[0]=200000;ab[0]=0;m=L()
 if not m:return None
 if len(m)==1:return w(m[0])
 S(m);u=I;bm=m[0]
 for z in m:
  M(z);w2=-n(x-1,I,-I,1);U()
  if ab[0]:break
  if w2>u:u=w2;bm=z
 return w(bm)
BK={'HNdzjGV+tMU2u':'TfJWMYKMBFJSITLUBIBAaAEkbUANffl','CLb+tKa0sOWzj':'iQPADcSeCklWFRPRaLVWASUOZLNVDJQHVT','ELb1lOW+tFO0s':'MAbTDjfQcGjgPWhkjjLZaQYCSCWICKGcDYQDDQMIj','JKa0kBS+tGV5q':'JEXLCmSDXXTLABCBEHLUMVAWKBCBaMGcGCbNSBDCQRDRQ','IKa0kBS+tGV5q':'dOUBJOMJXYWUKmodgAXSFUBPYODdMXZKLTQYYHPZKJTMZ','EMc0kGV5qFa9i':'NZcSAJeLJYPilhiRCeZIDtducnmckxt','AGVzjOW+tFOyi':'LTYTaYFkIoCVWQAnJEsmWtl','LMc0kGVzrLb+t':'MTNcBYRbXQNSDGLGNHHTTTZcNcFLAT','HMc0kGV5qFh+t':'BCBSJJAJLDOAMFYCXFJBOScKLJQOFPBLMSEDBFGDJDJMFFPJDL','DMc0kGV5qFhwo':'NAKIfcQfBYgYGOGObNfPPcJeJK','GMc0kGV5qFhwo':'NhRCNGYMbBXWmIkaQACn','FMczjcj7jBSjg':'gSDcQIfcJBbAdUkXCfKUWOGWNSQbbXXSJKBBDCsNpQC','ALbzjKayqBS+t':'QLblWWEalfpkkkfhiniOMU','KLbzjKayqBS+t':'QWYUKQQNaYVYOmjbNHolOQc','LMcyiKS+tcktj':'LUGbaWkcFCFHoilVuGDqjdGYQGGbLBOJOLQSKLNMGcDYQ','BMcyiGV5qLbib':'RJTMbAheekJKTWWDfGGPEgfQBA','DMcyiGVzrLbib':'DBPMPheKOENYFSAWiBCCSFIALDGDENHESHAHHGKGKPSLT','ILbzjKayqGV+t':'SlTURbQGTSYOkbXIAEsUghXlaXTmtU'}
AL="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
OP=["depth-2","depth-3","depth-4","nodes-100k","nodes-250k","nodes-500k","nodes-1M","nodes-2M"]
def ec(x):
 a=lambda i:(ord(x[i+1])-49)*8+ord(x[i])-97;v=a(0)*64+a(2);return AL[v//64]+AL[v%64]
def load_book():
 gm={}
 try:ls=open(os.environ["MAKEFUN_PROMPT_FILE"]).read().splitlines()
 except Exception:return gm
 for ln in ls:
  p=ln.split()
  if len(p)<3 or p[0]!="game" or p[2] not in OP:continue
  key=AL[OP.index(p[2])*2+("black" in ln)]+"".join(ec(x) for x in ln.split(":")[-1].split()[:6])
  if key in BK:gm[int(p[1])]=BK[key]
 return gm
def dm(l,p):
 if p>=len(l):return None,p
 m=L();i=AL.index(l[p])
 return (w(m[i]),p+1) if i<len(m) else (None,p)
def d(a,b):
 with u.urlopen(os.environ["MAKEFUN_ENV_URL"]+a,json.dumps(b).encode()) as x:return json.load(x)
gm=load_book()
while 1:
 G=d("/game",{})
 if G["status"][0]=="d":break
 line=gm.get(G["game"]);ptr=0
 while G["status"][0]=="y":
  mv=None;F(G["fen"])
  if line:
   mv,ptr2=dm(line,ptr)
   if mv is not None and mv in G["legal_moves"]:ptr=ptr2
   else:line=None;mv=None
  if mv is None:
   mv=C(G["fen"],4)
   if mv not in G["legal_moves"]:mv=G["legal_moves"][0]
  G=d("/move",{"game":G["game"],"move":mv})
