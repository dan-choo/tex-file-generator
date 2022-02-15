# Tex File Generator

## What does it do?
It basically takes a CSV file of a group of students and creates a a copy of
the .tex file and it's corresponding PDF file. 

It then creates two folders: `tex-files\` and `pdf-files\` in whatever
directory you're running this script where the .tex and PDF files will be stored.

**NOTE:** I've only tested this on Ubuntu so I don't know how it would work
on Windows. I think macOS should be fine too though?

## How to use it?
1. Change `file` to be the name of the CSV file you're opening (make sure it's in the same
directory)

**NOTE:** The program assumes that the first two columns are the student's name and
their ID.

2. Edit `texFile` to be the tex file you want to make copies of.
Then place `%(ID)s` and `%(NAME)s` wherever you want to replace it with the student's name
and ID.

**NOTE:** Latex also uses `%` to signify a comment. Unfortunately, since we're also using
`%` as our marker token, we need to make sure that there are no comments in the tex file,
otherwise our program won't run D:





