import pandas as pd, sqlite3
from Config import root_dir_final_df as rd
import os

class StringSearch():
    def __init__(self,input_string):
        self.input_string = input_string

    def string_search(self):
        #loading the data frames
        prefix_file = os.path.join(rd, "medical_terms_prefix.csv")
        root_file = os.path.join(rd, "medical_terms_root.csv")
        suffix_file = os.path.join(rd, "medical_terms_suffix.csv")
        prefix_df = pd.read_csv(prefix_file)
        root_df = pd.read_csv(root_file)
        suffix_df = pd.read_csv(suffix_file)


        #replace "-"
        suffix_df['WordPart:Suffix'] = suffix_df['WordPart:Suffix'].str.replace("-",'')
        prefix_df['WordPart:Prefix'] = prefix_df['WordPart:Prefix'].str.replace("-",'')
        root_df['WordPart:Root'] = root_df['WordPart:Root'].str.replace("-",'')

        #Split the df into parts > Split based on ','
        prefix_df["parts"] = prefix_df["WordPart:Prefix"].str.split(",")
        root_df["parts"] = root_df['WordPart:Root'].str.split(",")
        suffix_df["parts"] = suffix_df['WordPart:Suffix'].str.split(",")

        #Explode the df to add split
        suffix_df = suffix_df.explode("parts")
        prefix_df = prefix_df.explode("parts")
        root_df = root_df.explode("parts")

        #Remove the spaces
        suffix_df['parts'] = suffix_df['parts'].str.replace(" ", '')
        prefix_df['parts'] = prefix_df['parts'].str.replace(" ", '')
        root_df['parts'] = root_df['parts'].str.replace(" ", '')

        #Split Connecting Vowel
        prefix_df[["Prefix", "Connecting_Vowel_prefix1"]] = prefix_df['parts'].str.split("/", expand = True)
        root_df[["Root", "Connecting_Vowel_root-1","Connecting_Vowel_root-2","Connecting_Vowel_root-3"]] = root_df["parts"].str.split("/", expand=True)

        #Matching logic
        matched_suffix_list = []
        matched_prefix_list = []
        matched_root_list = []
        acceptable_df = [suffix_df, prefix_df,root_df]
        for input_dataframe in acceptable_df:
            for idx,row in input_dataframe.iterrows():
                if input_dataframe.equals(suffix_df):
                    if row['parts'] in self.input_string:
                        matched_suffix_list.append(row['parts'])
                if input_dataframe.equals(prefix_df):
                    if row['Prefix'] in self.input_string:
                        matched_prefix_list.append(row['Prefix'])
                if input_dataframe.equals(root_df):
                    if row['Root'] in self.input_string:
                        matched_root_list.append(row['Root'])
        if matched_suffix_list == [] and matched_root_list == [] and matched_suffix_list == []:
            final_output_2 =  {"Prefix" : "Input field doesn't Exist",
                             "Suffix" :"Input field doesn't Exist",
                             "Root" : "Input field doesn't Exist"}
        else:
            output_dict = {
        "Prefix": sorted(set(matched_prefix_list), key=len, reverse=True)[0] if matched_prefix_list else None,
        "Root":   sorted(set(matched_root_list), key=len, reverse=True)[0] if matched_root_list else None,
        "Suffix": sorted(set(matched_suffix_list), key=len, reverse=True)[0] if matched_suffix_list else None
            }
            if (output_dict["Root"] if output_dict["Root"] else '') + output_dict["Suffix"] == self.input_string:
                final_output_1 =  {
                        "Root" : sorted(list(set(matched_root_list)),key = len, reverse = True)[0] if matched_root_list else None,
                        "Suffix": sorted(list(set(matched_suffix_list)), key = len, reverse = True)[0] if matched_suffix_list else None }
                unique_list_suffix = suffix_df[suffix_df["parts"] == final_output_1["Suffix"]].values.tolist()
                unique_list_root = root_df[root_df["Root"] == final_output_1["Root"]].values.tolist()

                final_output_2 = {
                    "Suffix": {
                    "Suffix": final_output_1["Suffix"],
                    "Meaning": unique_list_suffix[0][1] if unique_list_suffix else None
                    },
                    "Root": {
                    "Root": final_output_1["Root"],
                    "Meaning": unique_list_root[0][1] if unique_list_root else None,
                    "Connecting Vowel": unique_list_root[4:] if unique_list_root else None
                    }
                    }








            else:
                final_output_1 = {
                "Prefix": sorted(set(matched_prefix_list), key=len, reverse=True)[0] if matched_prefix_list else None,
                "Root":   sorted(set(matched_root_list), key=len, reverse=True)[0] if matched_root_list else None,
                "Suffix": sorted(set(matched_suffix_list), key=len, reverse=True)[0] if matched_suffix_list else None
            }

                unique_list_prefix = prefix_df[prefix_df["Prefix"] == final_output_1["Prefix"]].values.tolist()
                unique_list_suffix = suffix_df[suffix_df["parts"] == final_output_1["Suffix"]].values.tolist()
                unique_list_root = root_df[root_df["Root"] == final_output_1["Root"]].values.tolist()

                final_output_2 =  { "Prefix" : {
                    "Prefix" : final_output_1["Prefix"],
                    "Meaning":   unique_list_prefix[0][1] if  unique_list_prefix else None ,
                    "Connecting Vowel": unique_list_prefix[0][4] if  unique_list_prefix else None
                },
                "Suffix" : {
                    "Suffix": final_output_1["Suffix"],
                    "Meaning": unique_list_suffix[0][1] if unique_list_suffix else None
                },
                    "Root": {
                        "Root": final_output_1["Root"],
                        "Meaning": unique_list_root[0][1] if unique_list_root else None,
                        "Connecting Vowel": unique_list_root[0][4:] if unique_list_root else None
                }
                }
        return final_output_2




