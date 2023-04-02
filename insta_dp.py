import instaloader as i

ig=i.Instaloader()
pp=input("Enter Your userName: ")


ig.download_profile(pp,profile_pic_only=True)
