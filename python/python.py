texminlerin_sayi = 0
bilinmeyen_reqem = 5
texminlerin_limiti = 3

while texminlerin_sayi < texminlerin_limiti:
    texmin = int(input('Texmin: '))
    texminlerin_sayi += 1
    if texmin == bilinmeyen_reqem:
        print('sen qazandin')
        break
else:
    print("sen uduzdun")

