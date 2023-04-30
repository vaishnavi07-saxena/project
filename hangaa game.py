'''Hangman game:
A row of dashes represents the word to guess. If the player guesses a letter in the word, the
script writes it in all its correct positions. The player has 10 turns to guess the word. You can easily
customize the game by changing the variables. '''






import random
words='''baboon badger bear beaver camel clam cobra cougar objective crackerjacks subway symptom grammaticalized
       coyote donkey eagle ferret goose hawk lion lizard llama monkey moose mouse mule newt hypercicvilised 
       parrot pigeon python rabbit raven rhino salmon seal shark sheep commercialising overemphasizing
       skunk sloth pscychology stork tiger toad trout turkey turtle friendship everything appreciate
       weasel whale wolf wombat zebra python sambahv hangman dazzling strawberry motivation'''.split()

word=list(words)

ans=random.choice(word)
print(ans)

l=[ans]
o=['_']*len(ans)
c=0

print('start guessing the word of length-->', len(ans))
print()
print(*o)
a=['  o','  o\n /','  o\n /|','  o\n /|\\','  o\n /|\\\n  |','  o\n /|\\\n  |\n /','  o\n /|\\\n  |\n / \\']
while(c<8):
    print('REMAINING CHANCE =',7-c)
    out=input()

    if out in ans:
        for i in range(len(ans)):
            if ans[i]==out:
                o.pop(i)
                o.insert(i,out)

        print(*o)

    else:

        print(a[c])
        c+=1
        if c==7:
            print('u could not save the man')
            break

    out=[i for i in o if i!='_']
    if len(out)==len(ans):
        print('HURRAH! U WON')
        break
    else:
        continue   
