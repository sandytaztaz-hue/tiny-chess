import json,os,urllib.request as u;A=[0,100,320,330,500,900,0];V=[[0]*128 for _ in range(16)]
T='::::SSSS??DI<<?F:::D<75:<??0::::!&++&0::+:?A+<AD+:AD+<?A&0:<!&++05555:::5:<?5<<?5:??5???5<::0555::::<???7:::7:::7:::7:::7::::::<05575:::5:<<7:<<::<<5<<<5:<:0557+&&!+&&!+&&!+&&!0++&5000DD::DI?:'
for t in range(1,7):
 for s in range(128):
  if s&136:continue
  r=s>>4;c=min(s&7,7-(s&7));v=(ord(T[(t-1)*32+(7-r)*4+c])-58)*2
  V[t][s]=A[t]+v;V[t|8][s^112]=-(A[t]+v)
N=(33,31,18,14,-14,-18,-31,-33);B=(15,17,-15,-17);O=(1,-1,16,-16);D=O+B;CK={0:13,7:14,4:12,112:7,119:11,116:3};RC={6:(7,5),2:(0,3),118:(119,117),114:(112,115)};b=[0]*128;s=0;c=0;k=[0,0];h=[];np=0;tt={};K=[0]*258;S=[0]
def F(x):
 global b,s,c,k,h,np;q=x.split();b=[0]*128;r=7;f=0;np=0
 for ch in q[0]:
  if ch=='/':r-=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   t='pnbrqk'.index(ch.lower())+1;p=t|8*(ch>='a');g=r*16+f;b[g]=p
   if t==6:k[ch>='a']=g
   elif t>1:np+=A[t]
   f+=1
 s=q[1]<'v';c=0
 for ch in q[2]:c|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
 S[0]=sum(V[p][x] for x,p in enumerate(b) if p)
 h=[]
def At(g,y):
 v=1-2*y;z=y<<3
 for o in(15,17):
  t=g-o*v
  if not t&136 and b[t]==1|z:return 1
 for e in N+D:
  t=g+e
  if not t&136 and b[t]==(2 if e in N else 6)|z:return 1
 for d in D:
  t=g+d
  while not t&136:
   p=b[t]
   if p:
    if p==3+(d in O)|z or p==5|z:return 1
    break
   t+=d
 return 0
def M(m):
 global s,c,np;f=m&127;g=(m>>7)&127;r=(m>>14)&7;p=b[f];o=p>>3;t=p&7;v=b[g];n=r|o<<3 if r else p;dS=V[n][g]-V[p][f]-(V[v][g]if v else 0)
 if m&262144:a,ee=RC[g];dS+=V[b[a]][ee]-V[b[a]][a]
 S[0]+=dS;h.append((m,v,c,dS));b[g]=n;b[f]=0
 if v&7>1:np-=A[v&7]
 if r:np+=A[r]
 if t==6:k[o]=g
 if m&262144:a,ee=RC[g];b[ee]=b[a];b[a]=0
 c&=CK.get(f,15)&CK.get(g,15);s^=1
 if At(k[o],o^1):U();return 0
 return 1
def U():
 global s,c,np;m,v,c,dS=h.pop();S[0]-=dS;f=m&127;g=(m>>7)&127;r=(m>>14)&7;s^=1;p=b[g];o=s
 if m&262144:a,ee=RC[g];b[a]=b[ee];b[ee]=0
 if r:np-=A[r];p=1|o<<3
 if v&7>1:np+=A[v&7]
 b[f]=p;b[g]=v
 if p&7==6:k[o]=f
def g(q=0):
 m=[];a=m.append;t=s
 for f,p in enumerate(b):
  if not p or p>>3!=t:continue
  y=p&7
  if y==1:
   d=16-32*t;o=f+d;pr=7-7*t;hr=1+5*t
   if not b[o] and not q:
    a(f|o<<7|81920*(o>>4==pr))
    if f>>4==hr and not b[o+d]:a(f|(o+d)<<7)
   for ee in(d-1,d+1):
    z=f+ee;v=b[z]if not z&136 else 0
    if v and v>>3!=t:a(f|z<<7|81920*(z>>4==pr))
  else:
   ds=(N,B,O,D,D)[y-2];sl=y not in(2,6)
   for d in ds:
    z=f+d
    while not z&136:
     v=b[z]
     if v:
      if v>>3!=t:a(f|z<<7)
      break
     if not q:a(f|z<<7)
     if not sl:break
     z+=d
   if y==6 and not q:
    z0=t*112
    for r,ee,o,zz in((1<<2*t,(5,6),7,6),(2<<2*t,(3,2,1),0,2)):
     if c&r and b[o+z0]==4|t<<3 and all(not b[v+z0] for v in ee) and not any(At(x+z0,1-t) for x in(4,ee[0],zz)):a(4+z0|(zz+z0)<<7|262144)
 return m
def E():
 return(1,-1)[s]*S[0]
def L():o=[];[o.append(m) or U() for m in g() if M(m)];return o
Z=[0,0,0];Kv=lambda z:b[(z>>7)&127];ph=[0]*129
def n(d,a,B,y):
 global s
 Z[0]+=1
 if Z[1] and Z[0]>=Z[1]:Z[2]=1;return 0
 if y>127:return E()
 ck=At(k[s],s^1)if d<1 or d>2 else 0
 if d<1 and not ck:
  p=E()
  if p>=B:return p
  u=p
  if p>a:a=p
  m=g(1);m.sort(key=Kv,reverse=1);l=0
  for zz in m:
   vc=b[(zz>>7)&127];pr=(zz>>14)&7
   if not M(zz):continue
   l+=1;w=-n(0,-B,-a,y+1);U()
   if Z[2]:return 0
   if w>u:u=w
   if w>a:a=w
   if a>=B:
    if not vc and not pr and zz!=K[2*y]:K[2*y+1]=K[2*y];K[2*y]=zz
    return u
  return u
 kk=bytes(b)+bytes((s,c))
 if y and kk in ph[:y]:return 0
 ph[y]=kk
 a0=a;tm=0
 if d>0:
  e=tt.get(kk)
  if e:
   tm=e[3]
   if e[0]>=d and(e[1]==1 or(e[1]==2 and e[2]>=B)or(e[1]==3 and e[2]<=a)):return e[2]
 if d>2 and np and not ck and E()>=B:
  s^=1;w=-n(d-3,-B,-B+1,y+1);s^=1
  if Z[2]:return 0
  if w>=B:return B
 m=g();m.sort(key=lambda z:(z==tm)*9999999+((z>>14)&7)*99999+(z==K[2*y])*40000+(z==K[2*y+1])*30000+10*A[b[(z>>7)&127]&7]-A[b[z&127]&7],reverse=1)
 l=0;bm=0;u=-100001
 for zz in m:
  vc=b[(zz>>7)&127];pr=(zz>>14)&7
  if not M(zz):continue
  l+=1
  if l>3 and d>2 and not ck and not vc and not pr and zz!=K[2*y] and zz!=K[2*y+1]:
   w=-n(d-2,-B,-a,y+1)
   if not Z[2] and w>a:w=-n(d-1,-B,-a,y+1)
  else:w=-n(d-1,-B,-a,y+1)
  U()
  if Z[2]:return 0
  if w>u:u=w;bm=zz
  if w>a:a=w
  if a>=B:
   if not vc and not pr and zz!=K[2*y]:K[2*y+1]=K[2*y];K[2*y]=zz
   break
 if l==0:return -100000+y if At(k[s],s^1) else 0
 if d>0:tt[kk]=(d,2 if u>=B else 3 if u<=a0 else 1,u,bm)
 return u
def r(l):
 m=L()
 if not m:return 0
 ph[0]=bytes(b)+bytes((s,c));u=m[0]
 for zz in range(1,65):
  Z[1]=l*(zz>1);Z[2]=0;a=v=-100001;ou=u;sc=[]
  for x in m:
   M(x);w=-n(zz-1,-100001,-a,1);U()
   if Z[2]:break
   sc.append((w,x))
   if w>v:v=w;u=x
   if w>a:a=w
  if Z[2]:u=ou;break
  m=[x for _,x in sorted(sc,reverse=1)]
  if v>=99872:break
 return u
def w(m):
 f=m&127;g=(m>>7)&127;return'%c%d%c%d'%(97+(f&7),1+(f>>4),97+(g&7),1+(g>>4))+('q'*((m>>14)&7>0))
def C(f,x):
 F(f)
 if len(tt)>200000:tt.clear()
 l=L()
 if not l:return None
 if len(l)==1:return w(l[0])
 Z[0]=0;m=r(x);return w(m)
def d(a,b):
 with u.urlopen(os.environ['MAKEFUN_ENV_URL']+a,json.dumps(b).encode()) as x:return json.load(x)
BK={'HNdzjGV+tMU2u':'TfJWMYKMBFJSITLUBIBAaAEkbUANffl','CLb+tKa0sOWzj':'iQPADcSeCklWFRPRaLVWASUOZLNVDJQHVT','ELb1lOW+tFO0s':'MAbTDjfQcGjgPWhkjjLZaQYCSCWICKGcDYQDDQMIj','JKa0kBS+tGV5q':'JEXLCmSDXXTLABCBEHLUMVAWKBCBaMGcGCbNSBDCQRDRQ','IKa0kBS+tGV5q':'dOUBJOMJXYWUKmodgAXSFUBPYODdMXZKLTQYYHPZKJTMZ','EMc0kGV5qFa9i':'NZcSAJeLJYPilhiRCeZIDtducnmckxt','AGVzjOW+tFOyi':'LTYTaYFkIoCVWQAnJEsmWtl','LMc0kGVzrLb+t':'MTNcBYRbXQNSDGLGNHHTTTZcNcFLAT','HMc0kGV5qFh+t':'BCBSJJAJLDOAMFYCXFJBOScKLJQOFPBLMSEDBFGDJDJMFFPJDL','DMc0kGV5qFhwo':'NAKIfcQfBYgYGOGObNfPPcJeJK','GMc0kGV5qFhwo':'NhRCNGYMbBXWmIkaQACn','FMczjcj7jBSjg':'gSDcQIfcJBbAdUkXCfKUWOGWNSQbbXXSJKBBDCsNpQC','ALbzjKayqBS+t':'QLblWWEalfpkkkfhiniOMU','KLbzjKayqBS+t':'QWYUKQQNaYVYOmjbNHolOQc','LMcyiKS+tcktj':'LUGbaWkcFCFHoilVuGDqjdGYQGGbLBOJOLQSKLNMGcDYQ','BMcyiGV5qLbib':'RJTMbAheekJKTWWDfGGPEgfQBA','ILbzjKayqGV+t':'SlTURbQGTSYOkbXIAEsUghXlaXTmtU'}
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
   mv=C(G["fen"],100000)
   if mv not in G["legal_moves"]:mv=G["legal_moves"][0]
  G=d("/move",{"game":G["game"],"move":mv})
