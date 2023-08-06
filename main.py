import matplotlib.pyplot as plt
import pandas as pd


def extract_data(filepath):
    test_drive_data = pd.read_json(filepath)

    # Extract data from json
    time_data = []
    torque_nm_data = []
    power_ps_data = []
    tire_pressure_psi_data = []
    drag_data = []
    oil_temperature_celsius_data = []
    tire_temperature_celsius_data = []
    velocity_kmh_data = []

    for i in range(len(test_drive_data["measurements"])):
        time_data.append(test_drive_data["measurements"][i]["time"])
        torque_nm_data.append(test_drive_data["measurements"][i]["torque_nm"])
        power_ps_data.append(test_drive_data["measurements"][i]["horsepower_ps"])
        tire_pressure_psi_data.append(test_drive_data["measurements"][i]["tire_pressure_psi"])
        drag_data.append(test_drive_data["measurements"][i]["drag"])
        oil_temperature_celsius_data.append(test_drive_data["measurements"][i]["oil_temperature_celsius"])
        tire_temperature_celsius_data.append(test_drive_data["measurements"][i]["tire_temperature_celsius"])
        velocity_kmh_data.append(test_drive_data["measurements"][i]["velocity_kmh"])

    # Print data lists
    print("Time Data:", time_data)
    print("Torque Data:", torque_nm_data)
    print("Power Data:", power_ps_data)
    print("Tire Pressure Data:", tire_pressure_psi_data)
    print("Drag Data:", drag_data)
    print("Oil Temperature Data:", oil_temperature_celsius_data)
    print("Tire Temperature Data:", tire_temperature_celsius_data)
    print("Velocity Data:", velocity_kmh_data)

    # Create dictionary which stores the json data in lists
    extracted_data = {
        "time": time_data,
        "torque_nm": torque_nm_data,
        "power_ps": power_ps_data,
        "tire_pressure_psi": tire_pressure_psi_data,
        "drag": drag_data,
        "oil_temperature_celsius": oil_temperature_celsius_data,
        "tire_temperature_celsius": tire_temperature_celsius_data,
        "velocity_kmh": velocity_kmh_data
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
    testdrive_data = extract_data("data.json")

    plot_single_graph(testdrive_data["time"], testdrive_data["torque_nm"], "time", "torque in nm")
    plot_single_graph(testdrive_data["time"], testdrive_data["power_ps"], "time", "power in ps")
    plot_single_graph(testdrive_data["time"], testdrive_data["tire_pressure_psi"], "time", "tire pressure in psi")
    plot_single_graph(testdrive_data["time"], testdrive_data["drag"], "time", "drag")
    plot_single_graph(testdrive_data["time"], testdrive_data["oil_temperature_celsius"], "time", "oil temperature in °C")
    plot_single_graph(testdrive_data["time"], testdrive_data["tire_temperature_celsius"], "time", "tire temperature in °C")
    plot_single_graph(testdrive_data["time"], testdrive_data["velocity_kmh"], "time", "velocity in kmh")

    plot_multi_value_graph(testdrive_data["time"], testdrive_data["velocity_kmh"], testdrive_data["torque_nm"], testdrive_data["power_ps"],
                           "time", "velocity in kmh", "torque in nm", "power in ps")
