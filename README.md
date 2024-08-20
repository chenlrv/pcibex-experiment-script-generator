# **Python Hackathon - Package for behavioral experiments in sentences parsing: Prof. Aya Meltzer**

**Project Description:**
In the lab, behavioral experiments are run using PCIbex, an online java script based
experiment builder. The experiments are different in what they are measuring and how
(reading times, accuracy on comprehension questions, etc), and in the technical parameters (presentation time and mode, order of trials, breaks, etc).

Currently, students in the lab build their own experiments based on previous scripts they have, with the required modifications. This may take several hours per experiment.

**Objectives and Goals:**

We would like to develop a friendly package whereby the students can input the type of
experiment (SPR - Self Paced Reading OR RSVP - Rapid Serial Visual Presentation), their language materials, and the relevant additional parameters, and the package will build the experiment and provide a relevant java script, ready to run in PCIbex.

What is uniuqe about our project is that we are aiming to offer a user-friendly interface to select the wanted parmeters; we aim to create a GUI (Graphical User Interface) that allows researchers to upload their experimental stimuli and make adjustments to the code by choosing their desirable experimental paradigm and specify parameters like SOA (Stimulus onset asynchrony), presentation preferences, factors’names etc.

**The input of the code will be:** 
1) Stimuli files with the experimental materials. 
2) An existing PCIbex scripts as a template.

The template scripts will be modified accoding to the output of the GUI as provided from the users (researchers) and based on thier experimental material. 

**The output:** 
A final PCIbex, java-based script, ready to be run and used to present the final linguistic experiment in the PCIbex platform.

--> The code can be divided into sections corresponding to those found in the template script, so that sections will be modified accordingly step by step. 

**Section #1: Selecting the presentation Paradigm (SPR/RSVP).**

The differnce between the 2 paradigms is basicslly how  the sentence is going to be presented to the participant during the experiment. In SPR participants control the pace of reading by clicking on a previosly specified key, the main goal is to measure the reading times of each word in the sentence. While in RSVP each word is presented in a fixed rate and participants cannot control the pace. This paradigm is mainlly used to examine comprehension when reading in high speeds. 

Based on the input coming from GUI regarding the user choice of the type of the paradigm, a set of different options (requerments) in the GUI will be presented, since each of them is customized with its own set of requerments.

If the paradigm chosen is SPR, in the GUI, users have to choose next the sentence presentation manner (Moving window /Fixed presentation (centered)), they need to fill the numbers of trials between breaks (as an integer), in addition to a text (optional) presented in the break screen. 

If the paradigm chosen is RSVP, in the GUI, the same as in SPR, users have to choose  the sentence presentation manner, but then they need to choose Presentation duration in msec (as an integer/float). Users have to choose InterWord break duration also in msec (integer/float). 

![Flow Chart of the GUI](https://github.com/chenlrv/pcibex-experiment-script-generator/blob/sina/flow%20chart%20GUI.png?raw=true)

**Section #2: Template Modification based on the GUI output.**

In the case of SPR: 
1) Change the template script to fit the presentation manner chosen by the user.
2) Change the template script to have the numbers of trials between breaks (int.) if needed.
3) In case the user wants breaks, change the template script to have the break screen text (optional). 
 
In the case of RSVP:
1) Change the template script to fit the presentation manner chosen by the user.
2) Change the template script to have the Presentation duration of each word in msec (int./float). 
3) Change the template script to have the InterWord break duration in msec (int./float).

**Section #3: Validating the compatibility of the Stimuli experimental materials.**

1) Extract the names of the columns in the csv file of the stimuli. 
2) Specify which column names are essential.  
2) Check whether the names of the columns match the names found in the template script (a list with the essential column names). 
4) Raise a warning if an essential column name is absent and provide a Warning message that explains for the user which column name is that. 
5) Ask the user to change the column names in the csv file based on the names found in the provided list.
6) If a 'cotext' is provided, then it is crucial to refer to that in the code, even though such column is not essential in general. If the GUI output gives 'True' parameter for the existence of a context, then the'context' should be added to the essential column names, and the user should give the corresponding column the right name in the csv file. 
7) The "answer" columns (for the experimental task) are not essential in general, since a Yes/No answer is considered as a defult. A modification is needed if the answers are provided words found in the columns, then these column become essential. Such information is provided in the GUI output, the code should access this type of information and change the status of the "answer" columns accordingly.
8) Last check, to run over the data provided in the csv file and make sure no data is missing. Replace empty values with NaN and raise a warning with the relevant indices. 

Once it is done, Return the final java script as a txt file. 











