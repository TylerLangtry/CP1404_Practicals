
sentence = input("Enter sentence: ").lower()
sentence_dict = {}
word_len = 0

sentence_list = sentence.split(" ")

for i in range(len(sentence_list)):
    count = 0
    if len(sentence_list[i]) > word_len:
        word_len = len(sentence_list[i])

    for j in range(len(sentence_list)):
        if sentence_list[i] == sentence_list[j]:
            count += 1
    sentence_dict[sentence_list[i]] = count

print("Text: " + sentence)

for key, value in sorted(sentence_dict.items()):
    print("{:{}} : {}".format(key, word_len, sentence_dict[key]))
    