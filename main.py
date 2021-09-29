import random
#written by @thedeaddan(https://thedeaddan.ddns.net)
#It works more stable on Python 3.9.1
death = [
'''
 =========''','''
    	
        |
        |
        |
        |
        |
 =========''','''
    +---+
        |
        |
        |
        |
        |
 =========''','''
    +---+
    |   |
        |
        |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
        |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']

words = ''' муравей бабуин барсук медведь бобр верблюд 
кошка моллюск кобра пума койот ворона олень собака осел 
утка орел хорек лиса лягушка коза гусь ястреб ящерица лама 
моль обезьяна лось мышь мул тритон выдра сова панда попугай 
голубь питон кролик баран крыса носорог лосось акула змея 
паук аист лебедь тигр жаба форель индейка черепаха ласка 
кит волк вомбат зебра'''.split(" ")

def get_random_word():
	return words[random.randint(0,len(words)-1)].replace("\n","")
def lock_word(word):
	locked_word = ""
	for i in range(len(word)):
		locked_word += "*"
	return locked_word
def change(word,num,letter):
	word_dic = []
	ch_word = ""
	j = 0
	for i in range(0,len(word)):
		if i == num:
			word_dic.append(letter)
		else:
			if word[i] == "*":
				word_dic.append("*")
			else:
				word_dic.append(word[i])
	for i in word_dic:
		ch_word = ch_word + i
	return ch_word
print("Игра Висельница\n")
while True:
	print("Суть игры заключается в том, что вы угадываете слово по одной букве\nи с каждой ошибкой вы будете всё ближе к смерти!\n")
	print("У вас 10 попыток. Удачи ;)\n")
	word = get_random_word()
	locked_word = lock_word(word)
	org_locked_word = locked_word
	attempt = 0
	bads = 0
	print("Готовы играть? (Да/Нет)")
	back = input()
	if "н" in back.lower():
		break
	while True:
		print("Введите предполагаемую букву: ")
		letter = input().lower()
		num = 0
		if letter in word:
			for i in word:
				if i == letter:
					locked_word = change(locked_word,num,letter)
				num += 1
		else:
			print("\n Думайте лучше, вы в "+str(int(9-bads))+" шагах от смерти!\n")
			print(death[bads])
			bads += 1
		if bads == 10:
			print("Вас повесили!!! Вы проиграли!")
			break
		attempt += 1
		print(locked_word)
		if locked_word == word:
			print("Вы выйграли!!! Всего попыток: "+str(attempt))
			break
	print("Хотите ли поиграть ещё? (Да/Нет)")
	back = input()
	if "н" in back.lower():
		break
