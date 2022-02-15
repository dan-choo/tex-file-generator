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
content =  r'''
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
  To solve this, we want to solve the linear system $T(\vec x) = A\vec x = \vec 0$.
  We have:
  \begin{align*}
    \begin{pmatrix}
      1 & 1 & 1 & \bigm| & 0 \\
      1 & 1 & 1 & \bigm| & 0 \\
      1 & 1 & 1 & \bigm| & 0 \\
    \end{pmatrix} \\
    \text{Subtract the first row from the second and third row.} \\
    \begin{pmatrix}
      1 & 1 & 1 & \bigm| & 0 \\
      0 & 0 & 0 & \bigm| & 0 \\
      0 & 0 & 0 & \bigm| & 0 \\
    \end{pmatrix} \\
    \text{Which gives us the solution set:} \\
    z &= s \\
    y &= t \\
    x &= -t-s \\
  \end{align*}
  We can write this solution set as a linear combination of vectors:
  \begin{equation*}
    s
    \begin{bmatrix}
      -1 \\ 1 \\ 0
    \end{bmatrix}
    +
    t
    \begin{bmatrix}
      -1 \\ 0 \\ 1
    \end{bmatrix}
  \end{equation*}
  Which means the vectors$ 
  \begin{bmatrix}
    -1 \\ 1 \\ 0
  \end{bmatrix}
  $
  and  $
  \begin{bmatrix}
    -1 \\ 0 \\ 1
  \end{bmatrix}
  $
  span the kernel of $A$.
\end{homeworkProblem}

\begin{homeworkProblem}[20]
  The image of the transformation is a plane in $R^3$. This is due
  to the fact that one of the column vectors is linearly dependent. We
  have that $
  2
  \begin{bmatrix}
    2 \\ 3 \\ 6
  \end{bmatrix}
  +
  -1
  \begin{bmatrix}
    1 \\ 4 \\ 5
  \end{bmatrix}
  =
  \begin{bmatrix}
    3 \\ 2 \\ 7
  \end{bmatrix}
  $.
\end{homeworkProblem}

\begin{homeworkProblem}[32]
  Consider a linear transformation with matrix $A$ s.t.
  $A =
  \begin{pmatrix}
    7 & 7 & 7 \\
    6 & 6 & 6 \\
    5 & 5 & 5 \\
  \end{pmatrix}
  $
  Observe that we have two vectors that are redundant, and so the image of
  our linear transformation is the line spanned by
  $
  \begin{bmatrix}
    7 \\ 6 \\ 5
  \end{bmatrix}
  $.
\end{homeworkProblem}

\newpage

\begin{homeworkProblem}[34]
  To find the linear transformation whose kernel is the line spanned by
  $
  \begin{bmatrix}
    -1 \\ 1 \\ 2
  \end{bmatrix}
  $, we can simply find the two planes, that when interesected, give us
  the line above. Observe we have the two planes:
  \begin{align*}
    x + y &= 0 \\
    2x + z &= 0 \\
  \end{align*}
  whose intersection is the our vector. Thus, we have the matrix transformation:
  $T(\begin{bmatrix}x \\ y \\ z\end{bmatrix}) = \begin{bmatrix} x + y \\ 2x + z  \end{bmatrix}$.
\end{homeworkProblem}

\newpage
\textbf{\large Section 3.2}
\begin{homeworkProblem}[26]
  We have the redundant vector $
  \begin{bmatrix}
    6 \\ 5 \\ 4
  \end{bmatrix}
  = 
  \begin{bmatrix}
    3 \\ 2 \\ 1
  \end{bmatrix}
  +
  3
  \begin{bmatrix}
    1 \\ 1 \\ 1
  \end{bmatrix}
  $.    

  Thus, $\vec 0 = 
  \begin{bmatrix}
    3 \\ 2 \\ 1
  \end{bmatrix}
  +
  3
  \begin{bmatrix}
    1 \\ 1 \\ 1
  \end{bmatrix}
  -
  \begin{bmatrix}
    6 \\ 5 \\ 4
  \end{bmatrix}
  $. Which means that we have the nonzero vector $
  \begin{bmatrix}
    3 \\ 1 \\ -1
  \end{bmatrix}
  $ in the kernel of $A$.
\end{homeworkProblem}

\begin{homeworkProblem}[32]
  Observe that we have the redundant vector $
  \begin{bmatrix}
    3 \\ 4 \\ 5 \\ 0
  \end{bmatrix}
  = 
  \begin{bmatrix}
    0 \\ 0 \\ 0 \\ 0
  \end{bmatrix}
  +
  \begin{bmatrix}
    1 \\ 0 \\ 0 \\ 0
  \end{bmatrix}
  +
  \begin{bmatrix}
    2 \\ 0 \\ 0 \\ 0
  \end{bmatrix}
  +
  4
  \begin{bmatrix}
    0 \\ 1 \\ 0 \\ 0
  \end{bmatrix}
  +
  5
  \begin{bmatrix}
    0 \\ 0 \\ 1 \\ 0
  \end{bmatrix}
  $. And also the redundant vector, $
  \begin{bmatrix}
    2 \\ 0 \\ 0 \\ 0
  \end{bmatrix}
  $ as we have 
  $
  2
  \begin{bmatrix}
    1 \\ 0 \\ 0 \\ 0
  \end{bmatrix}
  =
  \begin{bmatrix}
    2 \\ 0 \\ 0 \\ 0
  \end{bmatrix}
  $. As well as the first column vector as we can simply multiply some other
  vector in our matrix by 0 to get it.
  Thus, the basis vectors for image of the matrix is $
  \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1 \\
    0 & 0 & 0 \\
  \end{pmatrix}
  $.
\end{homeworkProblem}

\newpage

\begin{homeworkProblem}[46]
  Observe that we can find the kernel by solving the linear system
  $
  \begin{pmatrix}
    1 & 2 & 0 & 3 & 5 \bigm| 0\\
    0 & 0 & 1 & 4 & 6 \bigm| 0\\
  \end{pmatrix}
  $. 
  Notice from this matrix we have the equations:
  \begin{align*}
    x_5 &= r \\
    x_4 &= t \\
    x_3 &= -4t - 6r \\
    x_2 &= s \\
    x_1 &= -2s - 3t - 5r \\
  \end{align*}
  Giving us the vector:
  $
  \begin{bmatrix}
    -2s - 3t - 5r \\ s \\ -4t - 6r \\ t \\ r
  \end{bmatrix}
  $
  which we can write as a linear combination:
  $
  s
  \begin{bmatrix}
    -2 \\ 1 \\ 0 \\ 0 \\ 0
  \end{bmatrix}
  +
  t
  \begin{bmatrix}
    -3 \\ 0 \\ -4 \\ 1 \\ 0
  \end{bmatrix}
  +
  r
  \begin{bmatrix}
    -5 \\ 0 \\ -6 \\ 0 \\ 1
  \end{bmatrix}
  $, which are, by definition, linearly independent. And so, we say that these
  vectors are the basis vectors of our kernel.
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
      \newpage
    \item[b.] $S$ is not a subspace of $V$.

      \textbf{Proof:} Consider a counterexample like so:

      Fix $x \in S$ s.t. $x =
      \begin{bmatrix}
        1 \\ 2
      \end{bmatrix}
      $, and let $k = -1$. Then
      $kx =
      \begin{bmatrix}
        -1 \\ -2
      \end{bmatrix}
      $. But $kx \not\in S$ as $S$ only contains the vectors where $y > 0$.
      Thus, $S$ is not closed under scalar multiplication and so $S$ is not
      a subspace of $V$. \qed

    \item[c.] $S$ is not a subspace of $V$.

      \textbf{Proof:} Fix $M_1, M_2 \in S$ s.t.
      $
      M_1 =
      \begin{pmatrix}
        3 & 2 \\
        3 & 2 \\
      \end{pmatrix}
      $
      and
      $
      M_2 =
      \begin{pmatrix}
        1 & 1 \\
        0 & 0 \\
      \end{pmatrix}
      $.
      Observe that both $M_1$ and $M_2$ are non-invertible matrices as
      their determinants are 0 (Theorem 2.4.9). We have that $M_1 + M_2 =
      \begin{pmatrix}
        4 & 3 \\
        3 & 2 \\
      \end{pmatrix}
      $. But the determinant here is -1, which means that $M_1 + M_2$ is
      invertible and so $S$ is not closed under addition. We conclude that $S$
      is not a subspace of $V$. \qed

    \item[d.] $S$ is a subspace of $V$.

      \textbf{Proof:} Similarly to $A$, we will show that $S$ holds under
      the three properties of subspaces.
      \begin{enumerate}
        \item[1.] Observe that the zero vector is in $S$ because by definition
          it is an upper-triangular matrix.
        \item[2.] Fix $M_1, M_2 \in S$ s.t.
          $
          M_1 =
          \begin{pmatrix}
            x_1 & x_2 \\
            0 & x_4 \\
          \end{pmatrix}
          $
          and 
          $
          M_2 =
          \begin{pmatrix}
            y_1 & y_2 \\
            0 & y_4 \\
          \end{pmatrix}
          $.
          We want to show that $M_1 + M_2 \in S$. Observe we have that:
          \begin{align*}
            M_1 + M_2 &= 
            \begin{pmatrix}
              x_1 & x_2 \\
              0 & x_4 \\
            \end{pmatrix}
            +
            \begin{pmatrix}
              y_1 & y_2 \\
              0 & y_4 \\
            \end{pmatrix} \\
                      &=
                      \begin{pmatrix}
                        x_1+y_1 & x_2+y_2 \\
                        0 & x_4+y_4 \\
                      \end{pmatrix}
          \end{align*}
          Notice that $M_1+M_2$ is still an upper triangular matrix as the the only
          entry where $i > j$ is 0. Thus, we say $S$ is closed under addition.
        \item[3.] Fix $M_1 \in S$ s.t.
          $
          M =
          \begin{pmatrix}
            x_1 & x_2 \\
            0 & x_4 \\
          \end{pmatrix}
          $.
          Fix some scalar $k$. We want to show that $kM_1 \in S$.
          We have:
          \begin{align*}
            kM_1 &= 
            \begin{pmatrix}
              kx_1 & kx_2 \\
              0 & kx_4 \\
            \end{pmatrix}
          \end{align*}
          Which is still an upper triangular matrix by definition, thus, we 
          say that $S$ is closed under scalar multiplication. \qed
      \end{enumerate}
    \item[e.] $S$ is a subspace of $V$.

      \textbf{Proof:} Like the previous proofs, we will show that $S$ holds under the
      properties of subspaces.
      \begin{enumerate}
        \item[1.] The zero vector of our vector space is simply the function
          $f(x) = 0$. Which is in $S$.
        \item[2.] Fix $f, g \in S$. We want to show that
          $f + g \in S$. Observe that $(f + g)(0) = f(0) + g(0)$. But by definition,
          $f$ and $g$ are functions where $f(0) = 0$ and $g(0) = 0$. Thus,
          $f(0) + g(0) = 0$ and so $(f + g)(0) = 0$ and we say that $(f + g) \in S$.
          We conclude that $S$ is closed under addition.
        \item[3.] Fix $f \in S$. We want to show $k \cdot f \in S$
          where $k$ is some scalar.
          Observe that $(k\cdot f)(0) = k \cdot f(0)$. But $f(0) = 0$ by definition,
          so $k \cdot f(0) = 0$ and $(k\cdot f)(0) = 0$. Thus, $k \cdot f \in S$.
          We conclude that $S$ is closed under scalar multiplication. \qed
      \end{enumerate}
      \newpage

    \item[f.] $S$ is a subspace of $V$.

      \textbf{Proof:} We will show that $S$ holds under the properties of subspaces.
      \begin{enumerate}
        \item[1.] The zero vector of our vector space is simply the function
          $f(x) = 0$, which is differentiable as the derivative of some constant is 0.
        \item[2.] Fix $f, g \in S$. We want to show that $f + g \in S$.
          Observe that $(f+g)(x) = f(x) + g(x)$. But since $f(x)$ and $g(x)$ are
          differentiable functions by definition, then $(f+g)(x)$ is differentiable as well,
          where $(f+g)'(x) = f'(x) + g'(x)$.
        \item[3.] Fix $f \in S$ and some scalar $k$.
          We want to show that $kf \in S$.
          Observe that $(kf)(x) = kf(x)$. But this is differentiable as we can
          simply factor out constants when differentiating. Thus,
          $(kf)'(x) = kf'(x)$. And so $kf \in S$.
          We conclude that $S$ is closed under scalar multiplication. \qed
      \end{enumerate}

  \end{enumerate}
\end{homeworkProblem}

\begin{homeworkProblem}
  \begin{enumerate}
    \item[a.] \textbf{Proof:} To prove this, we will show that $U \cap V$ holds
      under the three properties of subspaces.
      \begin{enumerate}
        \item[1.] Both $U$ and $V$ are subspaces, so $\vec 0 \in U$ and $\vec 0 \in V$. 
          Which means that $\vec 0 \in U \cap V$.
        \item[2.] Fix two vectors $x, y \in U \cap V$. We want to
          show that $x + y \in U \cap V$.

          To show this, first observe that since $x \in U \cap V$,
          then $x \in U$ and $x \in V$. Similarly then, $y \in U$ and $y \in V$.
          Note, however, by assumption that $U$ and $V$ are both subspaces of $W$.
          Which means that $x + y \in U$ and $x + y \in V$. But then this
          means that $x+y \in U \cap V$.
          Thus, $U \cap V$ is closed under addition.

        \item[3.] Fix some scalar $k$ and some vector $x \in U \cap V$. We want
          to show that $kx \in U \cap V$.

          To show this, observe that $x \in U$ and $x \in V$ by definition. Since 
          both $U$ and $V$ are subspaces, then $kx \in U$ and $kx \in V$.
          But this means that $kx \in U \cap V$,
          thus, $U \cap V$ is closed under scalar multiplication.
          \qed
      \end{enumerate}
    \item[b.] \textbf{Proof:} Suppose our vector space $W$ is $\mathbb R^2$.
      Let $U, V$ be the set of all vectors along the $x$ and $y$ axis respectively.
      Observe that both $U$ and $V$ are subspaces as they are lines that go
      through $\vec 0$ (page 124 in the textbook). Now suppose we have two vectors
      $
      \begin{bmatrix}
        2 \\ 0
      \end{bmatrix}
      $
      and
      $
      \begin{bmatrix}
        0 \\ 2
      \end{bmatrix}
      $.
      They are both in $U \cup V$, however,
      $
      \begin{bmatrix}
        2 \\ 0
      \end{bmatrix}
      +
      \begin{bmatrix}
        0 \\ 2
      \end{bmatrix}
      =
      \begin{bmatrix}
        2 \\ 2
      \end{bmatrix}
      $, is not in $U \cup V$. Thus, $U \cup V$ need not be a subspace of $W$. \qed

    \item[c.] \textbf{Proof:} Like before,
      we will show that $U + V$ holds under the three properties of subspaces.
      \begin{enumerate}
        \item[1.] Both $U$ and $V$ are subspaces,
          thus $\vec 0 \in U$ and $\vec 0 \in V$.
          We have that $\vec 0 + \vec 0 = \vec 0$, so $\vec 0 \in U + V$.
        \item[2.] Fix two vectors $x, y \in U + V$. We want to show
          $(x + y) \in U + V$.

          To show this, first observe that $x = x_1 + x_2$ where $x_1 \in U,
          x_2 \in V$ and $y = y_1 + y_2$ where $y_1 \in U, y_2 \in V$
          by definition.
          We now know then that $x + y = x_1 + x_2 + y_1 + y_2$.
          But notice that both $U$ and $V$ are subspaces
          so $x_1 + y_1 \in U$ and $x_2 + y_2 \in V$.
          Thus, $x + y \in U+V$.
        \item[3.] Fix some scalar $k$ and some vector $x \in U + V$. We
          want to show $kx \in U + V$. By definition, $x = x_1 + x_2$ where
          $x_1 \in U, x_2 \in V$. Thus, $kx = k(x_1 + x_2) = kx_1 + kx_2$.
          But because both $U$ and $V$ are subspaces, then $kx_1 \in U$
          and $kx_2 \in V$.
          Thus, $kx \in U + V$. \qed
      \end{enumerate}
      \newpage
    \item[d.] \textbf{Proof:} Suppose $X$ is some subspace of $W$ that contains
      both $U$ and $V$, we claim that $U + V \subseteq X$.

      To show this, fix some vector $x \in U + V$. By definition, 
      $x = x_1 + x_2$ where $x_1 \in U, x_2 \in V$. But notice that
      $X$ contains all vectors from both $U$ and $V$, thus $x_1, x_2 in X$.
      And since $X$ is also a subspace, we have that $x_1 + x_2 \in X$.
      Which implies $\vec x \in X$.
      We conclude that $U + V \subseteq X$. \qed
  \end{enumerate}
\end{homeworkProblem}

\begin{homeworkProblem}
  \begin{enumerate}
    \item[a.] \textbf{Proof:} Suppose that $T: V \rightarrow W$ is a linear
      transformation and injective. Let $(v_1, \cdots, v_k)$ be a list of
      linearly independent vectors in V. We want to show that 
      $(T(v_1), \cdots, T(v_k))$ is a list of linearly independent vectors as well.
      That is:
      \begin{equation*}
        c_1T(v_1) + \cdots + c_kT(v_k) = 0
      \end{equation*}
      if and only if $c_1 = \cdots = c_k = 0$.

      To do this, we will prove both ways. First suppose that:
      \begin{equation*}
        c_1T(v_1) + \cdots + c_kT(v_k) = 0
      \end{equation*}
      By linearity, we can rewrite as $T(c_1v_1 + \cdots + c_kv_k) = 0$.
      Now because $T$ is a linear transformation, it must be the case that
      $T(0) = 0$ (proven in Quiz 2 under Professor Smythe).
      And because $T$ is injective, then any other $v \in V$ where
      $T(v) = 0 \implies v = 0$. Thus, we have that
      $c_1v_1 + \cdots + c_kv_k = 0$, and by our initial assumption that
      $(v_1, \cdots v_k)$ is a list of independent vectors, then it must be the
      case that $c_1 = \cdots c_k = 0$.

      Now suppose that $c_1 = \cdots = c_k = 0$. It follows that
      $c_1T(v_1) + \cdots + c_kT(v_k) = 0$.

      Thus, $(T(v_1), \cdots, T(v_k))$ is a list of linearly independent
      vectors.

    \item[b.] \textbf{Proof:} We will provide a counterexample that
      shows that the assumption
      of injectivity is necessary. Consider the transformation
      $T(\begin{bmatrix} x \\ y \end{bmatrix}) = x + y$.
      Note that $T$ is a linear transformation as
      \begin{equation*}
        T(\begin{bmatrix} x + x_1 \\ y + y_1 \end{bmatrix}) =
        x + y + x_1 + y_1 =
        T(\begin{bmatrix} x \\ y \end{bmatrix}) +
        T(\begin{bmatrix} x_1 \\ y_1 \end{bmatrix})
      \end{equation*}
      and  
      \begin{equation*}
        T(k\begin{bmatrix} x \\ y \end{bmatrix}) = kx + ky =
        k(x+y) = kT(\begin{bmatrix} x \\ y \end{bmatrix})
      \end{equation*}
      where $k$ is some scalar. However, observe that $T$ is not injective as:
      $
      T(
      \begin{bmatrix}
        1 \\ 0
      \end{bmatrix}
      )
      = 1
      =
      T(
      \begin{bmatrix}
        0 \\ 1
      \end{bmatrix}
      )
      $.

      Now we have that $V = \mathbb R^2$ and that $W = \mathbb R$. Consider
      a list of two vectors
      $
      (
      \begin{bmatrix}
        1 \\ 0
      \end{bmatrix}
      ,
      \begin{bmatrix}
        0 \\ 1
      \end{bmatrix}
      )
      $. Notice that these vectors are independent as they are
      not scalar multiples of each other.
      Thus, we have a linearly independent list of vectors in $V$.
      
      Now observe when we apply our transformation $T$ to our list of vectors we get:
      $(1, 1)$- which is not a list of linearly independent list of vectors as
      $1 - 1 = 0$. \qed
      \newpage

    \item[c.] Suppose $T$ is a surjective and that we have a list of vectors
      $(v_1, \cdots, v_k)$ that spans V. We want to show that
      $(T(v_1), \cdots, T(v_k))$
      spans $W$.

      To show this, first note that since $T$ is surjective, it follows that
      for all $w \in W$, there exists some $v \in V$ s.t. $T(v) = w$. 
      Now observe that the span of $(T(v_1), \cdots, T(v_k))$
      consists of all the vectors that can be written as the linear combination:
      $c_1T(v_1) + \cdots + c_kT(v_k)$. By linearity, we can rewrite as
      $T(c_1v_1 + \cdots + c_kv_k)$. Thus, it suffices to show that as long as
      we can reach any vector in $V$ with the linear combination, $c_1v_1 + \cdots + c_kv_k$,
      then we can say that $(T(v_1), \cdots, T(v_k))$ spans $W$
      as $T$ is surjective.

      Notice, however, by our initial assumption
      that $(v_1, \cdots, v_k)$ spans V, which means that any vector in $V$
      can be rewritten as the linear combination: $c_1v_1 + \cdots + c_kv_k$.
      Thus, it follows that $T(c_1v_1 + \cdots + c_kv_k)$ spans $W$ because
      $T$ is surjective and we can get any vector in $V$ with
      $c_1v_1 + \cdots + c_kv_k$. \qed

    \item[d.] \textbf{Proof:} We will provide a counterexample that
      shows that the assumption
      of surjectivity is necessary. Consider the transformation
      $T(x) = \begin{bmatrix} x \\ 0 \end{bmatrix}$.
      Note that $T$ is a linear transformation as
      \begin{equation*}
        T(x + x_1) = \begin{bmatrix} x + x_1 \\ 0 \end{bmatrix} =
        \begin{bmatrix} x \\ 0 \end{bmatrix} 
        +
        \begin{bmatrix} x_1 \\ 0 \end{bmatrix} =
        T(x) + T(x_1)
      \end{equation*}
      and  
      \begin{equation*}
        T(kx) = \begin{bmatrix} kx \\ 0 \end{bmatrix} =
        k\begin{bmatrix} x \\ 0 \end{bmatrix} = kT(x)
      \end{equation*}
      where $k$ is some scalar. However, observe that $T$ is not surjective as
      if we take some $w \in W$ where $w = \begin{bmatrix} 1 \\ 1\end{bmatrix}$,
      then there does not exist any $v \in V$
      where $T(v) = \begin{bmatrix} 1 \\ 1\end{bmatrix}$
      as $T(v) = \begin{bmatrix} v \\ 0\end{bmatrix}$.

      With this, we have that $V = \mathbb R$ and $W = \mathbb R^2$.
      Observe that the list $(1)$ is a list of vectors
      that spans $V$, as we can simply multiply 1 with any scalar to get
      all of $\mathbb R$. However, if we apply our transformation $T$, 
      we get the list $(\begin{bmatrix} 1 \\ 0\end{bmatrix})$- which does
      not span all of $W$, as there does not exist any scalar $k$ where 
      $k\begin{bmatrix} 1 \\ 0\end{bmatrix} = \begin{bmatrix} 1 \\ 1\end{bmatrix}$.
      \qed
  \end{enumerate}
\end{homeworkProblem}
\begin{homeworkProblem}
  \begin{enumerate}
    \item[a.] \textbf{Proof:} To prove this, we will prove both ways, that
      is $S$ is a subspace of $V \implies b = \vec 0$ and that
      $b = \vec 0 \implies S$ is a subspace of $V$. 

      First suppose that $S$ is a subspace of $V$. However, if $S$ is a subspace,
      then we know that $\vec 0 \in S$. Thus, we have that 
      $T(\vec 0) = b$. But since $T$ is a linear transformation, then it must
      be the case that $T(\vec 0) = 0$ (Quiz 2 under Professor Smythe). Thus,
      $b = \vec 0$.

      Now suppose that $b = \vec 0$. We then have that
      $S = \{x \in V : T(x) = \vec 0\}$. But notice that this is exactly
      the definition of the kernel of a linear transformation. That is
      all $x \in V$ s.t. $T(x) = \vec 0$. From Theorem 3.2.2 in the book,
      we know that the kernel of a linear transformation is a subspace. Thus,
      because $T$ is a linear transformation, and $S$ is the kernel of $T$,
      then $S$ is also a subspace of $V$. \qed

      \newpage

    \item[b.] \textbf{Proof:} Fix $x_0 \in S$. We want to show that
      $S = x_0 + \text{ker}(T)$ where $T$ is some linear transformation from
      $V \rightarrow W$.

      To show this, first fix some element $s \in S$. We want to show that
      $s \in x_0 + \text{ker}(T)$. That is, $s = x_0 + u$ where $u \in \text{ker}(T)$.

      Observe that $s = x_0 + s - x_0$. We claim that $s - x_0 \in \text{ker}(T)$.
      If we apply our transformation $T$, we get $T(s - x_0) = T(s) - T(x_0) = b - b = \vec 0$.
      Thus, $s - x_0 \in \text{ker}(T)$. Which allows us to conclude that
      $s \in x_0 + \text{ker}(T)$.

      Now fix some element $t \in x_0 + \text{ker}(T)$. By definition,
      we know that $t = x_0 + u$ where $u \in \text{ker}(T)$.
      If we apply our transformation $T$, we get $T(t) = T(x_0 + u)$, and by
      linearity $T(t) = T(x_0 + u) = T(x_0) + T(u)$. But since $u \in \text{ker}(T)$,
      then $T(u) = \vec 0$. So, $T(t) = T(x_0 + u) = T(x_0) + T(u) = T(x_0) = b$,
      as $x_0 \in S$.
      Thus, $t \in S$. \qed

    \item[ci.] To solve the linear system $A\vec x = b$, it suffices to solve
      the matrix:
      \begin{equation*}
        \begin{pmatrix}
          1 & 2 & 0 & \bigm| & -2\\
          2 & 0 & 1 & \bigm| & 5\\
          3 & 2 & 1 & \bigm| & 3\\
        \end{pmatrix} \\
      \end{equation*}
      Subtract 2 times the first row from the second row
      and 3 times the first row from the third row.
      \begin{equation*}
        \begin{pmatrix}
          1 & 2 & 0 & \bigm| & -2\\
          0 & -4 & 1 & \bigm| & 9\\
          0 & -4 & 1 & \bigm| & 9\\
        \end{pmatrix}
      \end{equation*}
      Subtract the second row from the third row.
      \begin{equation*}
        \begin{pmatrix}
          1 & 2 & 0 & \bigm| & -2\\
          0 & -4 & 1 & \bigm| & 9\\
          0 & 0 & 0 & \bigm| & 0\\
        \end{pmatrix}
      \end{equation*}
      Now we have the solutions:
      \begin{align*}
        z &= t \\
        y &= -\frac{9}{4} + \frac{t}{4} \\
        x &= \frac{5}{2} - \frac{t}{2} \\
      \end{align*}
      Giving us a solution
      $\vec x_0 = \begin{bmatrix}\frac{5}{2} \\ -\frac{9}{4} \\ 0\end{bmatrix}$.

      \newpage

    \item[cii.] First, using our work from above, observe that the solutions
      to our linear system $A\vec x = \vec b$ can be written as:

      \begin{equation*}
        \begin{bmatrix}
          \frac{5}{2} \\ -\frac{9}{4} \\ 0
        \end{bmatrix}
        +
        t
        \begin{bmatrix}
          -\frac{1}{2} \\ \frac{1}{4} \\ 1
        \end{bmatrix}
      \end{equation*}

      Now, to find the $\text{ker}(A)$, we can use our work from above,
      giving us the matrix:
      \begin{equation*}
        \begin{pmatrix}
          1 & 2 & 0 & \bigm| & 0\\
          0 & -4 & 1 & \bigm| & 0\\
          0 & 0 & 0 & \bigm| & 0\\
        \end{pmatrix}
      \end{equation*}
      Which means we have the solutions to the $\text{ker}(A)$ as:
      \begin{align*}
        z &= t \\
        y &= \frac{t}{4} \\
        x &= - \frac{t}{2} \\
      \end{align*}
      Allowing us to write our solutions in the form:
      \begin{equation*}
        t
        \begin{bmatrix}
          -\frac{1}{2} \\ \frac{1}{4} \\ 1
        \end{bmatrix}
      \end{equation*}
      But since $\vec x_0 = 
      \begin{bmatrix}
        \frac{5}{2} \\ -\frac{9}{4} \\ 0
      \end{bmatrix}
      $, then
      \begin{equation*}
        \vec x_0 + \text{ker}(A) =
        \begin{bmatrix}
          \frac{5}{2} \\ -\frac{9}{4} \\ 0
        \end{bmatrix}
        +
        t
        \begin{bmatrix}
          -\frac{1}{2} \\ \frac{1}{4} \\ 1
        \end{bmatrix}
      \end{equation*}
      which is exactly the solutions to our linear system.

      We have that the geometric objects of $S$ and $\text{ker}(A)$
      are lines. And because they have the same direction vector,
      they are parallel lines.
  \end{enumerate}
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
        f.write(content %{"ID": row[1], "NAME": row[0]})

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

