letter = input()
data = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
one = ' * **  * ** ****** *** **** *** **  * ** ************  ******'
one += ' ** ** ** ** ****'
two = '* ** ** ** **  *  *  * * *   *** *  ******* ** ** ** '
two += '**   * * ** ** ** ** *  *'
three = '***** *  * *** ** * **** *   **  *  ******* ***** *** '
three += ' *  * * ** ** * * * * * '
four = '* ** ** ** **  *  * ** * * * *** *  **** ** **  ****'
four += ' *  * * * ** ***** * * *  '
five = '* ***  * ** ****   *** **** * * ***** ** *****  **** '
five += '***  * *** * * ** * * ***'
for el in letter:
    h = data.find(el, 0)
    print(one[h * 3:h * 3 + 3], end='  ')
print('')
for el in letter:
    h = data.find(el, 0)
    print(two[h * 3:h * 3 + 3], end='  ')
print('')
for el in letter:
    h = data.find(el, 0)
    print(three[h * 3:h * 3 + 3], end='  ')
print('')
for el in letter:
    h = data.find(el, 0)
    print(four[h * 3:h * 3 + 3], end='  ')
print('')
for el in letter:
    h = data.find(el, 0)
    print(five[h * 3:h * 3 + 3], end='  ')
print('')
