# Tex File Generator

## What does it do?
It basically takes a CSV file of a group of students and creates a a copy of
the .tex file and it's corresponding PDF file with the students name and id.

It then creates two folders: `tex-files\` and `pdf-files\` in whatever
directory you're running this script and stores the `.tex` and `.PDF` files
in their corresponding folder. 

**NOTE:** I've only tested this on Ubuntu so I don't know how it would work
on Windows. I think macOS should be fine too though?

## How to use it?
1. Change `file` to be the name of the CSV file you're opening (make sure it's in the same
directory)

**NOTE:** The program assumes that the first two columns are the student's name and
their ID. So make sure whatever CSV file you're using follows that format
(you could probably just change that too though). I tested this script with the CSV
file from Gradescope so you could just use that.

2. Edit `texFile` to be the tex file you want to make copies of.
Then place `%(ID)s` and `%(NAME)s` wherever you want to replace it with the student's name
and ID.

**NOTE:** Latex also uses `%` to signify a comment. Unfortunately, since we're also using
`%` as our marker token to signify where we should replace the string,
we need to make sure that there are no comments in the tex file-
otherwise our program won't replace the strings correctly.

After that the program should work!



