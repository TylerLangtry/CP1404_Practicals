sentence = input("Enter sentence: ").lower()
sentence_dict = {}

sentence_list = sentence.split(" ")

for i in range(len(sentence_list)):
    count = 0
    for j in range(len(sentence_list)):
        if sentence_list[i] == sentence_list[j]:
            count += 1
    sentence_dict[sentence_list[i]] = count

print("Text: " + sentence)

for i in sentence_dict:
    print("{} : {}".format(i, sentence_dict[i]))
