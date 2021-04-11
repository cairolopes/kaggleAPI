from kaggleAPI import KaggleAPI

kaggle_API = KaggleAPI()

file_list = kaggle_API.search("bitcoin")
kaggle_API.download_kaggle_files(file_list)