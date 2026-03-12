sentence = "Sample sentence for frequency count and this sentence is just a sample taken by me "
words = sentence.split()
freq = {}
for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

print("Word Frequency Dictionary:", freq)