command_switch = {
  'abc' : lambda params: print('ABC(╹◡╹)')
, 'hoge': lambda params: print('HOGE(´・ω・｀)')
, 'xyz' : lambda params: print('XYZ(；・∀・)')
, "test": lambda params: {
            print('params: ', params)
          }
, 'help': lambda params: {
            print('aaa'),
            print('bbb')
          }
}

while 1:
  print('farming-system\n  << ', end='')
  input_line = input().split()
  try:
    command = input_line[0]
    
    if command == 'exit':
      break
    
    del input_line[0]
    params  = input_line
    command_switch[command](params)
  except:
    print('command `' + command + '` is not found. (`help` to see help.)')
