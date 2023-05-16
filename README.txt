This repository is meant to be used for the analysis of data of Sp(4) gauge theory with fermions
in the 2-antisymmetric representation obtained running GRID.


There are four main directories: 

1) The first one is called 'analysis_code', which contains
all the codes that has been used to analyse data presented in the paper to be
uploaded on the arXiv about this subject. Most of these codes are meant to give exactly
the output file that can be then plotted.

2) The second directory is called 'plots' and contains the codes that plot the data exactly as
they are shown in the paper. This directory contains also old codes used to develop the current
ones.

3) The third directory, called 'data' contains the data that have been used in the plots shown in the
paper.

4) The fourth directory is called 'raw_data'. Here you are expected to put the raw data, which will be
analysed through the codes in 'analysis_code' and whose deriving data will be put in 'data' and will
be plotted with the codes in 'plots' and saved in 'plots/figures'.

So far, the procedure is automatic at three levels
 - Submission: each directory in 'analysis_code' has a code that will generate the raw data and put them
   in the 'raw_data' directory.
 - Analysis: the same directory will contain a code that if ran will generate from the raw data contained
   in 'raw_data' the analysed data, and will put them in 'data'.
 - Plot: the directory 'plots' contains subdirectories. For each of them there will be one code that if
   ran, it will use the data in 'data' and generate the plots exactly as they are shown in the paper.
