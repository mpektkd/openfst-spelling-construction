## openfst-spelling-construction
NTUA Projects, NLP

  - **Step 1:** _Corpus Construction_
    - Download and basic preprocess the corpus 
  
  - **Step 2:** _Vocabulary Construction_
    - Dictionary <token, numberOfimpressions>
    - Filter tokens that appear less than 5 times
    - Produce file with two columns _(token, numberOfimpressions)_
    
  - **Step 3:** _Generate input/output symbols for FSTs_
    - Match each lowercase character English language in an ascending integer index
    - The first symbol with index 0 is ε (<eps>)
    - The result will be written to the file vocab/chars.syms 
    - Create the words.syms file that maps each word (token) from vocabulary you constructed in 
      Step 2 to a unique integer index. 
    - The result should written to vocab/words.syms.
  
  - **Step 4:** _Construction of edit distance converter_
    - Construct a single-state L-converter that implements the Levenshtein distance matching:
      1. each character in itself with weight 0 (no edit)
      2. each character in e with weight 1 (deletion)
      3. the e in each character with a weight of 1 (insertion)
      4. every character to every other character with weight 1
    - Use _fstcompile_ to compile L and save the result in fsts/L.binfst.
    - Use _fstdraw_ to draw L
  
  - **Step 5:** _Constructing a dictionary receiver_
    - Construct an acceptor V with an initial state that accepts every word in the dictionary
    - The weights of all edges are 0
    - Call _fstrmepsilon_, _fstdetermine_ and _fstminimize_ to optimize the model
    - Use _chars.syms_ for input symbols and _words.syms_ for output symbols
  
  - **Step 6:** _Spelling composition_
    - Combine the Levenshtein transducer L with the receiver V producing the min
      edit distance spell checker S. 
    - Analyze the behavior of this converter: 
      1. in the event that the edits are equal,
      2. for different weights of the edits (eg cost(insertion)=cost(deletion)=1,      
         cost(substitution)=1.5)
    - Test the model with the inputs "cit", "cwt"(we call fstarcsort on the transducer's 
      outputs and/or its inputs acceptor )
  - **Step 7:** _Evaluation_
    - Evaluate the model over the spell_test.txt
