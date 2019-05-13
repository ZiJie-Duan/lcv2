import uuid

uidlist = []
for x in range(30):
    a = uuid.uuid4()
    uidlist.append(str(a))

print(uidlist)