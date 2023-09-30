




class TransposeTransformer():
    """
    Transpose dataframe and map the index name following a dictionary. This function is meant to be used to transpose the sales dataframe, please put the dictionary to map d_1, etc to timestamp format
    
    """
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
    
    
    
    
    
    
class MeltTransformer():
    """
    This function is meant to melt the sales dataframe to the shape that is workable for machine learning.
    Upon instating, provide the list of id_vars ( variable that dont want to be melted ), variable name ( variable name for columns that were melted),
    value_name.
    
    
    """
    def __init__(self,list_id_vars,var_name,value_name):
        
        self.list_id_vars=list_id_vars
        self.var_name=var_name
        self.value_name=value_name
        
    def transform(self,df):
        
         melted_df=pd.melt(df, id_vars=self.list_id_vars, var_name=self.var_name, value_name=self.value_name)
            
         return melted_df  
    
    def fit(self,x,y=None):
        return self
        
          
            
            
class ImputeCategorical():
    """
    Function to impute values on categorical columns
    """
    def __init__(self):
        
    def fit (self,x,y=None):
        return self
    
    def transform (self,df,cols_list_to_impute,value_to_input):
        df[cols_list_to_impute].fillna(value_to_input, inplace=True)
