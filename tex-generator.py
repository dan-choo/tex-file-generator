import argparse
import os
import subprocess
import csv
from string import Template


texPath = r''

# CSV FILE HERE
file = "test2.csv"
fields = []
rows = []

if not os.path.exists('tex-files'):
    print("Creating tex-files directory...")
    os.makedirs('tex-files')
    print("DONE")

if not os.path.exists('pdf-files'):
    print("Creating pdf-files directory...")
    os.makedirs('pdf-files')
    print("DONE")

# TEX FILE HERE 
# Make sure that the tex file has no comments because we are using
# the % symbol to mark where we should replace it with the correct student name
# and ID. Probably not the best idea so maybe there's a better way?
texFile =  r'''
\documentclass{article}

\usepackage{fancyhdr}
\usepackage{extramarks}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amsfonts}
\usepackage{tikz}
\usepackage{tikz-3dplot}
\usepackage[plain]{algorithm}
\usepackage{algpseudocode}
\usepackage{tabularx}

\usetikzlibrary{automata,positioning}

\topmargin=-0.45in
\evensidemargin=0in
\oddsidemargin=0in
\textwidth=6.5in
\textheight=9.0in
\headsep=0.25in

\linespread{1.1}

\pagestyle{fancy}
\lhead{\hmwkAuthorName}
\chead{\hmwkClass\ (\hmwkClassInstructor\ \hmwkClassTime): \hmwkTitle}
\rhead{}
\lfoot{}
\cfoot{\thepage}

\renewcommand\headrulewidth{0.4pt}
\renewcommand\footrulewidth{0.4pt}

\setlength\parindent{0pt}

\newcommand{\enterProblemHeader}[1]{
  \nobreak\extramarks{}{Problem \arabic{#1} continued on next page\ldots}\nobreak{}
  \nobreak\extramarks{Problem \arabic{#1} (continued)}{Problem \arabic{#1} continued on next page\ldots}\nobreak{}
}

\newcommand{\exitProblemHeader}[1]{
  \nobreak\extramarks{Problem \arabic{#1} (continued)}{Problem \arabic{#1} continued on next page\ldots}\nobreak{}
  \stepcounter{#1}
  \nobreak\extramarks{Problem \arabic{#1}}{}\nobreak{}
}

\setcounter{secnumdepth}{0}
\newcounter{partCounter}
\newcounter{homeworkProblemCounter}
\setcounter{homeworkProblemCounter}{1}
\nobreak\extramarks{Problem \arabic{homeworkProblemCounter}}{}\nobreak{}

\newenvironment{homeworkProblem}[1][-1]{
  \ifnum#1>0
    \setcounter{homeworkProblemCounter}{#1}
  \fi
  \section{Problem \arabic{homeworkProblemCounter}}
  \setcounter{partCounter}{1}
  \enterProblemHeader{homeworkProblemCounter}
  }{
  \exitProblemHeader{homeworkProblemCounter}
}


\newcommand{\hmwkTitle}{Homework\ \#4}
\newcommand{\hmwkDueDate}{February 3, 2022}
\newcommand{\hmwkClass}{ %(ID)s  }
\newcommand{\hmwkClassTime}{Section 001}
\newcommand{\hmwkClassInstructor}{Professor Iian Smythe}
\newcommand{\hmwkAuthorName}{\textbf{ %(NAME)s }}

\title{
  \vspace{2in}
  \textmd{\textbf{\hmwkClass:\ \hmwkTitle}}\\
  \normalsize\vspace{0.1in}\small{Due\ on\ \hmwkDueDate\ at 11:59pm}\\
  \vspace{0.1in}\large{\textit{\hmwkClassInstructor\ \hmwkClassTime}}
  \vspace{3in}
}

\author{\hmwkAuthorName}
\date{}

\renewcommand{\part}[1]{\textbf{\large Part \Alph{partCounter}}\stepcounter{partCounter}\\}
\newcommand{\alg}[1]{\textsc{\bfseries \footnotesize #1}}

\newcommand{\deriv}[1]{\frac{\mathrm{d}}{\mathrm{d}x} (#1)}

\newcommand{\pderiv}[2]{\frac{\partial}{\partial #1} (#2)}

\newcommand{\dx}{\mathrm{d}x}

\newcommand{\solution}{\textbf{\large Solution}}

\newcommand{\E}{\mathrm{E}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\Bias}{\mathrm{Bias}}

\begin{document}

\maketitle

\pagebreak

\textbf{\LARGE Part A} \\

\textbf{\large Section 3.1}
\begin{homeworkProblem}[8]
\end{homeworkProblem}

\begin{homeworkProblem}[20]
\end{homeworkProblem}

\begin{homeworkProblem}[32]
\end{homeworkProblem}

\newpage

\begin{homeworkProblem}[34]
\end{homeworkProblem}

\newpage
\textbf{\large Section 3.2}
\begin{homeworkProblem}[26]
\end{homeworkProblem}

\begin{homeworkProblem}[32]
\end{homeworkProblem}

\newpage

\begin{homeworkProblem}[46]
\end{homeworkProblem}

\newpage

\textbf{\LARGE Part B}
\begin{homeworkProblem}[1]
  \begin{enumerate}
    \item[a.] $S$ is a subspace of $V$.

      \textbf{Proof:} We will show that $S$ fulfills the three properties of
      subspaces to prove this, that is, it contains the zero vector, is closed under addition,
      and is closed under scalar multiplication.
      \begin{enumerate}
        \item[1.] The zero vector is in $S$. By definition, the zero vector
          is perpendicular to all other vectors. If we take the dot product,
          we get $0 \cdot 1 + 0 \cdot 2 + 0 \cdot 3 = 0$.

        \item[2.] Fix two vectors $x, y, \in \mathbb S$ where $
          x =
          \begin{bmatrix}
            x_1 \\ x_2 \\ x_3
          \end{bmatrix},
          y = 
          \begin{bmatrix}
            y_1 \\ y_2 \\ y_3
          \end{bmatrix}
          $.
          We want to show that $(x + y) \in S$.

          Observe that $x + y =
          \begin{bmatrix}
            x_1+y_1 \\ x_2+y_2 \\ x_3+y_3
          \end{bmatrix}
          $.
          It suffices to show that the dot product of our vector above and
          $
          \begin{bmatrix}
            1 \\ 2 \\ 3
          \end{bmatrix}
          $
          is 0.
          The reason for this is that
          for two vectors to be perpendicular, their dot product must be 0.
          Thus, we have:
          \begin{align*}
            \begin{bmatrix}
              x_1+y_1 \\ x_2+y_2 \\ x_3+y_3
            \end{bmatrix}
            \cdot
            \begin{bmatrix}
              1 \\ 2 \\ 3
            \end{bmatrix}
            &= 1(x_1+y_1) + 2(x_2+y_2) + 3(x_3+y_3) \\
            &= 1(x_1) + 1(y_1) + 2(x_2) + 2(y_2) + 3(x_3)+3(y_3) \\
            &= 1(x_1) + 2(x_2) + 3(x_3) + 1(y_1) + 2(y_2) + 3(y_3) \\
          \end{align*}
          However, notice that because $x, y \in S$, then it
          must be the case that $1(x_1) + 2(x_2) + 3(x_3) = 0$ and that 
          $1(y_1) + 2(y_2) + 3(y_3) = 0$. Thus,
          \begin{equation*}
            1(x_1) + 2(x_2) + 3(x_3) + 1(y_1) + 2(y_2) + 3(y_3) = 0
          \end{equation*}
          Which allows us to conclude that $S$ is closed under addition.

        \item[3.] Fix some vector $x \in S$ where $
          x =
          \begin{bmatrix}
            x_1 \\ x_2 \\ x_3
          \end{bmatrix}
          $. We want to show that $kx \in S$ where $k$ is some scalar. 
          Observe that $
          kx = 
          \begin{bmatrix}
            kx_1 \\ kx_2 \\ kx_3
          \end{bmatrix}
          $. If we take the dot product, then we have:
          \begin{align*}
            \begin{bmatrix}
              kx_1 \\ kx_2 \\ kx_3
            \end{bmatrix}
            \begin{bmatrix}
              1 \\ 2 \\ 3
            \end{bmatrix}
             &= 1kx_1 + 2kx_2 + 3kx_3 \\
             &= k(1x_1 + 2x_2 + 3x_3)
          \end{align*}
          But notice that $1x_1 + 2x_2 + 3x_3 = 0$ by definition as $x \in S$.
          Thus, $k(1x_1 + 2x_2 + 3x_3) = 0$ and so $kx \in S$. \qed
      \end{enumerate}
  \end{enumerate}
\end{homeworkProblem}

\begin{homeworkProblem}
\end{homeworkProblem}

\begin{homeworkProblem}
\end{homeworkProblem}
\end{document}
'''

with open(file,'r') as csvFile:
    csvreader = csv.reader(csvFile)
    fields = next(csvreader)
      # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

for row in rows:
    fileName = row[0] + '.tex'
    with open('tex-files/' + fileName, 'w') as f:
        print("Creating file for " + row[0])
        f.write(texFile %{"ID": row[1], "NAME": row[0]})

    os.chdir("pdf-files/")
        
    cmd = ['pdflatex','-interaction', 'nonstopmode', '../tex-files/' + fileName]
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        os.unlink(row[0]+'.pdf')
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

    os.unlink(row[0]+'.aux')
    os.unlink(row[0]+'.log')
    os.chdir("../")

