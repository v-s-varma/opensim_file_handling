In example branch

# opensim_file_handling
This repository contains simple codes to manipulate data in files related to Opensim


marker_hearders_replace.py is a very specific small code that was written so that the 'table-headers' in the '.trc' files can be replaced so that they contain underscores instead of spaces in their names. This was required as Opensim is unable to read the files if the headers contain spaces, and there were a large number of files to be processed. These files contain motion capture data collected from gait labs and are required by Opensim (an open source musculoskeletal modelling and simulation software). Here is the url to Opensim website https://opensim.stanford.edu.

Basically this code searches for '.trc' files in a specific directory and when found reads it in, replaces the headers and overwrites the new file in the same location. The program is run from console as such: "python marker_hearders_replace.py", then the directory contaning the '.trc' file must be navigated to, then let the program do the work.

Here a sample folder named "files" containing '.trc' and '.mot' files has been provided to test the code. It only selects the '.trc' files and replaces the headers inside them.

~vsv/00001
