WORKERFEE_PER_METER_SQUARED = 5
CM2_TO_M2_CONVERSION_FACTOR = 10000

STD_ALUMINUM_TUBE_MEASUREMENTS = {
    "mainframe": {"length": 600, "weight": 8.4},
    "slash": {"length": 600, "weight": 5.5},
    "antifly": {"length": 600, "weight": 3.5},
    "slit": {"length": 600, "weight": 2.0}
}

ITEMS_PER_MAINFRAME = {"cornerjoint": 8}
ITEMS_PER_SLASH = {"cornerjoint": 4, "wheel": 2, "handle": 1}

PRICES = {"Aluminum kg": 3.8, "Handle":1.85, "Corner Joint": 0.32, "Wheel": 1.75}


windows = [
{"w": 200, "h": 250},
{"w": 200, "h": 125},
{"w": 200, "h": 250},
{"w": 200, "h": 275},
{"w": 150, "h": 125},
{"w": 150, "h": 150},
{"w": 180, "h": 250},
{"w": 200, "h": 250},
]

from datetime import datetime



def main():
    total_windows_cost = 0

    for i, window in enumerate(windows):
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

        # Calculate window area
        window_area = (window_w * window_h) / CM2_TO_M2_CONVERSION_FACTOR

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
        aluminum_weights = [total_mainframes_weight, total_slashes_weight, total_antifly_weight, total_slits_weight]
        total_aluminums_weight = sum(aluminum_weights)

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
        workerfee = window_area * WORKERFEE_PER_METER_SQUARED

        # Calculate total cost
        prices_to_sum = [total_aluminums_price , total_handles_price, total_cornerjoints_price, total_wheels_price, workerfee]
        total_cost = sum(prices_to_sum)

        # Calculate price per meter
        price_per_meter = total_cost / window_area

        # Assign amounts with prices
        debug = [{"Window:": f"width = {window_w} height = {window_h}"},
                {"Total Aluminums Weight": f"{total_aluminums_weight} kg", "Price": f"$ {total_aluminums_price}"},
                {"Total Handles": total_handles, "Price": f"$ {total_handles_price}"},
                {"Total Wheels": total_wheels, "Price": f"$ {total_wheels_price}"},
                {"Total Corner Joints:": total_cornerjoints, "Price": f"$ {total_cornerjoints_price}"},              
                {"Total Worker Fee": f"$ {workerfee}"},
                {"Total Cost": f"$ {total_cost}"},
                {"Total Aluminum Kg" : f"{total_aluminums_weight} kg"}
                ]
        
        output = [{"Window:": f"id: {i + 1} w: {window_w} h:{window_h}"},
                {"Total Aluminum Kg" : f"{total_aluminums_weight} kg"},
                {"Total Cost": f"$ {(total_cost):.2f}"},
                {"Price per meter": f"$ {price_per_meter:.2f}"}
                ]
                
        for dict in output:
            for key, value in dict.items():
                print(key, value)
        print("\n")

        total_windows_cost += total_cost

    print(f"total sum cost of windows: $ {round(total_windows_cost, 2)}")


def convert_length_to_weight(tube_type, length):
    std_length = STD_ALUMINUM_TUBE_MEASUREMENTS[tube_type]["length"]
    std_weight = STD_ALUMINUM_TUBE_MEASUREMENTS[tube_type]["weight"]
    weight = (std_weight * length) / std_length

    return weight


def calculate_price(price, quantity):
    total_price = price * quantity

    return total_price


if __name__ == "__main__":
    main()