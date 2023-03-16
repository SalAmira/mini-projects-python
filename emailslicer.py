email= input("Enter your email:")
slicee = email.index("@")
username=email[:slicee]
domain=email[slicee:]
print(f"your username is {username} and domain is {domain}")