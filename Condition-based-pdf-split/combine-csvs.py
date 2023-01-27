import os, csv, pandas as pd

def generate_csv_using_pandas(output_df, base_folder):
    output_df.to_csv(os.path.join(base_folder, 'Final_statewise_covid_data.csv'), index=False)

def generate_csv_using_DictFn(output_df, base_folder):
    dict = output_df.to_dict()
    keys = [key for key in dict]

    for key in keys:
        dict.update({key : list(dict[key].values())})

    with open(os.path.join(base_folder, 'Final_statewise_covid_data.csv'), "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(dict.keys())
        writer.writerows(zip(*dict.values()))

def generate_dataframe(csv_files_path):
    csv_files_list = os.listdir(csv_files_path)
    csv_files_list.sort()
    df_list = []
    for csv in csv_files_list:
        csv_path = os.path.join(csv_files_path, csv)
        df = pd.read_csv(csv_path)
        df_list.append(df)
    output_dataframe = pd.concat(df_list, ignore_index=True)
    return output_dataframe

if __name__ == '__main__':
    base_folder, file_name = os.path.split(os.path.realpath(__file__))
    csv_files_path = os.path.join(base_folder, 'Output-CSVs')
    output_df = generate_dataframe(csv_files_path)
    # generate_csv_using_pandas(output_df, base_folder)
    generate_csv_using_DictFn(output_df, base_folder)
