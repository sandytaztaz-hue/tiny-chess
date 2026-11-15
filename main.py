import json,os,urllib.request as u;A=[0,100,320,330,500,900,0];V=[[0]*128 for _ in range(16)]
T='::::SSSS??DI<<?F:::D<75:<??0::::!&++&0::+:?A+<AD+:AD+<?A&0:<!&++05555:::5:<?5<<?5:??5???5<::0555::::<???7:::7:::7:::7:::7::::::<05575:::5:<<7:<<::<<5<<<5:<:0557+&&!+&&!+&&!+&&!0++&5000DD::DI?:'
for i,ch in enumerate(T):
 t=i//32+1;j=i%32;r=7-j//4;c=j%4;v=A[t]+(ord(ch)-58)*2
 for f in(c,7-c):V[t][r*16+f]=v;V[t|8][r*16+f^112]=-v
N=(33,31,18,14,-14,-18,-31,-33);B=(15,17,-15,-17);O=(1,-1,16,-16);D=O+B;CK={0:13,7:14,4:12,112:7,119:11,116:3};RC={6:(7,5),2:(0,3),118:(119,117),114:(112,115)};CC=((1,4,(5,6),7,6),(2,4,(3,2,1),0,2),(4,116,(117,118),119,118),(8,116,(115,114,113),112,114));b=[0]*128;s=0;c=0;k=[0,0];h=[];tt={};I=-100001
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
def E():return(1-2*s)*sum(V[p][x]for x,p in enumerate(b)if p)
def L():return[m for m in g() if M(m)and(U()or 1)]
nn=[0];ll=[0];ab=[0]
def n(d,a,B,y):
 nn[0]+=1
 if nn[0]>=ll[0]>0:ab[0]=1;return 0
 if y>=128:return E()
 ck=At(k[s],s^1) if d<=0 else 0;u=I;bm=0;tm=0
 if d<=0 and not ck:
  u=E()
  if u>=B:return u
  if u>a:a=u
  m=g(1)
 else:
  a0=a;kk=bytes(b+[s,c])
  if d>0:
   e=tt.get(kk)
   if e:
    tm=e[3]
    if e[0]>=d and(e[1]==1 or(e[1]==2 and e[2]>=B)or(e[1]==3 and e[2]<=a)):return e[2]
  m=g()
 m.sort(key=lambda z:(z==tm,(z>>14)&7,10*A[b[(z>>7)&127]&7]),reverse=1);l=0
 for zz in m:
  if not M(zz):continue
  l+=1;w=-n(d-1,-B,-a,y+1);U()
  if ab[0]:return 0
  if w>u:u=w;bm=zz
  if w>a:a=w
  if a>=B:break
 if d<=0 and not ck:return u
 if l==0:return I+1+y if At(k[s],s^1) else 0
 if d<=0:return u
 tt[kk]=(d,1+(u>=B)+2*(u<=a0),u,bm)
 return u
def r(l):
 m=L()
 if not m:return 0
 u=m[0]
 for zz in range(64):
  ll[0]=l*(zz>0);ab[0]=0;a=v=I;ou=u
  for x in m:
   M(x);w=-n(zz,I,-a,1);U()
   if ab[0]:break
   if w>v:v=w;u=x
   if w>a:a=w
  if ab[0]:u=ou;break
  m.remove(u);m.insert(0,u)
 return u
def w(m):a=lambda z:chr(97+z%8)+str(1+z//16);return a(m&127)+a((m>>7)&127)+'q'*((m>>14)&7>0)
def C(f,x):
 F(f);tt.clear()
 nn[0]=0;m=r(x);return w(m)
def d(a,b):return json.load(u.urlopen(os.environ['MAKEFUN_ENV_URL']+a,json.dumps(b).encode()))
while 1:
 G=d('/game',{})
 if G['status'][0]=='d':break
 while G['status'][0]=='y':
  m=C(G['fen'],100000);l=G['legal_moves']
  if m not in l:m=l[0]
  G=d('/move',{'game':G['game'],'move':m})
