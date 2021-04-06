def avail_check(emailid):
    if (emailid in email_ids ):
        return True
    else:
        return False
email_ids=["gopi@123","gopi@1234","gopi@12345"]
email=input("Enter your email ID ")
res=avail_check(email)
print(res)