import hashlib
flag = 0
counter = 0
print("-----------------------------------------------------------")
print('''
██╗███████╗ █████╗ ██████╗  ██████╗ ██████╗ https://github.com/IZABOD
██║╚══███╔╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
██║  ███╔╝ ███████║██████╔╝██║   ██║██║  ██║ 
██║ ███╔╝  ██╔══██║██╔══██╗██║   ██║██║  ██║
██║███████╗██║  ██║██████╔╝╚██████╔╝██████╔╝
╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═════╝ 
                                            ''')
print("-----------------------------------------------------------")

pass_hash = input(">>>Enter md5 hash<<<: ")
wordlist = input(">>>File name<<<: ")
try:
    pass_file = open(wordlist, "r")
except:
    print("No file found!!")
    quit()
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    # print(word)
    # print(digest)
    # print(pass_hash)
    counter += 1
    if digest == pass_hash:
        print('''
-----------------------------------------------------------        
                                      88          
                              ""   ,d     
                                   88     
8b      db      d8 ,adPPYYba, 88 MM88MMM  
`8b    d88b    d8' ""     `Y8 88   88     
 `8b  d8'`8b  d8'  ,adPPPPP88 88   88     
  `8bd8'  `8bd8'   88,    ,88 88   88,    
    YP      YP     `"8bbdP"Y8 88   "Y888  
-----------------------------------------------------------''')
        print("Password found!!!")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("MD5 Hash used: " + pass_hash)
        print("passowrd is: " + word)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        flag = 1
        break
if flag == 0:
    print("password not found")
