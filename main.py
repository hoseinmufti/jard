import sys

WORKER_FEE_PER_METER_SQUARED = 5
M2_TO_M_CONVERSION_FACTOR = 10000

STD_ALUMINUM_TUBE_MEASUREMENTS = {
    "mainframe": {"length": 600, "weight": 8400},
    "slash": {"length": 600, "weight": 5500},
    "antifly": {"length": 600, "weight": 3500},
    "slit": {"length": 600, "weight": 2000}
}

ITEMS_PER_MAINFRAME = {"cornerjoint": 8}
ITEMS_PER_SLASH = {"cornerjoint": 4, "wheel": 2, "handle": 1}


PRICES = {"Aluminum kg": 3.8, "Handle":1.85, "Corner Joint": 0.32, "Wheel": 1.75}


windows = [{"w": 193, "h": 245}]

def main():
    for window in windows:
        # Assign number of frames for mainframe and slashashes
        num_mainframe = 1
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
        total_mainframes_length = total_mainframe_length * num_mainframe
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

        # Calculate amounts of handles
        total_handles = ITEMS_PER_SLASH["handle"] * num_slashes
        # Calculate corner joints
        mainframe_cornerjoints = ITEMS_PER_MAINFRAME["cornerjoint"] * num_mainframe
        s_cornerjoints = ITEMS_PER_SLASH["cornerjoint"] * num_slashes
        total_cornerjoints = mainframe_cornerjoints + s_cornerjoints
        # Calculate total wheels
        total_wheels = ITEMS_PER_SLASH["wheel"] * num_slashes

        # Calculate worker fee per area
        area = window_w * window_h
        area_meters = area / M2_TO_M_CONVERSION_FACTOR
        total_worker_fee = area_meters * WORKER_FEE_PER_METER_SQUARED

        # Calculate prices
        total_mainframe_price = total_mainframes_weight * PRICES["Aluminum kg"]
        total_s_price = total_slashes_weight * PRICES['Aluminum kg']
        total_handles_price = total_handles * PRICES["Handle"]
        total_cornerjoints_price = total_cornerjoints * PRICES["Corner Joint"]
        total_antifly_price = total_antifly_weight * PRICES["Aluminum kg"]
        total_slit_price = total_slits_weight * PRICES["Aluminum kg"]
        total_wheels_price = total_wheels * PRICES["Wheel"]

        # TODO: Compare total cost with manual calculation
        total_cost = total_mainframe_price + total_s_price + total_antifly_price + total_slit_price + total_cornerjoints_price + total_handles_price +total_wheels_price

        total_aluminum_kg = total_mainframes_weight + total_slashes_weight + total_antifly_weight + total_slits_weight

        # Assign amounts with prices
        debug = [{"Window:": f"width = {window_w} height = {window_h}"},
                {"Total MainFrame Weight": f"{total_mainframes_weight} kg", "Price": f"$ {total_mainframe_price:.2f}"},
                {"Total slashashes Weight": f"{total_slashes_weight} kg", "Price": f"$ {total_s_price:.2f}"},
                {"Total Antifly Weight": f"{total_antifly_weight} kg", "Price": f"$ {total_antifly_price:.2f}"},
                {"Total slit Weight": f"{total_slits_weight} kg", "Price": f"$ {total_slit_price:.2f}"},
                {"Total Handles": total_handles, "Price": f"$ {total_handles_price:.2f}"},
                {"Total Wheels": total_wheels, "Price": f"$ {total_wheels_price:.2f}"},
                {"Total Corner Joints:": total_cornerjoints, "Price": f"$ {total_cornerjoints_price:.2f}"},              
                {"Total Worker Fee": f"$ {total_worker_fee}"},
                {"Total Cost": f"$ {total_cost:.2f}"},
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
    weight = (std_weight * length) / std_length / 1000

    return weight


if __name__ == "__main__":
    main()