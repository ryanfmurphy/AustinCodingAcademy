Warmup Tue Nov 11 - Answering Questions
---------------------------------------

Create a function `answer(question)` which takes a string which is a question, such as "Are you having a good day?" or "Are you going to the store?", and returns an answer, such as "Yes, I am having a good day." or "No, I am not going to the store.".

You can make these assumptions:

* The question will start with "are you..." and end with a question mark "?".

You can follow this process:

* `import random` and choose a random Yes/No answer by calling `random.choice(['Yes','No'])`
* Split the question into words using `.split()`
* Replace the first 2 words of the question ("Are you") with either "Yes I am" or "No, I am not"
* Replace the question mark at the end of the last word with a period

