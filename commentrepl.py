comments=[]
new_comment = "a"
print ("Previously entered comments:")
for x in comments:
    print(x)
while new_comment!= " ":
    new_comment = input("Enter your comment:")
    if new_comment != " ":
        # https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
        from hashlib import sha256

        def create_hash(password):
            pw_bytestring = password.encode()
            return sha256(pw_bytestring).hexdigest()

        pw1 = input('Please enter your password:')
        hsh1 = create_hash(pw1)
        hsh2 = "9d777935627a29c77604c57273520eb42635fd1847d2eeea1e7441fbaeb26253"
        if hsh1 == hsh2:
            comments.append(new_comment)
            print ("Previously entered comments:")
            i=1
            for x in comments:
                print("%d.%s" %(i , x))
                i=i+1
        else:
            print ("You can't make a comment, password is wrong!")
