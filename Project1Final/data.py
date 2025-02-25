'''data.py
Reads CSV files, stores data, access/filter data by variable name
Chloe Zhang
CS 251 Data Analysis and Visualization
Spring 2023
'''
import csv

import numpy as np

class Data:
    def __init__(self, filepath = None, headers = None, data = None, header2col = None):
        self.filepath = filepath
        self.headers = headers
        self.data = data
        self.header2l = header2col
        if filepath != None: 
            self.read(filepath)
        else: 
            print("Filepath invalid")
        pass
        # Data object constructor

        # Parameters:
        # -----------
        # filepath: str or None. Path to data .csv file
        # headers: Python list of strings or None. List of strings that explain the name of each
        #     column of data.
        # data: ndarray or None. shape=(N, M).
        #     N is the number of data samples (rows) in the dataset and M is the number of variables
        #     (cols) in the dataset.
        #     2D numpy array of the dataset’s values, all formatted as floats.
        #     NOTE: In Week 1, don't worry working with ndarrays yet. Assume it will be passed in
        #           as None for now.
        # header2col: Python dictionary or None.
        #         Maps header (var str name) to column index (int).
        #         Example: "sepal_length" -> 0

        # TODO:
        # - Declare/initialize the following instance variables:
        #     - filepath
        #     - headers
        #     - data
        #     - header2col
        #     - Any others you find helpful in your implementation
        # - If `filepath` isn't None, call the `read` method.
        
        pass

    def read(self, filepath):
        self.filepath = filepath
        with open(filepath, newline='') as csvfile:
            self.header2col = {}
            self.headers = []
            reader = csv.reader(csvfile)
            headers_t = next(reader)
            #print(headers_t)
            types = next(reader)
            for i,j in enumerate (types):
                j = j.strip()
                # print(i)
                # print("#" + j + "#")
                if j == 'numeric':
                    self.headers.append(headers_t[i])      
            for i, j in enumerate(self.headers):
                j = j.strip()
                self.header2col[j] = i  
            # print(self.headers)
            # print(self.header2col)
            # print('headers header2col success')
            reader = csv.reader(csvfile,delimiter = ',')
            self.data = []
            for row in reader:
                ro = []
                for i in row:
                    try:
                        ro.append((float(i)))
                    except:
                        pass
                self.data.append(ro)
                
        self.data = np.array(self.data)
        #print(self.data)
        #enumerate
        # '''Read in the .csv file `filepath` in 2D tabular format. Convert to numpy ndarray called
        # `self.data` at the end (think of this as 2D array or table).

        # Format of `self.data`:
        #     Rows should correspond to i-th data sample.
        #     Cols should correspond to j-th variable / feature.

        # Parameters:
        # -----------
        # filepath: str or None. Path to data .csv file

        # Returns:
        # -----------
        # None. (No return value).
        #     NOTE: In the future, the Returns section will be omitted from docstrings if
        #     there should be nothing returned

        # TODO:
        # - Read in the .csv file `filepath` to set `self.data`. Parse the file to only store
        # numeric columns of data in a 2D tabular format (ignore non-numeric ones). Make sure
        # everything that you add is a float.
        # - Represent `self.data` (after parsing your CSV file) as an numpy ndarray. To do this:
        #     - At the top of this file write: import numpy as np
        #     - Add this code before this method ends: self.data = np.array(self.data)
        # - Be sure to fill in the fields: `self.headers`, `self.data`, `self.header2col`.

        # NOTE: You may wish to leverage Python's built-in csv module. Check out the documentation here:
        # https://docs.python.org/3/library/csv.html

        # NOTE: In any CS251 project, you are welcome to create as many helper methods as you'd like.
        # The crucial thing is to make sure that the provided method signatures work as advertised.

        # NOTE: You should only use the basic Python library to do your parsing.
        # (i.e. no Numpy or imports other than csv).
        # Points will be taken off otherwise.

        # TIPS:
        # - If you're unsure of the data format, open up one of the provided CSV files in a text editor
        # or check the project website for some guidelines.
        # - Check out the test scripts for the desired outputs.
        # '''
        pass

    def __str__(self):
        tostr = "-------------------------------/n" + self.filepath +"/n Headers:/n" + '   '.join(self.headers) + "/n -------------------------------/n" + "Showing first 5/" + self.get_num_samples+ " rows./n" + self.headers
        return tostr
        # '''toString method

        # (For those who don't know, __str__ works like toString in Java...In this case, it's what's
        # called to determine what gets shown when a `Data` object is printed.)

        # Returns:
        # -----------
        # str. A nicely formatted string representation of the data in this Data object.
        #     Only show, at most, the 1st 5 rows of data
        #     See the test code for an example output.
        # '''
        # pass

    def get_headers(self):
        return self.headers
        # '''Get method for headers

        # Returns:
        # -----------
        # Python list of str.
        # '''
        pass

    def get_mappings(self):
        mapdict = {}
        for i, j in enumerate(self.headers):
            mapdict[j] = i
        return(mapdict)
        # '''Get method for mapping between variable name and column index

        # Returns:
        # -----------
        # Python dictionary. str -> int
        # '''
        # pass

    def get_num_dims(self):
        return(len(self.headers)-1)
        #number of column?? does species count? no ; size/shape of headers
        # '''Get method for number of dimensions in each data sample

        # Returns:
        # -----------
        # int. Number of dimensions in each data sample. Same thing as number of variables.
        # '''
        # pass

    def get_num_samples(self):
        return(np.shape(self.data)[0])
        # '''Get method for number of data points (samples) in the dataset

        # Returns:
        # -----------
        # int. Number of data samples in dataset.
        # '''
        # pass

    def get_sample(self, rowInd):
        return self.data[rowInd-1,:]
        # '''Gets the data sample at index `rowInd` (the `rowInd`-th sample)

        # Returns:
        # -----------
        # ndarray. shape=(num_vars,) The data sample at index `rowInd`
        # '''
        # pass

    def get_header_indices(self, headers):
        rtn = [self.header2col.get(x) for x in headers if self.header2col.get(x) != None]
        #print (rtn)
        return rtn
        # '''Gets the variable (column) indices of the str variable names in `headers`.

        # Parameters:
        # -----------
        # headers: Python list of str. Header names to take from self.data

        # Returns:
        # -----------
        # Python list of nonnegative ints. shape=len(headers). The indices of the headers in `headers`
        #     list.
        # '''
        # pass

    def get_all_data(self):
        return np.copy(self.data)
        # '''Gets a copy of the entire dataset

        # (Week 2)

        # Returns:
        # -----------
        # ndarray. shape=(num_data_samps, num_vars). A copy of the entire dataset.
        #     NOTE: This should be a COPY, not the data stored here itself.
        #     This can be accomplished with numpy's copy function.
        # '''
        # pass

    def head(self):
        return self.data[0:5, :]
        # '''Return the 1st five data samples (all variables)

        # (Week 2)

        # Returns:
        # -----------
        # ndarray. shape=(5, num_vars). 1st five data samples.
        # '''
        # pass

    def tail(self):
        len = self.get_num_samples()
        if(len < 5):
            return self.data[-len:,:]
        else:
            return self.data[-5:, :]
        # '''Return the last five data samples (all variables)

        # (Week 2)

        # Returns:
        # -----------
        # ndarray. shape=(5, num_vars). Last five data samples.
        # '''
        # pass
        
        
    def limit_samples(self, start_row, end_row):
       #?  start_row start from 0 or 1? rn it's 1
        self.data = self.data[(start_row):(end_row)]
        # '''Update the data so that this `Data` object only stores samples in the contiguous range:
        #     `start_row` (inclusive), end_row (exclusive)
        # Samples outside the specified range are no longer stored.

        # (Week 2)

        # '''
        # pass

    def select_data(self, headers, rows = []):
        col = self.get_header_indices(headers) 
        if rows == []:
            return self.data[:,col]
        else:
            return self.data[np.ix_(rows,col)]
        # '''Return data samples corresponding to the variable names in `headers`.
        # If `rows` is empty, return all samples, otherwise return samples at the indices specified
        # by the `rows` list.

        # (Week 2)
        # np.ix_ gets a mesh
        # For example, if self.headers = ['a', 'b', 'c'] and we pass in header = 'b', we return
        # column #2 of self.data. If rows is not [] (say =[0, 2, 5]), then we do the same thing,
        # but only return rows 0, 2, and 5 of column #2.

        # Parameters:
        # -----------
        #     headers: Python list of str. Header names to take from self.data
        #     rows: Python list of int. Indices of subset of data samples to select.
        #         Empty list [] means take all rows

        # Returns:
        # -----------
        # ndarray. shape=(num_data_samps, len(headers)) if rows=[]
        #          shape=(len(rows), len(headers)) otherwise
        #     Subset of data from the variables `headers` that have row indices `rows`.

        # Hint: For selecting a subset of rows from the data ndarray, check out np.ix_
        # '''