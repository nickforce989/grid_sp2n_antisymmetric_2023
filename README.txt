This repository is meant to be used for the analysis of data of Sp(4) gauge theory with fermions
in the 2-antisymmetric representation obtained running GRID.

-------------------------------------------------------------------------------------------------------------------------------
GENERAL DESCRIPTION:

There are four main directories: 

1) The first one is called 'analysis_code/', which contains all the codes that has been used
to analyse data presented in the paper to be uploaded on the arXiv about this subject. Most 
of these codes are meant to give exactly the output file that can be then plotted.

2) The second directory is called 'plots/' and contains the codes that plot the data exactly as
they are shown in the paper. This directory contains also old codes used to develop the current
ones.

3) The third directory, called 'data/' contains the data that have been used in the plots shown in the
paper.

4) The fourth directory is called 'raw_data/'. Here you are expected to put the raw data, which will be
analysed through the codes in 'analysis_code' and whose deriving data will be put in 'data' and will
be plotted with the codes in 'plots/' and saved in 'plots/figures/'.


The procedure is automatic at three levels:

 - Submission: each directory in 'analysis_code/' has a code that will generate the raw data and put them
   in the 'raw_data/' directory.
   
 - Analysis: the same directory will contain a code that if ran will generate from the raw data contained
   in 'raw_data/' the analysed data, and will put them in 'data/'.
   
 - Plot: the directory 'plots/codes/' contains codes that if ran, they will use the data in 'data' and generate
   the plots exactly as they are shown in the paper. The results will be shown in 'plots/figures/'.

-------------------------------------------------------------------------------------------------------------------------------
ISTRUCTIONS:

To reproduce the figures as in the publication, follow these steps:

1) 'git clone' this code in the proper directory in Grid. (e.g. 'Grid/build/tests/sp2n').

2) Submit jobs.
   Every non-trivial submission can be achieved in an automated way, through the scripts in 'analysis_code'.
   In particular:
   - The parameter scan for each Sp(4) theory with Nf 2AS fermions can be submitted using 'analysis_code/parameter_scan/
     parameter_scan_submit.sh'.
   - The spacing distribution of eigenvalues can be submitted through 'analysis_code/eigenvalues/
     submit_eigenvalues_matrices.sh'.
   - The submission of Wilson Flow and Topological charges can be done through 'analysis_code/
     top_charge/submit_topcharges.sh'.

All the outputs will be saved in 'raw_data/'. These codes are expecting to have any possible submitting script in the same
directory. E.g. running 'analysis_code/parameter_scan/parameter_scan_submit.sh', you may want to put submitting scripts in 
'analysis_code/parameter_scan/.

3) Analyse data. 
   This can be done in an automated way, using the code in 'analysis_code/'.
   In particular:
   - The parameter scan for each Sp(4) theory with Nf 2AS fermions can be analysed using 'analysis_code/parameter_scan/
     analyze_plaquette.py'. 
   - The spacing distribution of eigenvalues can be analysed through '2AS_analysis.sh' or 'fund_analysis' (depending whether
     one is working in the fundamental or 2AS representation. These code will be located in 'analysis_code/eigenvalues/'.
   - The analysis of Wilson Flow can be done through 'analysis_code/WF/WF_energydens.py'.
   - The analysis of topological charges will be done with '/grid_sp2n_antisymmetric_2023/analysis_code/WF/top_charges.py'.
   - Every other more trivial analysis can be done with the codes in '/grid_sp2n_antisymmetric_2023/analysis_code/Utils'.

All the analysed data will be automatically saved in 'data'.

4) Plot data. 
   This can be done in an automated way, using the code in 'plots/codes/'.  
   Here we report a list of picture number and code used to plot them:
   'plot_data_creutz' --> Fig. 2
   'plot_data_plaq_step.py' --> Fig. 3
   'plot_data_dH_steps.py' --> Fig. 4
   'plot_data_pacc_steps.py' --> Fig. 5
   'plot_data_reversibility.py' --> Fig. 6
   'plot_forces.py' --> Fig. 7
   'plot_data_comp_rhmc.py' and 'plot_data_comp_rhmc_2p2.py' --> Fig. 8
   'plot_poly.py' --> Fig. 9
   'Dw_distributions.py' --> Fig. 10
   'plot_data_puregauge_scan' and 'plot_data_nfN_scan.py' with 1 <= N <= 8 --> Figs. 11 and 14
   'plot_hot.py' --> Fig. 12
   'plot_susc.py' --> Fig. 13
   'plot_topcharge_b68.py' and 'plot_topcharge_b69.py' --> Fig. 15
   'plot_WF_E.py' and 'plot_WF_W.py' --> Fig. 16   

All the plots will be automatically saved in 'plots/figures/' and will be exactly with the same style as the ones shown 
in the paper.  
