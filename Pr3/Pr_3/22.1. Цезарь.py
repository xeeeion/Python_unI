l_letter = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы',
        'ь','э','ю','я']
b_letter = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы',
        'Ь','Э','Ю','Я']

def encrypt_caesar(msg,shift):
    ret = ""
    for x in msg:
        if x in l_letter:
            ind = l_letter.index (x) % len (l_letter)
            ret += l_letter[(ind + shift) % len (l_letter)]
        elif x in b_letter:
            ind = b_letter.index (x) % len (l_letter)
            ret += b_letter[(ind + shift) % len (l_letter)]
        else:
            ret += x
    return ret


def decrypt_caesar(msg,shift):
    ret = ""
    for x in msg:
        if x in l_letter:
            ind = l_letter.index (x)
            ret += l_letter[ind - shift]
        elif x in b_letter:
            ind = b_letter.index (x)
            ret += b_letter[ind - shift]
        else:
            ret += x
    return ret
