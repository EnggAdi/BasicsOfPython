# IP address validation: To check if string provided can produce valid IP or not 
def is_valid(ip):
    ip = ip.split(".")
     
    # Checking for the corner cases
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                          int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
            i[0] == '0'):
            return False
             
    return True


#convert
def convert(s):     
    sz = len(s) 
    if sz > 12:
        return []
    snew = s
    l = []

    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]
                 
                if is_valid(snew):
                    l.append(snew)
                     
                snew = s
                 
    return l
IP_1 = "19216801"#"25525511135"
IP_2 = "190145"#"25505011535"
 
print("Output 1",convert(IP_1))
print("Output 2",convert(IP_2))

