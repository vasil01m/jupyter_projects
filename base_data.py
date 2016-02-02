import os
import pandas as pd
import matplotlib.pyplot as plt


SAVING_PATH = os.path.expanduser('~/Documents')
FOLDER_DATA = os.path.join(SAVING_PATH, 'books/machine_learning/islr_data/')

BOLD = '\033[1m'
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'


def ex(str_):
    return BOLD + GREEN + str_ + END


def warn(str_):
    return BOLD + RED + str_ + END


class DataContainer(object):
    '''Class to that interfaces with dataset through a pandas dataframe,
    collection of many utilities for the dataframe. To be used in the exercises
    of ISLR

    :param fp: filepath of csv file
    :param na_val: string of symbols - separated by `,` - that will be NaN in
                   the data.(default=`'?, ,unknown'`)
    '''

    def __init__(self, fp, clean={}, na_val='?, ,unknown'):
        self.filepath = fp
        self.na_val = na_val.split(',')
        self.df = self.df_from_csv()
        if clean:
            print 'Asked to clean the dataframe.'
            print 'Dimension before cleaning is {0}.'.format(self.dim_data())
            self.delete_row_by_value(clean)

    def __repr__(self):
        return 'Dataframe originated using csv file %s.' % self.filepath

    def df_from_csv(self):
        '''reads a csv file and return a pandas dataframe object it automatically
        set to NaN data that are '?'. To set more na recogniser provide a list
        of characters separated with a comma, e.g. '?,!,unknown'
        '''
        return pd.read_csv(self.filepath, na_values=self.na_val)

    def delete_row_by_value(self, del_dict):
        '''from self dataframe delete rows if column 'X' has value 'Y':
        :param del_dict: dictionary with key=column name and value the value to
                        be deleted: e.g. {'X': 'Y', ...}
        '''
        if not isinstance(del_dict, dict):
            raise ValueError(
                'In order to clean the data need to provide a dictionary!'
            )
        for k in del_dict:
            if isinstance(del_dict[k], list):
                for i in del_dict[k]:
                    self.df = self.df[self.df[k] != i]
            else:
                self.df = self.df[self.df[k] != del_dict[k]]
        return

    def delete_col(self, col_name):
        '''Delete the column(s) given in `col_name`, either one or more, e.g.
            `col_name = ['col_1', 'col_5',]`
        :param col_name: either list or one string that identify a df column
        '''
        if isinstance(col_name, list):
            for col in col_name:
                self.df = self.df.drop(col, axis=1)
        else:
            self.df = self.df.drop(col_name, axis=1)
        return

    def dim_data(self):
        '''return tuple with dimensions of pandas dataframe object,
        i.e. pair (row, columns)
        '''
        return self.df.shape

    def describe_data(self):
        return self.df.describe()

    def general_description(self):
        print self
        print ex('Data description:')
        print self.describe_data()
        print ex('Dimension:')
        print self.dim_data()

    def name_variables(self, list_return=True):
        '''return the name of the columns of the datafram as list if list_return
        otherwise as numpy.ndarray

        NB the same could be done with `list(df)` or `df.columns.tolist()`, but
        our choice is the fastest one
        '''
        return list(
            self.df.columns.values) if list_return else self.df.columns.values

    def hist_plot(
        self,
        var,
        bin_size=50,
        show=True,
        save=False,
        filename='hist_test.png'
    ):
        self.df[var].hist(bins=bin_size)
        if save:
            plt.savefig(filename)
        if show:
            plt.show()

    def scatter_plot(
        self,
        var1,
        var2,
        title_,
        show=True,
        save=False,
        filename='scatter_test.png'
    ):
        '''display and save a scatter plot of the data corresponding the two
        requested variables. Assume that they have int/float value or Yes/No
        in which case transate Yes=1, No=0
        -----
        For now this last funct does not work
        -----
        '''
        if var1 == var2:
            print 'Same variables'
            return 1

        try:
            [int(x) for x in self.df[var1]]
            print '%s has numbers' % var1
        except ValueError:
            print '%s has not all numbers' % var1
            # df[var1] = (df[var1] == 'Yes').astype(int)
            return 1

        try:
            [int(x) for x in self.df[var2]]
            print '%s has numbers' % var2
        except ValueError:
            print '%s has not all numbers' % var2
            # df[var2] = (df[var2] == 'Yes').astype(int)
            return 1

        try:
            print 'Plotting graphs with x=%s and y=%s' % (var1, var2)
            plt.scatter(self.df[var1], self.df[var2])
            plt.title(title_)
        except:
            print 'One of the two has non number values. %s, %s' % (var1, var2)
            return 1

        if save:
            print 'asked to save..'
            plt.savefig(filename)
        if show:
            plt.show()
        return 0

    def pairs_plot(
        self,
        show=True,
        save=False,
        filename='pairs_test.png'
    ):
        '''does not work properly!
        '''
        axes = pd.tools.plotting.scatter_matrix(
            self.df,
            alpha=0.2,
            figsize=[1.1, 1]
        )
        plt.tight_layout()
        if save:
            plt.savefig(filename)
        if show:
            plt.show()


def marko_data():
    csv_files = [
        'data/flight_8066207_complete.csv',
        'data/flight_8066209_complete.csv',
        'data/flight_8196069_complete.csv',
        'data/flight_8214244_complete.csv',
        'data/FZW-B737-Classic_Z-FAA_HRE_JNB_125_9aa943148312_7671116.csv',
        'data/FZW-B737-Classic_Z-FAA_HRE_JNB_125_bb599a312285_7671103.csv',
        'data/FZW-B737-Classic_Z-FAA_HRE_JNB_125_fb4f55a49aa4_7670788.csv',
        'data/FZW-B737-Classic_Z-FAA_JNB_BUQ_168_7d1597f0c0d1_7670757.csv',
        'data/FZW-B737-Classic_Z-FAA_JNB_HRE_132_028827f5fb1c_7671099.csv',
        'data/FZW-B737-Classic_Z-FAA_JNB_HRE_132_ff054e508106_7670786.csv',
        'data/FZW-B737-Classic_Z-FAA_JNB_None_120_03b1587bd102_7670771.csv',
        'data/FZW-B737-Classic_Z-FAA_JNB_None_120_0b09cc3116d1_7670853.csv',
        'data/FZW-B737-Classic_Z-FAA_VFA_HRE_149_7908227e9ec4_7670879.csv',
        'data/FZW-B737-Classic_Z-FAB_HRE_JNB_125_577882bc5404_7670830.csv',
        'data/FZW-B737-Classic_Z-FAB_JNB_BUQ_168_89949da86ace_7671078.csv',
        'data/FZW-B737-Classic_Z-FAB_JNB_HRE_120_58081bfcdda6_7671082.csv',
        'data/FZW-B737-Classic_Z-FAB_JNB_HRE_120_6f97a90d26ab_7670854.csv',
        'data/FZW-B737-Classic_Z-FAB_JNB_HRE_132_2eb389d8cb6e_7670891.csv',
        'data/FZW-B737-Classic_Z-FAB_VFA_HRE_149_3ade3e19ad00_7670719.csv',
        'data/JTG-B737-Classic_OY-JTI_MAD_LGG_38_10099ccd0048_7672716.csv',
        'data/SFR-B737-Classic_ZS-JRL_CPT_GRJ_1206_4307d87ba45c_7680179.csv',
        'data/SFR-B737-Classic_ZS-JRL_CPT_JNB_1004_23e7268a82dc_7680173.csv',
        'data/SFR-B737-Classic_ZS-JRL_CPT_JNB_1006_b29e3d3248bf_7680172.csv',
        'data/XLR-B737-Classic_A9C-TXL_BAH_ADJ_None_603cf030f07d_7686152.csv',
    ]
    cleaning_dict = {
        'phase': [1, 5]
    }
    data_obj = DataContainer(csv_files[0], clean=cleaning_dict)
    import pdb; pdb.set_trace()  # breakpoint f23075d0 //


def main():
    marko_data()

if __name__ == '__main__':
    main()
