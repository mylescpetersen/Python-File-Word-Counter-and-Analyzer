# Python-File-Word-Counter-And-Analyzer

Is run by "python word_length_counter.py --infile 'filename' [--sort] [--print-words]"
or        "./word_length_counter.py --infile 'filename' [--sort] [--print-words]"

Example Output (no arguments):

Count[01]=01;<br>
Count[02]=05;<br>
Count[04]=03;<br>
Count[07]=06;<br>
Count[08]=01;<br><br>

Example Output (--sort):<br><br>

Count[07]=06;<br>
Count[02]=05;<br>
Count[04]=03;<br>
Count[01]=01;<br>
Count[08]=01;<br>
Median word length: 3.0<br><br>

Example Output (--print-words):<br><br>

Count[01]=01; (words: "I")<br>
Count[02]=05; (words: "Oh", "ah", "eh", "ha" and "oh")<br>
Count[04]=03; (words: "Abcd", "abcd" and "dcba")<br>
Count[07]=06; (words: "sjufksi", "Hfyakua", "Mjswqyl", "bshiakw" and "zosjwlf")<br>
Count[08]=01; (words: "suenclyq")<br><br>

Example Output (--sort --print-words):<br><br>

Count[07]=06; (words: "sjufksi", "Hfyakua", "Mjswqyl", "bshiakw" and "zosjwlf")<br>
Count[02]=05; (words: "Oh", "ah", "eh", "ha" and "oh")<br>
Count[04]=03; (words: "Abcd", "abcd" and "dcba")<br>
Count[01]=01; (words: "I")<br>
Count[08]=01; (words: "suenclyq")<br>
 <br>

