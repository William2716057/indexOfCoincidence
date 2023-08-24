# indexOfCoincidence

Index of Coincidence Calculator
This Python script calculates the Index of Coincidence (IoC) for a given text. The IoC is a statistical measure used to assess the likelihood that a text is a substituted cipher or random text. It can also be used to identify the likely language of the encoded text.

How it Works
The script takes input text and performs the following operations:
Removes spaces and capitalizes all letters to ensure consistency.
Counts the frequency of each letter in the text.
Calculates the IoC using the formula: IoC = (N(N-1)) / (n(n-1)), where N is the total number of characters in the text, and n is the total number of unique letters.
Usage
Clone this repository to your local machine.

Run the script using Python:

bash
Copy code
python index_of_coincidence.py
Paste the text you want to analyze when prompted.

The script will calculate and display the Index of Coincidence for the input text.

Interpretation
The calculated IoC value typically ranges from about 0.0385 (for highly randomized text) to 0.067 (for typical English text). However, this range can vary depending on the language and text source.

A higher IoC value suggests that the text exhibits characteristics of typical language letter frequency, indicating it's likely in a natural language.

A lower IoC value suggests that the text may be more random or encrypted, deviating from typical language characteristics.
