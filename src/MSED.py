def algoritmo_division(a,b):
    q = a // b
    r = a % b
    if r < 0:
        r -= b
        q += 1
    return q, r

def algoritmo_euclides(a, b):
    cocientes = []
    residuos =[]
    q, r = algoritmo_division(a, b)
    if (r==0):
        cocientes.append(q)
        residuos.append(r)
    else:
        while (r != 0):
            cocientes.append(q)
            residuos.append(r)
            a = b
            b = r
            q, r = algoritmo_division(a, b)
    return b, cocientes, residuos

def mcd(a,b):
    d, c, r = algoritmo_euclides(a,b)
    return d

def lema_bezout(a,b):
   if (a==0):
        return b, 0, 1
   d, cocientes, residuos = algoritmo_euclides(a,b)
   if (residuos[0] == 0):
      x = 0
      y = 1
   else:
      x = 0
      y = 1
      for q in reversed(cocientes):
         aux = y
         y = x - q*y
         x = aux
   return d, x, y

def algoritmo_division_zn(a,b,n):
    d, u, v = lema_bezout(b,n)
    k,r = algoritmo_division(a,d)
    q= u*k
    q1, q = algoritmo_division(q, n)
    return q, r

def algoritmo_euclides_zn(a,b,n):
    cocientes = []
    residuos = []
    q, r = algoritmo_division_zn(a, b, n)
    if (r== 0):
        cocientes.append(q)
        residuos.append(r)
    else:
        while r != 0:
            cocientes.append(q)
            residuos.append(r)
            a = b
            b = r
            q, r = algoritmo_division_zn(a, b, n)
    mcd,c, r =algoritmo_euclides(b,n)

    return mcd, cocientes, residuos

def MCD (a,b,n):
    d,c,r= algoritmo_euclides_zn(a,b,n)
    return d

def lema_bezout_zn(a,b,n):
    d1, u ,v = lema_bezout(a,b)
    d, u1, v1= lema_bezout(d1,n)
    x= u*u1
    y= v*u1
    q1,x= algoritmo_division(x,n)
    q2,y= algoritmo_division(y,n)
    return d, x, y

def hay_solucion(a, b, c, n):
    solucion = False
    d = MCD(a,b,n)
    q,r = algoritmo_division(c,d)
    if r == 0:
        solucion = True
    return solucion
    
def falsa_posicion(a,b,c,n,x1,y1):
    d= a*x1 + b*y1
    q0,d= algoritmo_division(d,n)
    m = mcd(d,n)
    q,r= algoritmo_division(c,d)
    if (m==1):
        m, d_i , l = lema_bezout(d,n)
        k= c*d_i
        x= x1*k
        y= y1*k
        q1, x = algoritmo_division(x,n)
        q2, y = algoritmo_division(y,n)
    elif (m!=1 and r==0):
        x= x1*q
        y= y1*q
        q1, x = algoritmo_division(x,n)
        q2, y = algoritmo_division(y,n)
    return x ,y

def euclides_bezout(a,b,c,n):
    d, u, v = lema_bezout_zn(a,b,n)
    k, r = algoritmo_division_zn(c,d,n)
    x= u*k
    y= v*k
    q,x= algoritmo_division(x, n)
    q,y= algoritmo_division(y, n)
    return x, y

def diofanto (a,b,c,n,t_2):
    m, cocientes, residuos = algoritmo_euclides_zn(b,a,n)
    p=[]
    if (len(residuos) == 1):
        y = a*t_2 + c
        x= t_2 + cocientes[0]*y 
        q, x = algoritmo_division(x,n)
        q1, y = algoritmo_division(y,n)
    else:
        t_1 = residuos[-2]*t_2 + c
        p.append(t_2)
        p.append(t_1)
        for q in reversed(cocientes):
            t = q*t_1 + t_2
            p.append(t)
            aux = t_1
            t_1= t
            t_2= aux
        x= p[-1]
        y= p[-2]
        q, x = algoritmo_division(x,n)
        q1, y = algoritmo_division(y,n)
    return x,y

def ternas_Diofanto1 (m,n):
    z= m**2+1
    x= 2*m
    y= m**2 -1
    q1,x = algoritmo_division(x,n)
    q2,y = algoritmo_division(y,n)
    q3,z = algoritmo_division(z,n)
    return x,y,z

def ternas_Diofanto2 (p,q,n):
    z= p**2 + q**2
    x= 2*p*q
    y= p**2 - q**2
    q1,x = algoritmo_division(x,n)
    q2,y = algoritmo_division(y,n)
    q3,z = algoritmo_division(z,n)
    return x,y,z

def sucesion_fibonacci(n):
  f1 = 1
  if n<=f1:
    return n
  else:
    fn = sucesion_fibonacci(n-1) + sucesion_fibonacci(n-2)
    return fn

def ternas_fibonacci(m,n):
    fm= sucesion_fibonacci(m)
    fm1= sucesion_fibonacci(m+1)
    fm2= sucesion_fibonacci(m+2)
    fm3= sucesion_fibonacci(m+3)
    x= fm*fm3
    y= 2*fm1*fm2
    z= fm1**2 + fm2**2
    q1,x = algoritmo_division(x,n)
    q2,y = algoritmo_division(y,n)
    q3,z = algoritmo_division(z,n)
    return x,y,z
