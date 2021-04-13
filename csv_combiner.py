#!/usr/bin/env python

import pandas as pd
import os
import sys

def combine_csv(input_filenames, final_column_list, chunksize, output_file):
    chunks_per_file = []
    try:
        for i in range(0, len(input_filenames)):
            # chunking to handle memory limit being reached
            for chunk in pd.read_csv(input_filenames[i], chunksize=chunksize):
                chunk["filename"] = os.path.basename(input_filenames[i]) # remove directory from filename
                chunks_per_file.append(chunk)
    except pd.errors.EmptyDataError:
        print("One or more of the input files is empty. Execution stopped.")
    except pd.errors.ParserError:
        print("One or more of the input files is an invalid csv file. Execution stopped.")
    except FileNotFoundError:
        print("One or more of the input files not found. Execution stopped.")
    else:
        columns_matched = all(list(chunk.columns) == final_column_list for chunk in chunks_per_file)
        if columns_matched:
            stacked_df = pd.concat(chunks_per_file, axis = 0)
            stacked_df.to_csv(output_file, chunksize=chunksize, index=False, line_terminator='\n')
        else:
            print("One or more input files have invalid column names or sequences. Execution stopped.")

def main():
    # modify input check if more than 2 input files
    if len(sys.argv) != 3:
        print("Incorrect command length. Execution stopped.")
    else:
        final_column_list = ["email_hash", "category", "filename"] # modifiable
        chunksize = 10**5 # modifiable
        combine_csv(sys.argv[1:], final_column_list, chunksize, sys.stdout)
        
if __name__ == '__main__':
    main()
