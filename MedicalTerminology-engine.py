#Read the tables and export them in a database
import pandas as pd
import os
from Config import root_dir_final_df as rd , pdftables_csv as ps


def datacleaning():
    filenames = os.listdir(ps)
    filenames.sort(key = str.lower)
    prefix_df = pd.DataFrame(columns=["WordPart:Prefix",'Meaning'])
    root_df = pd.DataFrame(columns=["WordPart:Root",'Meaning'])
    suffix_df = pd.DataFrame(columns=["WordPart:Suffix",'Meaning'])
    file_list = []
    for file in filenames:
        pdf_df = pd.read_csv(os.path.join(ps,file))
        pdf_df.columns = [pdf_df.columns[0].replace(' ',''), 'Meaning']
        if 'Prefix' in pdf_df.columns[0]:
            pdf_df.columns = ['WordPart:Prefix', 'Meaning']
            prefix_df = pd.concat([prefix_df,pdf_df],axis = 0 )
        if 'Suffix' in pdf_df.columns[0].replace(' ','') :
            pdf_df.columns = ['WordPart:Suffix', 'Meaning']
            suffix_df = pd.concat([suffix_df,pdf_df],axis = 0 )
        if 'Root' in pdf_df.columns[0].replace(' ','') :
            pdf_df.columns = ['WordPart:Root', 'Meaning']
            root_df = pd.concat([root_df,pdf_df],axis = 0 )
        if ('WordPart:Prefix' in pdf_df.columns[0] or 'WordPart:Suffix' in pdf_df.columns[0] or 'WordPart:Root' in pdf_df.columns[0]) != True:
            file_list.append(file)

    if not os.path.exists(rd):
        os.makedirs(rd, exist_ok=True)

    prefix_file = os.path.join(rd, "medical_terms_prefix.csv")
    root_file = os.path.join(rd, "medical_terms_root.csv")
    suffix_file = os.path.join(rd, "medical_terms_suffix.csv")
    prefix_df.to_csv(prefix_file, index=False)
    root_df.to_csv(root_file, index=False)
    suffix_df.to_csv(suffix_file, index=False)
    return file_list