import matplotlib.pyplot as plt
import pandas as pd


def extract_data(filepath, value1_name, value2_name, value3_name, value4_name, value5_name, value6_name, value7_name, value8_name):
    json_data = pd.read_json(filepath)

    # Extract data from json
    value1_data = []
    value2_data = []
    value3_data = []
    value4_data = []
    value5_data = []
    value6_data = []
    value7_data = []
    value8_data = []

    for i in range(len(json_data["measurements"])):
        value1_data.append(json_data["measurements"][i][value1_name])
        value2_data.append(json_data["measurements"][i][value2_name])
        value3_data.append(json_data["measurements"][i][value3_name])
        value4_data.append(json_data["measurements"][i][value4_name])
        value5_data.append(json_data["measurements"][i][value5_name])
        value6_data.append(json_data["measurements"][i][value6_name])
        value7_data.append(json_data["measurements"][i][value7_name])
        value8_data.append(json_data["measurements"][i][value8_name])

    # Print data lists
    print(value1_name, value1_data)
    print(value2_name, value2_data)
    print(value3_name, value3_data)
    print(value4_name, value4_data)
    print(value5_name, value5_data)
    print(value6_name, value6_data)
    print(value7_name, value7_data)
    print(value8_name, value8_data)

    # Create dictionary which stores the json data in lists
    extracted_data = {
        value1_name : value1_data,
        value2_name : value2_data,
        value3_name : value3_data,
        value4_name : value4_data,
        value5_name : value5_data,
        value6_name : value6_data,
        value7_name : value7_data,
        value8_name : value8_data
    }

    return extracted_data


def plot_single_graph(x_data, y_data, x_name, y_name):
    # Create a line plot of data
    plt.plot(x_data, y_data, marker='o')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(y_name + " vs. " + x_name)
    plt.grid(True)
    plt.show()


def plot_multi_value_graph(x_data, y_data1, y_data2, y_data3, x_name, y_name1, y_name2, y_name3):
    # Create a multi value plot of data
    plt.plot(x_data, y_data1, "r--", x_data, y_data2, "b--", x_data, y_data3, "g--")
    plt.xlabel(x_name)
    plt.ylabel(y_name1 + " red; " + y_name2 + " blue; " + y_name3 + " green;")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    testdrive_data = extract_data("data/data.json", "time", "torque_nm", "horsepower_ps", "tire_pressure_psi", "drag", "oil_temperature_celsius", "tire_temperature_celsius", "velocity_kmh")

    plot_single_graph(testdrive_data["time"], testdrive_data["torque_nm"], "time", "torque in nm")
    plot_single_graph(testdrive_data["time"], testdrive_data["horsepower_ps"], "time", "horsepower in ps")
    plot_single_graph(testdrive_data["time"], testdrive_data["tire_pressure_psi"], "time", "tire pressure in psi")
    plot_single_graph(testdrive_data["time"], testdrive_data["drag"], "time", "drag")
    plot_single_graph(testdrive_data["time"], testdrive_data["oil_temperature_celsius"], "time", "oil temperature in °C")
    plot_single_graph(testdrive_data["time"], testdrive_data["tire_temperature_celsius"], "time", "tire temperature in °C")
    plot_single_graph(testdrive_data["time"], testdrive_data["velocity_kmh"], "time", "velocity in kmh")

    plot_multi_value_graph(testdrive_data["time"], testdrive_data["velocity_kmh"], testdrive_data["torque_nm"], testdrive_data["horsepower_ps"],
                           "time", "velocity in kmh", "torque in nm", "horsepower in ps")
