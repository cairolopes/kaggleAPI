import os 
import kaggle

class KaggleAPI:

    def __init__(self):
        # Authenticate -> .kaggle/kaggle.json
        kaggle.api.authenticate()

    def search(self,search):

        SEARCH = str(search)

        kaggle_list = kaggle.api.dataset_list(
                                            search=SEARCH,
                                            file_type="csv",
                                            sort_by="published")[0:2] # Just a test! 
        return kaggle_list

# downlod all files in the list 
    def download_kaggle_files(self, kaggle_files_list):
        
        DOWNLOAD_LOCAL = '.kaggle/data'
        
        for dataset in kaggle_files_list:
            try:
                kaggle.api.dataset_download_files(
                                                str(dataset),
                                                path=DOWNLOAD_LOCAL,
                                                unzip=True)

                print('Download: ', dataset," | ", dataset.title," | ",dataset.size)

            except Exception:
                print('Error:    ',dataset, " | ", dataset.title," | ",dataset.size)


