from collections import Counter
list1=list()
list2=list()
list1=['192.168','192.168','192.168','192.166','192.168','166.122']
dic={}

result=Counter(list1)
print result
print type(result)
for key in list1:
    dic[key]=dic.get(key,0)+1
print dic
for key in dic:
    print ("%s count=%s")%(key, dic[key])
for key in list1:
    dic[key]=dic.get(key,0)+1
print dic
for key in dic:
    print ("%s count=%s")%(key, dic[key])

    #print ("%s count=%s " %(key,value))

