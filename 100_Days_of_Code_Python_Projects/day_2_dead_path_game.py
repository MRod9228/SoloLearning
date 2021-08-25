#based on d3l36
import time
print('''
*******************************************************************************
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----)
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((   \X\/X/    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))  /X/\X\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \ /      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------)
 \_/__________________________________________________________________/
*******************************************************************************
''')


left = 'Left'
right = 'Right'
forward = 'Forward'
backward = 'Backwards'

print('Welcome to a 2 steps game. Choose correct = You live / Choose wrong = You die! ')
print('You wake up with four trails sorrounding you.')
print('There is only one way out, the other three lead to your dead, good luck!')
answer = input('Which way would you like to go? Left, Right, Forward, Backwards: ' )
print(f'You choose the {answer} path. Good Luck!')
if answer == left:
    print('You choose left but hesitated and a coconut fell on you!---You are...Dead?')
elif answer == right:
    print('You moved to the right and a snake that was on the ground poison you!---You will be dead in 5 seconds---Good Bye')
elif answer == forward:
    print('You moved forward unafraid and fainted after seeing your mother in law!---BUT you survived [CONGRATULATION]')
elif answer == backward:
    print('You moved backwards and fell on a spike trap!--- Sorry, you died.')
else:
    print('Wrong selection! You were eaten alive!!!')
count_down = 10
print('Closing in: '+ str(count_down)+'seconds.')


while count_down != 0:
    print(count_down)
    count_down-=1
    time.sleep(1)
print('BYE')
time.sleep(.3)