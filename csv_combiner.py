#!/usr/bin/env python

import pandas as pd
import os
import sys

def combine_csv(input_filenames, final_column_list, chunksize, output_file):
    first_row_check = True
    curr_mode = 'w+'
    try:
        for i in range(0, len(input_filenames)):
            # chunking to handle memory limit being reached
            for chunk in pd.read_csv(input_filenames[i], chunksize=chunksize):
                chunk["filename"] = os.path.basename(input_filenames[i]) # remove directory from filename
                if list(chunk.columns) == final_column_list:
                    chunk.to_csv(output_file, mode=curr_mode, header=first_row_check, index=False, line_terminator='\n')
                    if first_row_check == True: first_row_check = False
                    if curr_mode == 'w+': curr_mode = 'a'
                else:
                    print("One or more input files have invalid column names or sequences. Execution stopped.")
    except pd.errors.EmptyDataError:
        print("One or more of the input files is empty. Execution stopped.")
    except pd.errors.ParserError:
        print("One or more of the input files is an invalid csv file. Execution stopped.")
    except FileNotFoundError:
        print("One or more of the input files not found. Execution stopped.")

def main():
    # modify input check if more than 2 input files
    if len(sys.argv) != 3:
        print("Incorrect command length. Execution stopped.")
    else:
        final_column_list = ["email_hash", "category", "filename"] # modifiable
        chunksize = 10**6 # modifiable
        combine_csv(sys.argv[1:], final_column_list, chunksize, sys.stdout)
        
if __name__ == '__main__':
    main()
