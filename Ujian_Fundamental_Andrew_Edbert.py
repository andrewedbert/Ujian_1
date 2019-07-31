#Soal 1
def calculate_years(principal, interest, tax, desired) :
    year = 0
    while principal < desired:
        principal=principal+((principal*interest)-(principal*interest*(tax)))
        year+=1
    
    return print(year)

calculate_years(1000.00,0.05,0.18,1100.00)
calculate_years(1200.00,0.17,0.05,2000.00)
calculate_years(1500.00,0.07,0.6,5000.00)

#Soal 2
def expanded_form(num):
    if int(num)<10 :
        a=str(num)
        print(a)
    elif int(num)>=10 and int(num)<100:
        b=str(num)
        c=b[0]
        d=int(c)*10
        e=b[1]
        print(str(d)+' + '+str(e))
    elif int(num)>=100 and int(num) <1000:
        f=str(num)
        g=f[0]
        h=f[1]
        i=f[2]
        j=int(g)*100
        k=int(h)*10
        if k==0:
            print(str(j)+' + '+str(i))
        else:
            print(str(j)+' + '+str(k)+' + '+str(i))
    elif int(num)>=1000 and int(num) <10000:
        l=str(num)
        m=l[0]
        n=l[1]
        o=l[2]
        p=l[3]
        q=int(m)*1000
        r=int(n)*100
        s=int(o)*10
        if r==0:
            print(str(q)+' + '+str(s)+' + '+str(p))
        elif s==0:
            print(str(q)+' + '+str(r)+' + '+str(p))
        elif r==0 and s==0:
            print(str(q)+' + '+str(p))
        else:
            print(str(q)+' + '+str(r)+' + '+str(s)+' + '+str(p))
    elif int(num)>=10000 and int(num) <100000:
        t=str(num)
        u=t[0]
        v=t[1]
        w=t[2]
        x=t[3]
        y=t[4]
        z=int(u)*10000
        aa=int(v)*1000
        ab=int(w)*100
        ac=int(x)*10
        if aa==0:
            if aa==0 and ab==0:
                print(str(z)+' + '+str(ac)+' + '+str(y))
            elif aa==0 and ac==0:
                print(str(z)+' + '+str(ab)+' + '+str(y))
            elif aa==0 and ab==0 and ac==0:
                print(str(z)+' + '+str(y))
            else:
                print(str(z)+' + '+str(ab)+' + '+str(ac)+' + '+str(y))
        elif ab==0:
            if aa==0 and ab==0:
                print(str(z)+' + '+str(ac)+' + '+str(y))
            elif ab==0 and ac==0:
                print(str(z)+' + '+str(aa)+' + '+str(y))
            elif aa==0 and ab==0 and ac==0:
                print(str(z)+' + '+str(y))
            else:
                print(str(z)+' + '+str(aa)+' + '+str(ac)+' + '+str(y))
        elif ac==0:
            if aa==0 and ac==0:
                print(str(z)+' + '+str(ab)+' + '+str(y))
            elif ab==0 and ac==0:
                print(str(z)+' + '+str(aa)+' + '+str(y))
            elif aa==0 and ab==0 and ac==0:
                print(str(z)+' + '+str(y))
            else:
                print(str(z)+' + '+str(aa)+' + '+str(ab)+' + '+str(y))
        else:
            print(str(z)+' + '+str(aa)+' + '+str(ab)+' + '+str(ac)+' + '+str(y))  

expanded_form(12)
expanded_form(42)
expanded_form(70304)

# Soal 3
def tower_builder(n_floors, block_size):
    w, h = block_size
    x=''
    for o in range(n_floors):
        for k in range(h):
            for c in range(w):
                x+=' * '
            x+='\n'
        w=w+4
    print(x)

tower_builder(3,(2,3))
tower_builder(6,(2,1))