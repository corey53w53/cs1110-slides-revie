def after_at(s):

    temp=s.split("@")
    if len(temp)==1:
        return []
    afters_list = temp[1:]
    if len(afters_list) == 1:
        if afters_list[0]=='':
            return [] 
        else:
            return [afters_list[0]]
    return_list = []
    print(afters_list)
    for s in afters_list: 
        new_s=''
        if s[0]!=' ':
            keep_running=True
            for char in s:
                if char!=' ' and keep_running:
                    new_s+=(char)
                else: keep_running=False
        if not new_s in return_list and new_s!='':
            return_list.append(new_s)
    return return_list
print(after_at("@martha @Martha @martha"))