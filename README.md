# SE_assg

The interface will have two features - to update an entry in the database or to search for an already existing entry in the database.

SEARCH : On availing the search feature, a dropdown list will be provided showing the names of the entries already present. Whichever option the user selects the details i.e the name, amino-acid sequence, G+C% etc will be displayed.

UPDATE : The user will be provided with the option to browse through the local files to upload a file. If it is a .txt file, it will be checked if it is valid following the above mentioned conditions. In case , there are letters other than  ‘a’,’u’,’t’,’c’, a remark will be added. Otherwise, the nucleotide sequence will be converted to the corresponding amino-acid sequence. First of all, the input file contents need to be extracted and validated. After this, the first line starting with ’>’ represents the description of the nucleotide sequence that follows it. It may be multiple lines until a line starting with ’>’ is encountered again. Then the nucleotide sequence is extracted 3 at a time (codon) and its corresponding amino acid is generated from a map that stores this information i.e. map[codons]=amino_acid.  Along with this, the G+C% value is also computed and stored in a float variable. Then all the generated values are added as an entry to the database.
