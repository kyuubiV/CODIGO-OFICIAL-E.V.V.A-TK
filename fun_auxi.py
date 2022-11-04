def d(x):
 if x==1:
   print("\033[35m*¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨*".center(60))
 elif x==2:
  print("\033[1;31m*¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨*".center(60))
 elif x==3:
  print("\033[1;36m*¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨*".center(60))
 elif x==4:
   print("\033[1;94m*¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨*".center(60))
 else:
  print("\033[1;33m*¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨°¨¨¨¨¨*".center(60))
   
def load():
  import time
  import os
  print('\033[0;49;94mCARREGANDO')
  time.sleep(1)
  os.system('clear')
  print('\033[0;49;31mCARREGANDO .')
  time.sleep(0.5)
  os.system('clear')
  print('\033[0:49;32mCARREGANDO ..')
  time.sleep(0.5)
  os.system('clear')
  print('\033[0:49;33mCARREGANDO :.')
  time.sleep(0.5)
  os.system('clear')
  print('\033[0:49;34mCARREGANDO ::')
  time.sleep(0.5)
  os.system('clear')
  print('\033[0:49;35mCARREGANDO .')
  time.sleep(0.5)
  os.system('clear')
  print('\033[0:49;31mCARREGANDO ..')
  time.sleep(0.5)
  os.system('clear')
  print('\033[0:49;32mCARREGANDO :.')
  time.sleep(0.5)
  os.system('clear')
  print('\033[0:49;33mCARREGANDO ::')
  time.sleep(0.5)
  os.system('clear')
def txt(titu,y):
  
 d(y)
 print(titu.center(55)) 
 d(y)