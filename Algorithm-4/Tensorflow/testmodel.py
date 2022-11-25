import tensorflow as tf
import numpy as np

# load model
model = tf.keras.models.load_model('poem.h5')
tokenizer = tf.keras.preprocessing.text.Tokenizer()

data = open('new_poem.txt').read()

corpus = data.lower().split("\n")

tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in corpus:
	token_list = tokenizer.texts_to_sequences([line])[0]
	for i in range(1, len(token_list)):
		n_gram_sequence = token_list[:i+1]
		input_sequences.append(n_gram_sequence)

# pad sequences 
max_sequence_len = max([len(x) for x in input_sequences])

while True:
    # ask for user input
    seed_text = input("Enter seed text or 'q' to quit: ")

    # break if user enters 'q'
    if seed_text == 'q':
        break

    # ask for number of words to generate
    next_words = int(input("Enter number of words to generate: "))

    # generate text
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = tf.keras.preprocessing.sequence.pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    print(seed_text)


