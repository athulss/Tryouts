import datetime
x=876542319012265423
y=654231901213474839
starttime=datetime.datetime.now()
def gcd(x,y):
    if(x>y):
        if(x%y==0):
            return y
        else:
            a=x%y
            if(a<y):
                return gcd(y,a)
            else:
                return gcd(a,y)
b=gcd(x,y)
print(b)
endtime=datetime.datetime.now()
print(endtime-starttime)
