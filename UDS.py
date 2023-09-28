import pandas as pd
import itertools

#function to get uds data, takes in excel file and sheet nameas paramater
#returns array of dataframes for every state
def get_uds_data(excel_file, sheet_name, year):
	#get data
	ehb = pd.read_excel(excel_file,sheet_name = sheet_name, index_col=0)
	#get unique names/states
	ehb.index.unique()
	#split dataframe into datafrmes per state
	df_list = [d for _, d in ehb.groupby(level = 0)]
	UDS_arr= []

	for i in df_list:
	    
	    #rename value to name of state
	    #i = i.rename(columns = {"value":i.index[0]})
	    #get index
	    state = i.index[0] 
	    #Transpose dataframe
	    i = i.T
	    #get column unique names 
	    i.columns = i.iloc[4]+" "+i.iloc[3]

	    #get values
	    df = i.iloc[-1]
	    #transpose into dataframe
	    df = df.to_frame().T
	    df["State"] = state 
	    df["Pharmacy"] = df[df.columns[0]]
	    df['year'] = year
	    df = df.set_index("State")
	    year = df.pop("year")
	    df.insert(1,"year",year)
	    # df = df.reset_index()
	    UDS_arr.append(df)

	UDS_df =UDS_arr[0]
	for i in UDS_arr[1:]:
		UDS_df = pd.concat([UDS_df,i], axis = 0)


	return UDS_df


#enter data in correct order
#combine all dataframes in order
def combine_dataframes(array_of_dataframes_A, array_of_dataframes_B):
	#result = pd.concat([array_of_dataframes_A,array_of_dataframes_B], axis = 0)
	#for x, y in itertools.zip_longest(array_of_dataframes_A, array_of_dataframes_B):
		# frames = [x,y]
		# result = pd.concat(frames, axis	= 0)
		
	# result = pd.merge(array_of_dataframes_A, array_of_dataframes_B, left_index=True, right_index=True, how='outer')
	result = array_of_dataframes_A.append(array_of_dataframes_B, ignore_index = True)
	#combined.append(result)
	return result
	




def to_excel(dataframe, excel_name):
	dataframe.to_excel(excel_name)


