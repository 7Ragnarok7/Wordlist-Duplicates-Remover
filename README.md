# Wordlist-Duplicates-Remover

 ***THis tool can be very useful to cleanup a wordlist containing duplicate entries.***
 ***Might be handy for CTF challenges where wordlists are intentionally made large and contain lots of duplicate entries.***
 
 ## Usage:-
 
 ```sh
 $ ./dup-rem.py input-file output-file {Optional arguments: asc, dsc}
 ```

## Arguments:-
**asc** : Sorts the output in an ascending order.

**dsc** : Sorts the output in a descending order.

## Examples:-

```sh
 $ ./dup-rem.py file1.txt file2.txt asc
 $ ./dup-rem.py file1.txt file2.txt
 $ ./dup-rem.py file1.txt file2.txt dsc
 ```
 
 ## Features:-
 
 - The output will be randomized/shuffled everytime (may overall time to perform a dictionary-attack if the wordlist is sorted)
 - The output can be manually sorted in ascending or descending order
 - The difference between number of lines in the old and new wordlist will be printed
