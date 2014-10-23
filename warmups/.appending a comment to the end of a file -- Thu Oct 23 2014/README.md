Introducing: add_comment - a simple script written in the bash scripting language
=================================================================================
Adds a text remark to the end of a text-based file.


Usage
-----
```
add_comment <file> <msg>
```


Example usage at Shell Prompt / Terminal
----------------------------------------
```
add_comment notes "#todo Call that cool person I met at that party"
```


Description of Behavior
-----------------------
* Appends remark to end of text file.
* Leaves an extra newline between the new remark and the existing content.


Limitations
-----------
* The file must already exist, otherwise you'll get an error.


Bash Code
---------
Don't worry if you don't understand this Bash code.  Your goal is to write Python code that does follows the "Descriptiong of Behavior".
```
#!/bin/bash

# add (bash script): adds a text remark to a text-based file
#  example usage at shell prompt:
#   $ add_comment notes "#todo Call that cool person I met at that party"
#  description of behavior:
#   leaves an extra newline between the new remark and the existing content

file="$1"
msg="$2"
if [[ `tail -n 1 "$file"` ]];   then echo "" | cat >> "$file";   fi
echo -e "$msg" | cat >> "$file"
```


Austin Coding Academy Warmup challenge!
------------------------------------------------------------------------------
* Create a script that does the same thing in Python.
* Make it in a function `def add_comment(string_data, remark)` that adds the remark to the string_data and returns the string_data
* Remember to leaves an extra newline between the new remark and the existing content, but don't leave 2!
* _BONUS 1:_ Make a function `def add_comment_to_file(filename, remark)` that uses your first function `add_comment` to add the `remark` to the file named `filename`.
* _BONUS 2:_ Use `if __name__ == "__main__"` to let your python script be used from the command line just like my bash script.


