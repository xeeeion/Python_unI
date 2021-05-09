horses = []

def do_bet(horse, do_bet):
    if do_bet == 0 or horse in horses or horse > 10 or horse <= 0:
        print("Что-то пошло не так, попробуйте ещё раз")
        return
    else:
        print("Ваша ставка в размере", do_bet, "на лошадь", horse, "принята")
        horses.append(horse)
        return
