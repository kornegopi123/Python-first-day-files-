
class Doctor:
    
    def __init__(self,doc_id,uname,passw,fname,lname,special):
        self.doc_id=doc_id
        self.uname=uname
        self.passw=passw
        self.fname=fname
        self.lname=lname
        self.special=special
    
    def verifyCredential(self,uname,passw):
        if(self.uname==uname) and (self.passw==passw):
            return True
        else:
            return False
    
    def display(self):
        print(self.doc_id,'\n',
        self.uname,'\n',
        self.passw,'\n',
        self.fname,'\n',
        self.lname,'\n',
        self.special)
    
doct1=Doctor(123,'gopi',9908,'korne','gopi','dentist')
print(doct1.verifyCredential('gopi',9908))
print()
doct1.display()


class Appointment:
    
    def __init__(self,appoint_id,appoint_time,appoint_date):
        self.appoint_id=appoint_id
        self.appoint_time=appoint_time
        self.appoint_date=appoint_date
         
        
    def appoint_avilable(self,appoint_id,appoint_time,appoint_date):
        if(self.appoint_id==appoint_id) and (self.appoint_time==appoint_time) and (self.appoint_date==appoint_date):
            print("Appointment Availble")
            return True
        else:
            print("Appointment not avilable")
            return False

appoint1=Appointment(233,12,'12-04-21')
print(appoint1.appoint_avilable(233,12,'12-04-21'))

appoint2=Appointment(234,9,'12-04-21')
print()
print(appoint2.appoint_avilable(234,12,'12-04-21'))

class Prescription:
    
    def description(self,disease):
        print("You are suffering with  ",disease)
    def medcines(self,med_list):
        print("You have to use this medicines regularly for few days ",med_list)
presc1=Prescription()
print()
presc1.description("fever")
presc1.medcines("Dolo 650 one pill per every 6 hours if you feel temperature will be high take 2 pills")

class Review:
    def write_review(self,review):
        print(review)
review1=Review()
print()
review1.write_review("some review about doctor consultation")
           