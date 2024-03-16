username=input('enter your username' )
password=input('enter your password')
if username or password is not 'admin':
  print('wrong username or password')
if username and password is 'admin':
  print('succesfully login')