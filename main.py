import requests
import os
from datetime import datetime
import pandas as pd


def ensure_folder_exists(foldername):
    try:
        # Create tmp folder
        os.mkdir(foldername)
        print("Directory created: " + foldername)
    except FileExistsError:
        pass


def download_and_save(url, filename):
    print("Downloading " + url)
    response = requests.get(url)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)


def file_exists(filename):
    return os.path.isfile(filename)


def get_data():
    tmp_folder_name = "tmp"

    ensure_folder_exists(tmp_folder_name)

    active_cases_url = "https://raw.githubusercontent.com/MinCiencia/\
Datos-COVID19/master/output/producto19/CasosActivosPorComuna.csv"
    phases_url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/\
master/output/producto74/paso_a_paso.csv"

    todays_date_string = str(datetime.date(datetime.now()))

    active_cases_file_name = "active_cases_{}.csv".format(todays_date_string)
    phases_file_name = "phases_{}.csv".format(todays_date_string)

    active_cases_file_path = os.path.join(
        tmp_folder_name, active_cases_file_name)
    phases_file_path = os.path.join(tmp_folder_name, phases_file_name)

    if not (file_exists(active_cases_file_path)):
        download_and_save(active_cases_url, active_cases_file_path)

    if not (file_exists(phases_file_path)):
        download_and_save(phases_url, phases_file_path)

    # Load data

    cases = pd.read_csv(active_cases_file_path)
    phases = pd.read_csv(phases_file_path)

    print(cases)
    print(phases)




def main():
    # Fetch data
    data = get_data()
    # Calculate
    # Plot
    print(data)


if __name__ == "__main__":
    main()
