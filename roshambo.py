#Rock beats scissors. Scissors beats paper. Paper beats rock.
pONE=str(input("Player one enter Rock, Paper, or Scissors: ")).lower()
pTWO=str(input("Player two enter Rock, Paper, or Scissors: ")).lower()
#
def cmp(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(cmp(pONE, pTWO))
