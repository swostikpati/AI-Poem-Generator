# FINAL PROJECT - AI POEM GENERATOR
***by Swostik Pati and Prince Ampofo***

## Introduction
Our project is based on the idea of using algorithms to generate new poems using the existing poems in book The Thousand and one Nights. The algorithms used span from simple programs to complex ones built on machine learning and artificial intelligence. Our final goal is to consistently produce new poems using both types of algorithms and then compare their results in the end. In the end, we also analyze how machine-generated poems compare against human-composed ones. The poems that we are using are taken from the following chapters of the book: 

## Motivation
Programming and AI are powerful tools that humans have designed. We keep speculating about the fact how soon machines will reach the peak of human intelligence and surpass us. Even though the present level of progress is convincing, but we are still far away from seeing machines being as capable and intelligent as us. This is because the human intelligence is made from much more than just knowledge that can be fed into a computer - it is made up of creativity, of innovation so powerful that is capable of designing such AI technologies to begin with. 

Poems and stories are one area where immense creativity is required to craft them and we wanted to use our self-implemented algorithms to test the creativity of machines in building those. Another intriguing motivation behind our project is just the thought that what if Anton Galland had access to the program - how would he have used it to produce more poems (and even stories) to keep publishing more books.

## Data Collection and Filtering
We started out by extracting the poems out of the chapters and segregated them into separate files. We then thought of writing a small program to remove all the punctuation characters and convert all the characters into lowercase letters and run the text through the program. But finally we decided against it in the initial steps and instead thought of running the final generated poem through the program instead to decrease the number of times the program will be run and thereby increase the efficiency of the algorithm. So the text from the poems that were extracted from the book were directly used in the different algorithms after some pre-processing that is specific to each algorithm.

## Implementation

### Initial Algorithm (#1) - Tagged words
The initial algorithm that we designed to just test things out was a very simple random-choice algorithm. The way we derived at this algorithm was when we were going through a random story generation algorithm. We tried it out by generating some lines of a random story. These were some of the lines that we got while initially learning to implement the algorithm:
“In the 20 BC there was a man named Jack. One full-moon night he was going for a picnic to  the garden he saw a man who seemed to be in late 20s searching something.”
Using our learnings from the implementation of the story algorithm, we expanded the code to run poems. We took some words out of the poem and tagged them based on subject, actions, and random phrases. From these tagged lists of words, we randomly picked words and formed verses of the poem. We used to run the code in a loop to generate multiple such lines to form the final poem.

These are some of the ones that we managed to generate:

***“sun caresss whole
life love crave and desire
sun caresss company
I love eternal
I admire company 
life love whole”***  

#### Problems and Possible Improvements
The program didn’t seem to give decent results at all while using it for poems even though the results from the story generator were much more convincing. The reason for this might be the fact that it is much more difficult to tag words of existing poems into different categories, especially when there are so many ways of writing styles.

There was also a problem with the repetition of words in the poem. We realized this could be mitigated by including more words and removing the used words from the tagged lists.

Another possible improvement is to give more power to the user to customize the poem they want to generate - in terms of both the number of lines of the poem they want to generate and the number of words per line.

### Algorithm #2 - Randomized and Customizable
Taking our understanding from the failures of the first program, we created another program where we made sure to mitigate the problems of the first algorithm. This time instead of tagging words, we thought of going forward with a completely randomized algorithm, but made sure to not repeat words. To do this, we simply copied all the words from the poems into separate lists and then started combining words from the lists separately. Every time we used a word, we simply removed that from the list to prevent repetitions. We also gave the user some power to customize the number of words and number of lines they want to generate. These are some snippets from the poems that are generated by the algorithm:

(5 lines and 5 words per line)

***“I face turning back have  
I not wept for will  
suffer your neglect as hunger   
have not had kind to  
contempt hard to the time ”***

(7 lines and 4 words per line)

***“pain wore laid within  
my wet love hid  
by tell-tale sobs  
hard agony cause remedy  
a game of many  
fine souls meet blade  
will Love nor seek”***

#### Comparison with the initial algorithm
This algorithm seemed to produce much better results than our initial algorithm. The user customization allows us to see different poems of completely different types. Even though the poems sound still coarse, they have a very wide range of words that they are created from and are completely repetition free. 
One important thing to consider though is the fact that due to the random nature of the algorithm, the poems generated aren’t quite built around a specific theme and rather convey different and sometimes conflicting emotions. They also lack a proper sentence structure as yet again, the concatenated words are based on complete randomness.

### Algorithm #3(a) - GPT-J AI Model - I (Pytorch)
The field of machine learning allows for the training and finetuning of models on specific tasks. With that said, we decided to train a model on a list of poems from A thousand and one night stories. First of all, we had to tag poems as love, pleasure, lust, sadness, frustration, etc. These poems and tags are stored in a JSON file - poemTags.json. It is worth noting that one poem may have several tags. A picture of the raw dataset can be found below:


We then proceed by transforming this dataset into a form that can be understood by the model. We do this by writing a python script, json_to_csv.py. This script does two things -the first is to flatten the json and randomly shuffle the data. The second is to divide the flattened JSON into 80% training and 20% validation dataset and store these as CSV(poem_train.csv and poem_validation.csv) files. There are “<|endoftext|>” markers at the end of each line. Each line is of the form “<|endoftext|>tags:poem<|endoftext|>”. Find an image of the flattened data set below ;



After that, we feed this data to the model for fine-tuning. The size of the model after fine-tuning is approximately 72.6 GB. We then test this model by giving it a poem tag as an input and the model outputs a poem. Find some examples below;

Lust

***“The term 'lust' comes from the Latin word for life,  
a life that one lives through anOther.  
The word 'lust' is also used to describe attraction  
The attraction that exists between two individuals.”***

Pleasure 

***“The pleasure you get from a single book  
is like the pleasure of looking at a single flower  
it's perfectly real, and it's gone in an instant.  
But the pleasure you get from reading a handful  
is more like what you get from eating a handful of pe”***

Sadness 

***“I am a human being.  
I have been in your shoes and in someone else’s shoes.  
I have had experiences that were the most painful in my life.  
There have been days when I have cried for hours at a time,  
and days were I haven”***

#### Problems and Possible Improvements
First of all, the model GPT-J being used has already been trained with over 6 billion parameters. We are only fine-tuning this model to generate a poem. Hence, the model might not produce poems specific to a thousand and one-night stories. This is because the model has already been trained with several other datasets.
The output limit of the model affects the accuracy of the poem. In order for the model to give you an output when giving an input tag, you need to specify its output limit which corresponds to the number of characters the model should output. After testing, we realized that if we increase the output parameter, the model turns to generate general sentences but if lowered it gives accurate poems. This might be due to the fact that the poems being fed to it are shorter in length.
Improvements can also be made by fine-tuning the model on more datasets. Currently, we have only 89 datasets which aren’t enough for the model to learn how to generate accurate poems.

### Algorithm #3(b) - GPT-J AI Model - II (Pytorch)
Algorithm 3(a)’s responses were very generalized even after training it with the entire dataset we created using just poems from The Thousand and One Nights. This was because as explained above, the training was overshadowed by the amount of previous data that the model was trained on. Therefore, just putting the tagged words as input in the model didn’t help at all as the words were quite generic and hence, generated generic responses. Just when we thought that this was a complete failure, we thought of experimenting with just a last thing - we tried the entire poems as inputs and tried to check if the model was able to extend the existing poems. This seemed to do work much better than the last algorithm in some cases, where the model maintained the cohesiveness of the poems. Some examples are:

***“For pleasure, find these four: Zither, lute, harp and flute.  
Pair them with four more: Myrtle, clove, blossom, rose.  
Four you must include: Wine, a lover, gold, and youth.  
Three you must use: Fire, a mother, and a friend.  
Three you must avoid: Vine, a father, and a horse.”***

***“How fine is the forgiveness of the strong  
And finer when it falls on weaker hearts  
If friendship ever was a sacred bond  
Do not cast off the first friend for the last  
I dare say that she may stand by you forever”

The primary reason for the change in responses was because of the specific input statements we provided, which sort of made the model focus much more on the dataset that we trained by putting more weight on it overshadowing the previous datasets that it was already trained on. The poems extended by this algorithm all have an element of The Thousand and One Nights and are extended from there. A very interesting thing to note here is the way the model has kept the sentence structure consistent (to an extent) while extending the poem. Our conclusion here is that the model works fairly well in extending poems when the input given is specific to our dataset.

### Final Algorithm (#4) - AI Model Trained from Scratch (Tensorflow)
Even though the previous model gave some promising results, we wanted to build an AI model completely based on the poems of just The Thousand and One Nights from scratch. Since GPT-J had already been trained on a lot of unrelated datasets, we used Tensorflow in this case to create our own model. First of all, we wrote a python script to pre-process the poems for training and stored the output in clean_poem.txt.  A snippet of the code can be found below:

We then passed the clean_poem.txt file to the model for training and initial testing with a seed text. A snippet of the code used for training can be found below;

After the initial testing , we then created a file to test the model when given any input. A snippet of the code can be found below;

The model works by predicting the next word in the poem by assigning weights to each word in the poem during the training phase and since this model only knows about The Thousand and One Nights poem , it gave promising results than the previous algorithms. It is definitely the slam dunk winner amongst the others and can be trained further to produce even better results!

The poems that we were able to generate using this AI model with variable output length are:

Input: “Have you not had enough”

Output:  
***“Have you not had enough  
 my heart longs for a table  
spread with light kunafa  
in a buttered honey bath  
all day two armies fight  
 till all the blood is shed  
but covered by the night  
they sleep in the same bed   
to see their traces is to ache and cry  
where they once were”***

Input: “For pleasure, find these four zither lute harp and flute” 

Output:  
***“For pleasure, find these four  
zither lute harp and flute  
and love’s oath not to stray boredom  
that eyes to read and daisy rose and gillyflowers grow  
if the house could know who came this way  
it would thrill at the news and kiss the ground  
as if to greet its guest as if to say well met and welcome  
to a gracious mind mind trays of sweets face  
what heat in eyes that want to speak to and  
welcome to speak where and daisy rose and gillyflowers grow  
if the house could know who came this”*** (poetic device - repetition)

Input: “Leave the house to mourn its builder.”

Output:  
***“Leave the house to mourn its builder.  
its builder and own my regrets to a where myrtle daisy rose and gillyflowers grow  
if the house could know who came this way  
it would thrill at the news and kiss the ground as if to greet its guest  
as if to say well met and welcome to a gracious mind  
trays of sweets pair surpass beg return return”***

Input: “Love” (1001 Nights specific output for generalized keyword)

Output:  
***“Love is my law my drug inside and out 
a note for loving eyes to read and read 
met and welcome to mend 
where myrtle daisy rose and gillyflowers grow 
if the house could know who came this way it would”***

#### Highlights of Algorithm #4
• Since we trained this model from scratch with input poems only from The Thousand and One Nights, the algorithm generated poems using only words from the poems we fed it. It had no external influence whatsoever and the element of the poems we fed into it, popped out.

• We even tried out generic words like “Love” this time as input (just like we did in algorithm 3a), and the output results were no longer generic but rather very specific to the poems from The Thousand and One Nights, making our model completely different from the online generators that are fed with only external data and provide generalized responses.

• This model also provides the user with the option to change the number of words they want to generate thereby increasing customisability.

## Summary and Conclusion
Providing machines with human creativity is difficult. It requires a lot of experiments, testings, and failures. This paper goes through the process of designing and testing all the algorithms before arriving at the final one. The first step was to understand the most fundamental concept behind creating a poem/story generator. We started by writing simple algorithms to create a generialized story generator and then using those understandings, created a poem generator. The major problem that we faced here was that unlike a story, it is difficult to segregate poems based on their sentence structure. The algorithm was also prone to excessive repetition of words. Taking our learnings from this trial, we pivoted our approach into completely randomizing the words generated, avoiding repetitions, and giving the user more power to customize the poems. This was implemented well, but the poems generated were still very rough and felt more like a bunch of words put together than a poem. This was the point where we decided that we had ample understanding of the fundamental concept and the next step was to integrate AI. We learned about the GPT-J model and learned how to implement it. We had to create our own dataset where we tagged all the emotions that we felt from each poem. The results that we got after feeding the poems into the model were much more cohesive and poem like, but there was one major problem - the model had already been trained by over 6 billion datapoints and our dataset didn’t hold any weight. This caused us to get very generalized responses. We somehow had to make the algorithm give more weight to our dataset to be able to find elements of The Thousand and One Nights in the generated poems. So instead of trying to generate new poems altogether, we tweaked the input to be entire poems and instead check the proficiency of the algorithms to extend the poems. This way, more weight was drawn from our datasets as the inputs weren’t generic keywords like “love” anymore and therefore the results that we received were coherent extensions of the poems that we fed as inputs. The extensions did have elements other than our dataset, but the major part of the poem was still constructed from the input we provided. The final step in our process of constructing an AI-based poem generator algorithm was to train and deploy an model completely from scratch just using the dataset we provide, keeping any external elements away. And this is exactly what we implemented in the end. We trained an AI model on Tensorflow and fed it with just our dataset of poems. This time we tried both generating and extending poems using the algorithm, and the results we received convinced us that our project was successful. The poems wer received were just constructed from The Thousand and One Nights, were cohesive, and were customizable (selecting output length). The model did a great job in combining the elements of different poems to generate new poems and even generated poems based on generic keywords like “love” (the responses in this case weren’t generalized at all.  It was a tough process of trial and error, testing and feedback, but in the end we finally were able to reach the ideal outcome we had hoped for. 

Revisiting our initial thesis, we have made an attempt to showcase the creativity prospects of AI. The progress that AI has made over the years is absolutely spellbinding. But at the same time, the speculation of AI reaching the level of human intelligence someday, still feels like a far-reaching prospect. They sure might be able to become much better than humans in storing information and training on the stored data, but creativity is something that cannot ever be programmed - it can only be mimicked to an extent. Even to program that bit, it takes quite a lot of creativity on the end of the programmer which sort of imparts a sense of creativity (biased cause it comes from a human) into the machine rather than it being intrinsic to the computer. This is the closest that we can get to showcasing creativity (a vital component of human intelligence) in machines. The final poems generated by the model is really good considering it coming from a machine, but it still has a mechanical feel to it, which is much different from reading a poem written by a human. That being said, our model is just one of the many that exist, and there may definitely be much more powerful and robust AI systems capable of producing better results. 

As for whether Galland would have used the poem/story generator if it was available during his time is an interesting question to ponder upon. From what we have found from his adaptations of Hanna Diyaab’s stories is the fact that he really puts a lot of detail into making the simple mechanical notes that he took to create very detailed stories. So maybe he wouldn’t have used the model so as to be able to put his touch of creativity into the stories. But on the other hand, he was fast running out of stories and such a model would have definitely seemed very alluring to him. Even though we have no way of knowing it now, to think about such a propose is intriguing.

## Github Repository Link

https://github.com/swostikpati/AI-Poem-Generator

## References

• https://github.com/kingoflolz/mesh-transformer-jax/  
• https://www.eleuther.ai/  
• https://www.tensorflow.org/  









