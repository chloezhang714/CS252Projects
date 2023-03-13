'''transformation.py
Perform projections, translations, rotations, and scaling operations on Numpy ndarray data.
YOUR NAME HERE
CS 251 Data Analysis Visualization
Spring 2023
'''
import numpy as np
import matplotlib.pyplot as plt
import palettable
import analysis
import data

class Transformation(analysis.Analysis):

    def __init__(self, orig_dataset, data = None):
        super().__init__(data)
        self.orig_dataset = orig_dataset
        # '''Constructor for a Transformation object

        # Parameters:
        # -----------
        # orig_dataset: Data object. shape=(N, num_vars).
        #     Contains the original dataset (only containing all the numeric variables,
        #     `num_vars` in total).
        # data: Data object (or None). shape=(N, num_proj_vars).
        #     Contains all the data samples as the original, but ONLY A SUBSET of the variables.
        #     (`num_proj_vars` in total). `num_proj_vars` <= `num_vars`

        # TODO:
        # - Pass `data` to the superclass constructor.
        # - Create an instance variable for `orig_dataset`.
        # '''
        # pass

    def project(self, headers = None):
        if headers == None:
            head = self.orig_dataset.get_headers()
            header2col = {}
            for i, j in enumerate(headers):
                header2col[j] = i  
            self.data = data.Data(data = self.orig_dataset.get_all_data(), headers = head, header2col = header2col)
        else:
            projected_data = self.orig_dataset.select_data(headers)
            header2col = {}
            for i, j in enumerate(headers):
                header2col[j] = i  
            self.data = data.Data(data = projected_data, headers = headers, header2col = header2col)
        #print(self.data.get_all_data())
        
        #modified the function a bit so that it could take no headers and that would mean keep all the data 
        # '''Project the original dataset onto the list of data variables specified by `headers`,
        # i.e. select a subset of the variables from the original dataset.
        # In other words, your goal is to populate the instance variable `self.data`.

        # Parameters:
        # -----------
        # headers: Python list of str. len(headers) = `num_proj_vars`, usually 1-3 (inclusive), but
        #     there could be more.
        #     A list of headers (strings) specifying the feature to be projected onto each axis.
        #     For example: if headers = ['hi', 'there', 'cs251'], then the data variables
        #         'hi' becomes the 'x' variable,
        #         'there' becomes the 'y' variable,
        #         'cs251' becomes the 'z' variable.
        #     The length of the list matches the number of dimensions onto which the dataset is
        #     projected — having 'y' and 'z' variables is optional.

        # TODO:
        # - Create a new `Data` object that you assign to `self.data` (project data onto the `headers`
        # variables). Determine and fill in 'valid' values for all the `Data` constructor
        # keyword arguments (except you dont need `filepath` because it is not relevant here).
        # '''
        # pass

    def get_data_homogeneous(self):
        homogenized_data = self.data.get_all_data()
        # print(self.data.get_num_samples())
        homogenized_data = np.append(homogenized_data, np.array([np.ones(self.data.get_num_samples(), dtype=int)]).T, axis=1)
        return homogenized_data
        # '''Helper method to get a version of the projected data array with an added homogeneous
        # coordinate. Useful for homogeneous transformations.

        # Returns:
        # -----------
        # ndarray. shape=(N, num_proj_vars+1). The projected data array with an added 'fake variable'
        # column of ones on the right-hand side.
        #     For example: If we have the data SAMPLE (just one row) in the projected data array:
        #     [3.3, 5.0, 2.0], this sample would become [3.3, 5.0, 2.0, 1] in the returned array.

        # NOTE:
        # - Do NOT update self.data with the homogenous coordinate.
        # '''
        # pass

    def translation_matrix(self, magnitudes):
        translateTransform = np.eye(self.data.get_num_dims()+2, dtype=float)
        for i in range(self.data.get_num_dims()+1):
             translateTransform[i, self.data.get_num_dims()+1] = magnitudes[i]
        return translateTransform
        # ''' Make an M-dimensional homogeneous transformation matrix for translation,
        # where M is the number of features in the projected dataset.

        # Parameters:
        # -----------
        # magnitudes: Python list of float.
        #     Translate corresponding variables in `headers` (in the projected dataset) by these
        #     amounts.

        # Returns:
        # -----------
        # ndarray. shape=(num_proj_vars+1, num_proj_vars+1). The transformation matrix.

        # NOTE: This method just creates the translation matrix. It does NOT actually PERFORM the
        # translation!
        # '''
        # pass

    def scale_matrix(self, magnitudes):
        scaleTransform = np.eye(self.data.get_num_dims()+2, dtype=float)
        for i in range(self.data.get_num_dims()+1):
            scaleTransform[i, i] = magnitudes[i]
        #print(scaleTransform)
        return scaleTransform
        # '''Make an M-dimensional homogeneous scaling matrix for scaling, where M is the number of
        # variables in the projected dataset.

        # Parameters:
        # -----------
        # magnitudes: Python list of float.
        #     Scale corresponding variables in `headers` (in the projected dataset) by these amounts.

        # Returns:
        # -----------
        # ndarray. shape=(num_proj_vars+1, num_proj_vars+1). The scaling matrix.

        # NOTE: This method just creates the scaling matrix. It does NOT actually PERFORM the scaling!
        # '''
        # pass

    def translate(self, magnitudes):
        translateTransform = self.translation_matrix(magnitudes = magnitudes)
        #print(translateTransform)
        dat = (translateTransform @ self.get_data_homogeneous().T).T
        #print(dat)
        dat = np.delete(dat, -1, axis = 1)
        self.data = data.Data(data = dat, headers = self.data.get_headers(), header2col= self.data.header2col)
        return dat
        # '''Translates the variables `headers` in projected dataset in corresponding amounts specified
        # by `magnitudes`.

        # Parameters:
        # -----------
        # magnitudes: Python list of float.
        #     Translate corresponding variables in `headers` (in the projected dataset) by these amounts.

        # Returns:
        # -----------
        # ndarray. shape=(N, num_proj_vars). The translated data (with all variables in the projected).
        #     dataset. NOTE: There should be NO homogenous coordinate!

        # TODO:
        # - Use matrix multiplication to translate the projected dataset, as advertised above.
        # - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        # dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        # transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a homogenous
        # coordinate!
        # '''
        # pass

    def scale(self, magnitudes):
        scaleTransform = self.scale_matrix(magnitudes = magnitudes)
        #print(scaleTransform)
        dat = (scaleTransform @ self.get_data_homogeneous().T).T
        dat = np.delete(dat, -1, axis = 1)
        self.data = data.Data(data = dat, headers = self.data.get_headers(), header2col= self.data.header2col)
        return dat
        # '''Scales the variables `headers` in projected dataset in corresponding amounts specified
        # by `magnitudes`.

        # Parameters:
        # -----------
        # magnitudes: Python list of float.
        #     Scale corresponding variables in `headers` (in the projected dataset) by these amounts.

        # Returns:
        # -----------
        # ndarray. shape=(N, num_proj_vars). The scaled data (with all variables in the projected).
        #     dataset. NOTE: There should be NO homogenous coordinate!

        # TODO:
        # - Use matrix multiplication to scale the projected dataset, as advertised above.
        # - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        # dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        # transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a
        # homogenous coordinate!
        # '''
        # pass


#week 2
    def transform(self, C):
        dat = (C @ self.get_data_homogeneous().T).T
        dat = np.delete(dat, -1, axis = 1)
        self.data = data.Data(data = dat, headers = self.data.get_headers(), header2col= self.data.header2col)
        return dat
        # '''Transforms the PROJECTED dataset by applying the homogeneous transformation matrix `C`.

        # Parameters:
        # -----------
        # C: ndarray. shape=(num_proj_vars+1, num_proj_vars+1).
        #     A homogeneous transformation matrix.

        # Returns:
        # -----------
        # ndarray. shape=(N, num_proj_vars). The projected dataset after it has been transformed by `C`

        # TODO:
        # - Use matrix multiplication to apply the compound transformation matix `C` to the projected
        # dataset.
        # - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        # dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        # transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a homogenous
        # coordinate!
        # '''
        # pass

    def normalize_together(self):
        
        '''Normalize all variables in the projected dataset together by translating the global minimum
        (across all variables) to zero and scaling the global range (across all variables) to one.

        You should normalize (update) the data stored in `self.data`.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The normalized version of the projected dataset.

        NOTE: Given the goal of this project, for full credit you should implement the normalization
        using matrix multiplications (matrix transformations).
        '''
        pass

    def normalize_separately(self):
        '''Normalize each variable separately by translating its local minimum to zero and scaling
        its local range to one.

        You should normalize (update) the data stored in `self.data`.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The normalized version of the projected dataset.

        NOTE: Given the goal of this project, for full credit you should implement the normalization
        using matrix multiplications (matrix transformations).
        '''
        pass

    def rotation_matrix_3d(self, header, degrees):
        '''Make an 3-D homogeneous rotation matrix for rotating the projected data
        about the ONE axis/variable `header`.

        Parameters:
        -----------
        header: str. Specifies the variable about which the projected dataset should be rotated.
        degrees: float. Angle (in degrees) by which the projected dataset should be rotated.

        Returns:
        -----------
        ndarray. shape=(4, 4). The 3D rotation matrix with homogenous coordinate.

        NOTE: This method just creates the rotation matrix. It does NOT actually PERFORM the rotation!
        '''
        pass

    def rotate_3d(self, header, degrees):
        '''Rotates the projected data about the variable `header` by the angle (in degrees)
        `degrees`.

        Parameters:
        -----------
        header: str. Specifies the variable about which the projected dataset should be rotated.
        degrees: float. Angle (in degrees) by which the projected dataset should be rotated.

        Returns:
        -----------
        ndarray. shape=(N, num_proj_vars). The rotated data (with all variables in the projected).
            dataset. NOTE: There should be NO homogenous coordinate!

        TODO:
        - Use matrix multiplication to rotate the projected dataset, as advertised above.
        - Update `self.data` with a NEW Data object with the SAME `headers` and `header2col`
        dictionary as the current `self.data`, but DIFFERENT data (set to the data you
        transformed in this method). NOTE: The updated `self.data` SHOULD NOT have a
        homogenous coordinate!
        '''
        pass

    def scatter_color(self, ind_var, dep_var, c_var, title=None):
        color_map = palettable.colorbrewer.sequential.Purples_9
        x = self.orig_dataset.select_data(ind_var)
        y = self.orig_dataset.select_data(dep_var)
        z = self.orig_dataset.select_data(c_var)
        #print(self.data.get_all_data())
        #print(x)
        plt.scatter(x, y, c=z, s=75, cmap=color_map.mpl_colormap, edgecolor='black')
        plt.title(title)
        plt.xlabel(ind_var)
        plt.ylabel(dep_var)
        plt.colorbar(label = c_var)
        '''Creates a 2D scatter plot with a colo)r scale representing the 3rd dimension.

        Parameters:
        -----------
        ind_var: str. Header of the variable that will be plotted along the X axis.
        dep_var: Header of the variable that will be plotted along the Y axis.
        c_var: Header of the variable that will be plotted along the color axis.
            NOTE: Use a ColorBrewer color palette (e.g. from the `palettable` library).
        title: str or None. Optional title that will appear at the top of the figure.
        '''
        pass
