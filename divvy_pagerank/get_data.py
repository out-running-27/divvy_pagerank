import requests
import zipfile
import io
import os
import pandas as pd

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "../data/")

def get_ride_data():
    divvy_file = 'https://s3.amazonaws.com/divvy-data/tripdata/Divvy_Trips_2018_Q2.zip'

    r = requests.get(divvy_file)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(data_dir)


def get_station_data():
    api = "https://feeds.divvybikes.com/stations/stations.json"
    columns = ["id", "stationName", "latitude", "longitude"]

    r = requests.get(api).json()
    df = pd.DataFrame(r["stationBeanList"], columns=columns)
    df.set_index("id", inplace=True)

    # write to csv to use in graph
    df.to_csv(data_dir + "station_info.csv")


def main():
    if not os.path.exists("../data/Divvy_Trips_2018_Q2.csv"):
        print("getting ride data")
        get_ride_data()
    else:
        print("file already exists")

    # if not os.path.exists("../data/station_info.csv"):
    print("getting station data")
    get_ride_data()
    # else:
    #     print("file already exists")

    get_station_data()


if __name__ == '__main__':
    main()
