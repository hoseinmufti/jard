import sys

WORKERFEE_PER_METER_SQUARED = 5
M2_TO_M_CONVERSION_FACTOR = 10000

STD_ALUMINUM_TUBE_MEASUREMENTS = {
    "mainframe": {"length": 600, "weight": 8.4},
    "slash": {"length": 600, "weight": 5.5},
    "antifly": {"length": 600, "weight": 3.5},
    "slit": {"length": 600, "weight": 2.0}
}

ITEMS_PER_MAINFRAME = {"cornerjoint": 8}
ITEMS_PER_SLASH = {"cornerjoint": 4, "wheel": 2, "handle": 1}

PRICES = {"Aluminum kg": 3.8, "Handle":1.85, "Corner Joint": 0.32, "Wheel": 1.75}


windows = [{"w": 193, "h": 245}]

def main():
    for window in windows:
        # Assign number of frames for mainframe and slashashes
        num_mainframes = 1
        num_slashes = 2

        w_per_mainframe = 2
        h_per_mainframe = 2

        w_per_slash = 2
        h_per_slash = 2

        # Assign window width and height
        window_w = window["w"]
        window_h = window["h"]
        slash_w = window_w / w_per_slash

        # Calculate total mainframe length
        total_mainframe_w = window_w * w_per_mainframe
        total_mainframe_h = window_h * h_per_mainframe
        total_mainframe_length = total_mainframe_w + total_mainframe_h

        # Calculate total slash length
        total_slash_w = slash_w * w_per_slash
        total_slash_h = window_h * h_per_slash
        total_slash_length = total_slash_w + total_slash_h

        # Calculate total frames lengths
        total_mainframes_length = total_mainframe_length * num_mainframes
        total_slashes_length = total_slash_length * num_slashes

        # Calculate total mainframes weight
        total_mainframes_weight = convert_length_to_weight("mainframe", total_mainframes_length)
        # Calculate total slashes weight
        total_slashes_weight = convert_length_to_weight("slash", total_slashes_length)
        # Caluclate total antiflies weight
        total_antifly_weight = convert_length_to_weight("antifly", total_slash_length)
        # Calculate total slits weight
        total_slits_length = window_h * num_slashes
        total_slits_weight = convert_length_to_weight("slit", total_slits_length)

        # Calculate total aluminum tubes weight
        total_aluminum_weights = [total_mainframes_weight, total_slashes_weight, total_antifly_weight, total_slits_weight]
        total_aluminums_weight = sum(total_aluminum_weights)

        # Calculate amounts of handles
        total_handles = ITEMS_PER_SLASH["handle"] * num_slashes
        # Calculate corner joints
        mainframe_cornerjoints = ITEMS_PER_MAINFRAME["cornerjoint"] * num_mainframes
        s_cornerjoints = ITEMS_PER_SLASH["cornerjoint"] * num_slashes
        total_cornerjoints = mainframe_cornerjoints + s_cornerjoints
        # Calculate total wheels
        total_wheels = ITEMS_PER_SLASH["wheel"] * num_slashes

        # Calculate prices
        total_aluminums_price = calculate_price(PRICES["Aluminum kg"], total_aluminums_weight)
        total_handles_price = calculate_price(PRICES["Handle"], total_handles)
        total_cornerjoints_price = calculate_price(PRICES["Corner Joint"], total_cornerjoints)
        total_wheels_price = calculate_price(PRICES["Wheel"], total_wheels)
        # Calculate worker fee per area
        workerfee = calculate_workerfee(window_w, window_h)

        # TODO: Compare total cost with manual calculation
        prices_to_sum = [total_aluminums_price , total_handles_price, total_cornerjoints_price, total_wheels_price, workerfee]
        total_cost = sum(prices_to_sum)

        total_aluminum_kg = round(total_mainframes_weight + total_slashes_weight + total_antifly_weight + total_slits_weight, 3)

        # Assign amounts with prices
        debug = [{"Window:": f"width = {window_w} height = {window_h}"},
                {"Total Aluminums Weight": f"{total_aluminums_weight} kg", "Price": f"$ {total_aluminums_price}"},
                {"Total Handles": total_handles, "Price": f"$ {total_handles_price}"},
                {"Total Wheels": total_wheels, "Price": f"$ {total_wheels_price}"},
                {"Total Corner Joints:": total_cornerjoints, "Price": f"$ {total_cornerjoints_price}"},              
                {"Total Worker Fee": f"$ {workerfee}"},
                {"Total Cost": f"$ {total_cost}"},
                {"Total Aluminum Kg" : f"{total_aluminum_kg} kg"}
                ]
        
        output = [{"Total Cost": f"$ {total_cost:.2f}"},
                {"Total Aluminum Kg" : f"{total_aluminum_kg} kg"}
                ]
                
        
        for dict in output:
            for key, value in dict.items():
                print(key, value, end=' | ')
            print("")
        print("\n")


def convert_length_to_weight(tube, length):
    std_length = STD_ALUMINUM_TUBE_MEASUREMENTS[tube]["length"]
    std_weight = STD_ALUMINUM_TUBE_MEASUREMENTS[tube]["weight"]
    weight = (std_weight * length) / std_length

    return weight


def calculate_workerfee(w, h):
    area = w * h
    area_meters = area / M2_TO_M_CONVERSION_FACTOR
    workerfee = round(area_meters * WORKERFEE_PER_METER_SQUARED, 2)

    return workerfee


def calculate_price(price, quantity):
    total_price = round(price * quantity, 2)

    return total_price


if __name__ == "__main__":
    main()