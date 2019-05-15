f = open("demofile.txt", "r")
for x in f:
  print(x)
  
EOF: end-of-file is reached when read or readline returns an empty string. while (s != ""):
   s = f.readline()
   do_something
