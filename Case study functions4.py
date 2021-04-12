def login_page(userid,passw):
	if (userid in data_name and passw in data_passw):
		return True
	else:
		return False
data_name=["g","k"]
data_passw=["1","10"]
res=login_page(input("Enter User Name"),int(input("Enter password")))
print(res)