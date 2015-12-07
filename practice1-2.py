def maxtomin(lst):
    mx=lst[0]
    mn=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>mx:
            mx=lst[i]
        if lst[i]<mn:
            mn=lst[i]
    result=[mx,mn]
    return result