string = ['   ', '  *', ' * ', ' **', '*  ', '* *', '** ', '***']
dic = ['25755', '65656', '25452', '65556', '74647',
       '74644', '34553', '55755', '72227', '31152',
       '56465', '44447', '57775', '57755', '75557',
       '75744', '75577', '65655', '34216', '72222',
       '55557', '55552', '55575', '55255', '55522',
       '71247']
n = input()
for i in range(5):
    print('  '.join([string[int(dic[ord(k) - ord('A')][i])] for k in n]))

