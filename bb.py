
fo = open("foo.txt","r+")
fo.write("TSC Bhola")
print ("Current pointer Position: ",fo.tell() )
fo.seek (0,0)
print ("Current pointer after reset: ",fo.tell()) 
str1 = fo.read(13)
print ("String 1 is", str1 )

fo.close()