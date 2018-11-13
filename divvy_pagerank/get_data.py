import requests
import zipfile
import io
import os


def get_ride_data():
    divvy_file = 'https://s3.amazonaws.com/divvy-data/tripdata/Divvy_Trips_2018_Q2.zip'

    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, "../data/")

    r = requests.get(divvy_file)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(file_name)


def get_station_data():
    # TODO get data from API
    pass


def main():
    if not os.path.exists("../data/Divvy_Trips_2018_Q2.csv"):
        get_ride_data()
    else:
        print("file already exists")


if __name__ == '__main__':
    main()
