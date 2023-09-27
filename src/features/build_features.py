class TransposeTransformer():
    def __init__(self,col_names_dict):
        # Supposed to be a dictionary to map the column filled with d_1 d_2 into the normal date   
        self.col_names=col_names_dict
        
    def transform(self,x):
        # Renaming the column
        x.rename(columns=self.col_names, inplace=True)
        
        # Transpose the DataFrame
        transposed_df = x.transpose()
        
        return transposed_df
        
    def fit(self,x,y=None):
        return self