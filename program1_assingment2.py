def break_test(sentence, k):
    words = sentence.split()

    broken_text = list()
    char_counter = -1
    current_words = list()
    index = 0
    while index < len(words):
        word = words[index]

        if len(word) > k:
            return None

        if char_counter + len(word) + 1 <= k:
            char_counter += len(word) + 1
            current_words.append(word)
            index += 1
        else:
            broken_text.append(" ".join(current_words))
            char_counter = -1
            current_words = list()

    broken_text.extend(current_words)
    return broken_text

sentence=input()
k=int(input())
print(break_test(sentence,k))
