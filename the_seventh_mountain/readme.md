# About Panditah of the Seventh Mountain
On hard mode, the most time consuming puzzle in Jewels of the Oracle as far as I know at least. The python scripts here are majour duplicates of each other just quickly intended to solve it in different ways.

`7th_jewels_of_the_oracle.py` solves it the most basic way. It solves it once. Comment back in the standard for loop and uncomment the `randomly` stuff to solve it like a computer would. The randomly part is used to sort of replicate a human choosing a number that works which we don't necessarily do in order 0-9.
However, the order in which it solves the puzzle is important. Choosing to solve certain parts in a certain order increase the changes of stumbling upon a correct solution. Which is what

`7th_jewels_of_the_oracle_stat_hardest.py` does. It solves it in the worst possible order. These are compared in the video.

`7th_jewels_of_the_oracle_stat.py` solves it using the good method, but sends results to a hardcoded .csv file.

# Disclaimer
I provide this code only as companion to my Let's Play videos. It was used only to get the answers I wanted as quickly as possible. The duplication of code between three files is already a terrible thing, and the format / algorithm could probably be improved. _Do Not Use Any Of My Work As An Example Of Good Python Code_. I am not a python developer and I assure you it is very much terrible code.
