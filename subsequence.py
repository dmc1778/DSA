def isSubsequence(s: str, t: str) -> bool:        
        s = list(s)
        temp = {}
        order_flag = []
        flag = False
        final = []
        for token in list(t):
            if token in s:
                temp[token] = 1
                order_flag.append(token)
        new_s = [v for k,v in temp.items()]
        if all(new_s) == 1 and len(new_s) == len(s):
            if "".join(s) == "".join(order_flag):
                flag = True
        return flag
isSubsequence("ca", "accaab")