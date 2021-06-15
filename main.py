import requests
import os



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

def get_data():
	tmp_folder_name = "tmp"

	ensure_folder_exists(tmp_folder_name)

	active_cases_url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto19/CasosActivosPorComuna.csv"
	phases_url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto74/paso_a_paso.csv"

	active_cases_file_name = "active_cases.csv"
	phases_file_name = "phases.csv"

	active_cases_file_path = os.path.join(tmp_folder_name, active_cases_file_name)
	phases_file_path = os.path.join(tmp_folder_name, phases_file_name)

	download_and_save(active_cases_url, active_cases_file_path)
	download_and_save(phases_url, phases_file_path)

def main():
	# Fetch data
	data = get_data()
	# Calculate
	# Plot
	print(data)

if __name__ == "__main__":
	main()