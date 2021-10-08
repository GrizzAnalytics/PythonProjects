import sys

alphabets_list = []
for i in range(26):
	alphabets_list.append(str(chr(97 + i)))


def get_word_pattern(word):
	number_of_letter = 0
	letter_dict ={}
	word_pattern = []
	for letter in word:
		if letter not inletter_dict:
			letter_dict[letter] = str(number_of_letter)
			number_of_letter += 1
		word_pattern.append(letter_dict[letter])
	word_pattern_str = '.'.join(word_pattern)
	return word_pattern_str

word_file = open("dictionary.lst", 'r')
word_dictionary = dict()
for line in word_file.readlines():
	word = line.lower().strip()
	word_pattern_str = get_word_pattern(word)
	if word_pattern_str not in word_dictionary.keys():
		word_dictionary[word_pattern_str] = []
	word_dictionary[word_pattern_str].append(word)

cipher_text = raw_input()