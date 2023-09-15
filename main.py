def int1():
  print('INTERFACE 1')
  print()
  title = '\033[31m=' + '\033[0m=' + '\033[34m=' + '\033[1;33m  Music App  ' + '\033[34m=' + '\033[0m=' + '\033[31m='
  print(f'\033[1m{title:^100}\033[0m')
  print()
  
  a = '🔥▶️  Radio Gaga.'
  print(f'{a:^45}')
  b = 'Queen'
  print(f'\033[1;33m{b:^46}\033[0m')
  print()
  print()
  
  c = 'PREV'
  d = 'NEXT'
  e = 'PAUSE'
  print(f'''
  {c:^36}
  \033[32m{d:^48}
  \033[1;35m{e:^62}\033[0m
  ''')


def int2():
  print()
  print()
  print('INTERFACE 2')
  print()
  f = 'WELCOME TO'
  print(f'{f:^70}')
  e = '\033[34m--     ARMBOOK     --'
  print(f'{e:^76}')
  print()
  
  a = 'Definitely not a rip off of'
  b = 'a certain other social'
  c = 'networking site.'
  print(f'''
  \033[1;33m{a:^80}
  {b:^85}
  {c:^90}\033[0m
  ''')
  print()
  
  g = 'Honest.'
  h = 'Username:'
  i = 'Password:'
  print(f'\033[1;31m{g:^70}')
  print()
  print(f'\033[0m{h:^69}')     
  print(f'\033[0m{i:^69}') 

int1()
int2()
