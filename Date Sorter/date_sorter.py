import pandas as pd
import re

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df[154]
from dateutil import parser
from datetime import datetime
def date_sorter():
    d=pd.DataFrame(df,columns=["Date"])
    d["Dat"]=None
    d["y"]=None
    d["m"]=None
    d["d"]=None
    d["fd"]=None
    l=len(d)      
        
    q0=r"(\d{1,2}[/.,-]\d{1,2}[/-]\d{2,4})[=]*"
    q1=r"(\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.-/,]* \d{4})"
    q2=r"[(]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})[)]"
    q3="(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})[\n.]"
    q4=r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[., /]*\d{1,2}[. ,/]*\d{4})"
    q5=r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,/ ]*\d{4})"
    q6=r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-,/.]* \d{1,2}[-/,.]* \d{4})"
    q10=r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-, /]*\d{1,2}[-/, .]*\d{4})"
    q7= r"(\d{1,2}[.,/-]\d{4})"
    q8= r"(\d{4})"
    q9=r"(\d{1,2}(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.-/,]* \d{4})"

    z=d.columns.get_loc("Date")
    for i in range(len(d)):
        if re.search(q0,d.iat[i,z]) is not None:
            q=q0
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date

        elif re.search(q1,d.iat[i,z]) is not None:
            q=q1
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date
            d.Dat[i]=d.Dat[i].strip(").,(=\n ")
            d.Dat[i]=d.Dat[i].replace(" ",'/')
            d.Dat[i]=d.Dat[i].replace(",",'/')
            d.Dat[i]=d.Dat[i].replace("-",'/')
            d.Dat[i]=d.Dat[i].replace("ruary","")
            x=d.Dat[i].split("/")
            x[0]=x[0].strip(" .")
            d.d[i]=(x[0])
            d.m[i]=(x[1])
            if x[2] == "":
                d.y[i]=(x[3][-2:])
            else:
                d.y[i]=(x[2][-2:])
        elif re.search(q9,d.iat[i,z]) is not None:
            q=q9
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date
            d.Dat[i]=d.Dat[i].strip(").,-(=\n ")
            d.Dat[i]=d.Dat[i].replace(" ",'')
            d.Dat[i]=d.Dat[i].replace(",",'/')
            d.Dat[i]=d.Dat[i].replace("-",'/')
            d.Dat[i]=d.Dat[i].replace("-","/")
            x=d.Dat[i].split("/")
            d.d[i]=(x[0])[0]
            d.m[i]=(x[0])[1:]
            d.y[i]=x[1]
        elif re.search(q2,d.iat[i,z]) is not None:
            q=q2
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        elif re.search(q3,d.iat[i,z]) is not None:
            q=q3
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        elif re.search(q4,d.iat[i,z]) is not None:
            q=q4
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        elif re.search(q10,d.iat[i,z]) is not None:
            q=q10
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        elif re.search(q6,d.iat[i,z]) is not None:
            q=q6
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        elif re.search(q10,d.iat[i,z]) is not None:
            q=q10
            date=re.search(q,d.Date[i]).group()
            d.Dat[i]=date

        elif re.search(q7,d.iat[i,z]) is not None:
            q=q7
            date="1/"+re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        elif re.search(q5,d.iat[i,z]) is not None:
            q=q5
            date="1/"+re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        elif re.search(q8,d.iat[i,z]) is not None:
            q=q8
            date="1/1/"+re.search(q,d.Date[i]).group()
            d.Dat[i]=date
        
        if q==q5 or q==q8 or q==q7:
            
            d.Dat[i]=d.Dat[i].strip(").,(=\n ")
            d.Dat[i]=d.Dat[i].replace(" ",'/')
            d.Dat[i]=d.Dat[i].replace(",",'/')
            d.Dat[i]=d.Dat[i].replace("-",'/')
            d.Dat[i]=d.Dat[i].replace("ruary","")
            x=d.Dat[i].split("/")

            try:
                x[0]=x[0].strip(" .")
                if x[1].isalpha():

                    d.d[i]=(x[0])
                    d.m[i]=(x[1])
                    if x[2] == "":
                        d.y[i]=(x[3][-2:])
                    else:
                        d.y[i]=(x[2][-2:])
                else:
                    d.d[i]=(x[0])
                    d.m[i]=(x[1])
                    if x[2] == "":
                        d.y[i]=(x[3][-2:])
                    else:
                        d.y[i]=(x[2][-2:])
            except:
                d.d[i]=1
                d.m[i]=x[0]
                d.y[i]=x[1][-2:]
                
        elif q==q0 or q==q2 or q==q3 or q==q4 or q==q6 or q==q10:
            
            d.Dat[i]=d.Dat[i].strip(").,(=\n ")
            d.Dat[i]=d.Dat[i].replace(" ",'/')
            d.Dat[i]=d.Dat[i].replace(",",'/')
            d.Dat[i]=d.Dat[i].replace("-",'/')
            d.Dat[i]=d.Dat[i].replace("ruary","")
            x=d.Dat[i].split("/")

            try:
                x[0]=x[0].strip(" .")
                if x[1].isalpha():

                    d.d[i]=(x[0])
                    d.m[i]=(x[1])
                    if x[2] == "":
                        d.y[i]=(x[3][-2:])
                    else:
                        d.y[i]=(x[2][-2:])
                else:
                    d.d[i]=(x[1])
                    d.m[i]=(x[0])
                    if x[2] == "":
                        d.y[i]=(x[3][-2:])
                    else:
                        d.y[i]=(x[2][-2:])
            except:
                d.d[i]=1
                d.m[i]=x[0]
                d.y[i]=x[1][-2:]


    for i in range(len(d.Dat)):
        d.m[i]=d.m[i].replace("January","1").replace("ruary","").replace("aury","").replace("emeber","").replace("Feburary","2").replace("March","3").replace("April","4").replace("May","5").replace("June","6").replace("July","7").replace("August","8").replace("September","9").replace("septem","9").replace("October","10").replace("November","11").replace("December","12")       
        d.m[i]=d.m[i].replace("Jan","1").replace("Feb","2").replace("Mar","3").replace("Apr","4").replace("May","5").replace("Jun","6").replace("Jul","7").replace("Aug","8").replace("Sep","9").replace("Oct","10").replace("Nov","11").replace("Dec","12")

        try:
            c=int(d.m[i])
        except:
            d.m[i]=d.m[i].strip(". ")
        if int(d.m[i])>12:
            t=d.m[i]
            d.m[i]=d.d[i]
            d.d[i]=t
        d.fd[i]="-".join([str(d.m[i]),str(d.d[i]),str(d.y[i])])

    d["fd"] = pd.to_datetime(d["fd"])
    s=pd.Series((d.fd.sort_values()).index,index=d.index)
    pd.set_option('display.max_rows', None)
    return s#d.set_index(["y"]).sort_index()

date_sorter()