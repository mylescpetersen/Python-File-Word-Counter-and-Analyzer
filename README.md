# Python-File-Word-Counter-And-More

Is run by ./word_length_counter.py --infile <filename> [--sort] [--print-words]
or        python --infile <filename> [--sort] [--print-words]

Example Output (no arguments):

Count[01]=01;
Count[02]=05;
Count[04]=03;
Count[07]=06;
Count[08]=01;

Example Output (--sort):

Count[07]=06;
Count[02]=05;
Count[04]=03;
Count[01]=01;
Count[08]=01;
Median word length: 3.0

Example Output (--print-words):

Count[01]=01; (words: "I")
Count[02]=05; (words: "Oh", "ah", "eh", "ha" and "oh")
Count[04]=03; (words: "Abcd", "abcd" and "dcba")
Count[07]=06; (words: "sjufksi", "Hfyakua", "Mjswqyl", "bshiakw" and "zosjwlf")
Count[08]=01; (words: "suenclyq")

Example Output (--sort --print-words):

Count[07]=06; (words: "sjufksi", "Hfyakua", "Mjswqyl", "bshiakw" and "zosjwlf")
Count[02]=05; (words: "Oh", "ah", "eh", "ha" and "oh")
Count[04]=03; (words: "Abcd", "abcd" and "dcba")
Count[01]=01; (words: "I")
Count[08]=01; (words: "suenclyq")
 

