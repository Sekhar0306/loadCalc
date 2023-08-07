def calculate_cooling_load(area, num_occupants, building_type, outdoor_temp, indoor_temp):
    if building_type.lower() == "residential":
        cooling_load = 100 * num_occupants
    elif building_type.lower() == "commercial":
        cooling_load = 150 * num_occupants
    else:
        raise ValueError("Invalid building type. Supported types: residential, commercial")

    u_coefficient = 30
    q_conduction = u_coefficient * area * (outdoor_temp - indoor_temp)
    sensible_cooling_load = q_conduction + cooling_load

    return sensible_cooling_load

try:
    print("21BCI0243 GUNA SEKHAR DEVINENI")
    area = float(input("Enter the area of the building (in square meters): "))
    num_occupants = int(input("Enter the number of occupants in the building: "))
    building_type = input("Enter the type of building (residential/commercial): ")
    outdoor_temp = float(input("Enter the outdoor temperature (in Celsius): "))
    indoor_temp = float(input("Enter the indoor desired temperature (in Celsius): "))

    cooling_load = calculate_cooling_load(area, num_occupants, building_type, outdoor_temp, indoor_temp)
    print(f"The sensible cooling load is: {cooling_load} W")
except ValueError as e:
    print(f"Error: {e}")

