This repository is meant to be used for the analysis of data of Sp(4) gauge theory with fermions
in the paper 'Symplectic lattice gauge theories on Grid: approaching the conformal window' 
(arXiv:2306.11649).

---------------------------------------------------------------------------------------------------------

GENERAL DESCRIPTION AND USAGE:

This code is working in two ways: it either makes the analysis from raw output data given by GRID, and then
plots them, or it simply plots the pre-analysed data. The code automatically detects if precomputed data
will be put in the suitable directory, and will plot them. Otherwise, if those directories will be empty, 
it will look for raw_data in the proper directory, and will analyse them from scratch and them plot the 
results of the analysis. You can also fill part of the subdirectories within 'precomputed_data' and plot
part of the plots as in the paper, and re-analyse from scratch the rest of them.

---------------------------------------------------------------------------------------------------------

FIRST THINGS TO DO, IF YOU WANT TO MAKE SURE TO AVOID COMPATIBILITY PROBLEMS: 

Download this code and download the data release files in ###########

Then, create the conda environment in terminal with conda installed:

$ conda env create -f environment.yml

Once the environment is created, you can active it:

$ conda activate analysis-env

---------------------------------------------------------------------------------------------------------

DESCRIPTION OF DIRECTORIES:

There are seven main directories: 

1) The first one is called 'submit_code' and it is the code used for submission of jobs on GRID.
This can be used as a useful tool to submit some of the jobs that would take quite a long time to
submit manually. These were thought be used on Tursa Dirac. Some old codes in 'submit_code/old_codes/'
were though to be used on SuperComputing Wales SUNBIRD.

2) The second one is called 'analysis_code/', which contains all the codes that has been used
to analyse data presented in the paper (arXiv:2306.11649). 

3) The third directory is called 'plots/' and contains the codes (in particular, in the subdirectory 
'plots/codes/') in the that plot the data as they are shown in the paper. This directory contains also
old codes used to develop the current ones. Also 'plots/figures/' will contain the output figures, 
obtained from running the code.

4) The fourth directory, called 'data/' contains the data that will be the outcome if the user will run the 
code, having the purpose to redo the analysis+plotting procedure from raw_data for all or part of the data.

5) The fifth directory is called 'raw_data/'. Here the user is expected to put the raw data, in case they want
to make the analysis and plotting of data. The raw data will be analysed through the codes in 'analysis_
code/' and the deriving data will be put in 'data/'. These will be plotted through the codes in 'plots/' and 
the resulting figures will be saved in 'plots/figures/'. The raw data used in the analysis of (arXiv:2306.11649)
can be downloaded from ######.

6) The sixth directory is called 'automated_results/'. This contains all the codes that are meant 
to give the final plots to the user, in an automated way. For all the figures shown in the paper there are 
codes producing them.

7) The seventh directory is called 'precomputed_data'. These data can be downloaded from ######. These
are the datapoints that have been obtained from the analysis done in the paper, and if the user will run one
or more than one of the codes in 'automated_code' with these directories not being empty, this will result in
plotting these datapoints, rather than redoing the whole analysis from scratch. If a directory in 'precomputed_
data' has the necessary files to be plotted, the user doesn't need to have every file to be analysed in 'raw_data'.
Conversely, if the user wants to analyse from scratch data, he will have to make sure that the corresponding 
'raw_data' directory will be filled and the correspondent 'precomputed_data' directory will be empty. 

--------------------------------------------------------------------------------------------------------

LEVELS OF AUTOMATION:

The procedure is automatic at three levels:

 - Submission: each directory in 'analysis_code/' has a code that will generate the raw data and put them
   in the 'raw_data/' directory.
   
 - Analysis: the same directory will contain a code that if ran will generate from the raw data contained
   in 'raw_data/' the analysed data, and will put them in 'data/'.
   
 - Plot: the directory 'plots/codes/' contains codes that if ran, they will use the data in 'data' (in case
   that the correspondent subdirectory of 'precomputed_data' will be empty) and generate the plots exactly 
   as they are shown in the paper. The results will be shown in 'plots/figures/'.
   
Anyways, the analysis+plot can made in one go. Below are the istructions for making everything in one go
and separating the two steps.

-------------------------------------------------------------------------------------------------------

ISTRUCTIONS FOR SUBMISSION OF JOBS:

To reproduce the figures as in the publication, follow these steps:

1) 'git clone' this code in the proper directory in Grid. (e.g. 'Grid/build/tests/sp2n').

2) Submit jobs.
   Some submissions can be achieved in an automated way, through the scripts in 'submit_code'.
   In particular:
   - The parameter scan for each Sp(4) theory with Nf 2AS fermions can be submitted using 'submit_code/
     parameter_scan/parameter_scan_submit_tursa.sh'.
   - The spacing distribution of eigenvalues can be submitted through 'submit_code/eigenvalues/
     submit_eigenvalues_matrices.sh'.
   - The submission of Wilson Flow and Topological charges can be done through 'submit_code/
     WF_top_charge/submit_topcharges.sh'.

All the outputs will be saved in 'raw_data/'. These codes are expecting to have any possible submit
script in the same directory. E.g. running 'submit_code/parameter_scan/parameter_scan_submit.sh',
you may want to put submit scripts in 'submit_code/parameter_scan/.
The examples of the scripts used were left in each directory.

-------------------------------------------------------------------------------------------------------

ISTRUCTIONS FOR ANALYSIS AND PLOTTING:

The analysis and plotting can be splitted in two steps or done in one go automatically. Otherwise one
can also plot precomputed data, filling the proper directories with those data.


1.a) AUTOMATED WAY, ANALYSIS+PLOT:

There will be a directory called 'automated_results/':
- 'initial_results.sh' will process the data for the preliminary results in figs. 2-6.
   This will need to have either 'raw_data/initial_tests' filled or 'precomputed_data/
   initial_tests' filled to run. In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).
   
   
- 'forces.sh' will process the data shown in fig. 7.
   This will need to have either 'raw_data/force_contribution' filled or 'precomputed_data/
   force_contribution' filled to run.In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).
   
   
- 'rhmc_compatibilities.sh' will process the data shown in fig. 8.
   This will need to have either 'raw_data/rhmc_compatibilities' filled or 'precomputed_data/
   rhmc_compatibilities' filled to run. In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).

- 'polyakov_loops.sh' will process the data shown in fig. 9.
   This will need to have either 'raw_data/polyakov_loops' filled or 'precomputed_data/
   polyakov_loops' filled to run. In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).


- 'eigenvalues.sh' will process both plots for the unfolded distribution of Eigenvalues, 
   for both Fundamental and 2AS representation, shown in fig. 10.
   This will need to have either 'raw_data/eigenvalues' filled or 'precomputed_data/
   eigenvalues' filled to run. In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).
   
   
- 'parameter_scan.sh' will process the data for the parameter scan. Usage of it's reported 
   at the beginning of the code. This will allow to process the data for figs. 11 and 14.
   This will need to have either 'raw_data/Nk_data' filled or 'precomputed_data/
   Nk_data' filled to run, with 0 <= k <= 8. In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).
   
   USAGE: 'bash parameter_scan.sh <beta_values> <thermalisation_number> <number_of_2AS_flavours>'
   where <beta_values> e.g. could be '6.4 6.7 6.5 7.0 7.1'.
   
  
- 'hot_parameter_scan.sh' will allow to process the data for fig. 12. 
   This will need to have either 'raw_data/Nf4_hot' and 'raw_data/Nf4_data filled or 
   'precomputed_data/Nf4_hot' and 'precomputed_data/Nf4_data' filled to run.
   In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).
   
   
- 'susceptibility.sh' will allow to process the data for fig. 13.
   This will need to have either 'raw_data/susceptibility' filled or 'precomputed_data/
   susceptibility' filled to run. In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).


- 'WF.sh' will process both plots from Wilson flow. This will allow to process the data shown
   in fig. 15. 
   This will need to have either 'raw_data/WF' filled or 'precomputed_data/
   WF' filled to run.  In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).
   
   
- 'topological_charge.sh' will process both plots for Topological charge. This will allow to
   process the data shown in fig. 16. 
   This will need to have either 'raw_data/TopCharge' filled or 'precomputed_data/
   TopCharge' filled to run. In case that the 'precomputed_data/' subdirectory will be
   filled, the analysis will be skipped and we will do data processing described in the
   point 1.b).
   


All the analysed data will be automatically saved in 'data/'. In case the 'precomputed_data/' subdirectory
will be found empty by the code. Otherwise 'data/' will be left untouched.

All the plots will be automatically saved in 'plots/figures/' and will be exactly with the same style 
as the ones shown in the paper.  





1.b) PLOTTING PRECOMPUTED DATA:
If you will fill the suitable subdirectories of 'precomputed_data' and run the automated codes, these 
codes will take those data, avoiding any further analysis, and plot them. 


1.c) SPLITTING ANALYSIS AND PLOTTING DATA:

1.c.1) Analyse data. 
   This can be done using the code in 'analysis_code/'.

All the analysed data will be automatically saved in 'data/'.

1.c.2) Plot data. 
   This can be done using the codes in 'plots/codes/'.    

All the plots will be automatically saved in 'plots/figures/' and will be exactly with the same style 
as the ones shown in the paper.  

-----------------------------------------------------------------------------------------------------

Here we report a list of picture number and code used to plot them in 'plots/codes/':
   'figure1.nb' --> Fig. 1
   'plot_data_creutz.py' --> Fig. 2
   'plot_data_plaq_step.py' --> Fig. 3
   'plot_data_dH_steps.py' --> Fig. 4
   'plot_data_pacc_steps.py' --> Fig. 5
   'plot_data_reversibility.py' --> Fig. 6
   'plot_forces.py' --> Fig. 7
   'plot_data_comp_rhmc.py' and 'plot_data_comp_rhmc_2p2.py' --> Fig. 8
   'plot_poly.py' --> Fig. 9
   'Dw_distributions.py' --> Fig. 10
   'plot_data_nfN_scan.py' with 0 <= N <= 8 --> Figs. 11 and 14
   'plot_hot.py' --> Fig. 12
   'plot_susc.py' --> Fig. 13
   'plot_topcharge_b68.py' and 'plot_topcharge_b69.py' --> Fig. 15
   'plot_WF_E.py' and 'plot_WF_W.py' --> Fig. 16 

-----------------------------------------------------------------------------------------------------

All the subdirectories have very intuitive names, and their names coincide with the names of the directories
uploaded in ##########, in order to avoid any confusion. You just need to copy and paste the content of the 
right directory either in the subdirectories of 'raw_data/' (if you are starting from raw data) or 'precomputed
_data/' (if you just want to plot data).
