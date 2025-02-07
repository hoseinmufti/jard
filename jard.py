WORKERFEE_PER_METER_SQUARED = 5
CM2_TO_M2_CONVERSION_FACTOR = 10000

STD_ALUMINUM_TUBE_MEASUREMENTS = {
    "frame": {"length": 600, "weight": 8.4},
    "slash": {"length": 600, "weight": 5.5},
    "antifly": {"length": 600, "weight": 3.5},
    "slit": {"length": 600, "weight": 2.0}
}

PRICES = {"Aluminum kg": 3.8, "Handle":1.85, "Corner Joint": 0.32, "Wheel": 1.75}

ACCESSORIES_PER_FRAME = {"cornerjoint": 8}
ACCESSORIES_PER_SLASH = {"cornerjoint": 4, "wheel": 2, "handle": 1}


class Jard():
    def slide_window(self, windows):
        total_windows_cost_sum = 0

        for i, window in enumerate(windows):
            # Assign number of frames for frame and slashashes
            frames_count = 1
            slashes_count = 2

            w_count_per_frame = 2
            h_count_per_frame = 2

            w_count_per_slash = 2
            h_count_per_slash = 2

            # Assign window width and height
            window_w = window["w"]
            window_h = window["h"]
            slash_w = window_w / w_count_per_slash

            # Calculate window area
            window_area = (window_w * window_h) / CM2_TO_M2_CONVERSION_FACTOR

            # Calculate total frame length
            total_frame_w = window_w * w_count_per_frame
            total_frame_h = window_h * h_count_per_frame
            total_frame_length = total_frame_w + total_frame_h

            # Calculate total slash length
            total_slash_w = slash_w * w_count_per_slash
            total_slash_h = window_h * h_count_per_slash
            total_slash_length = total_slash_w + total_slash_h

            # Calculate total frames lengths
            total_frames_length = total_frame_length * frames_count
            total_slashes_length = total_slash_length * slashes_count


            # Calculate total frames weight
            total_frames_weight = self._convert_length_to_weight("frame", total_frames_length)
            # Calculate total slashes weight
            total_slashes_weight = self._convert_length_to_weight("slash", total_slashes_length)
            # Caluclate total antiflies weight
            total_antifly_weight = self._convert_length_to_weight("antifly", total_slash_length)
            # Calculate total slits weight
            total_slits_length = window_h * slashes_count
            total_slits_weight = self._convert_length_to_weight("slit", total_slits_length)

            # Calculate total aluminum tubes weight
            aluminum_weights = [total_frames_weight, total_slashes_weight, total_antifly_weight, total_slits_weight]
            total_aluminums_weight = sum(aluminum_weights)

            # Calculate amounts of handles
            total_handles = ACCESSORIES_PER_SLASH["handle"] * slashes_count
            # Calculate corner joints
            frame_cornerjoints = ACCESSORIES_PER_FRAME["cornerjoint"] * frames_count
            s_cornerjoints = ACCESSORIES_PER_SLASH["cornerjoint"] * slashes_count
            total_cornerjoints = frame_cornerjoints + s_cornerjoints
            # Calculate total wheels
            total_wheels = ACCESSORIES_PER_SLASH["wheel"] * slashes_count

            # Calculate prices
            total_aluminums_price = self._calculate_price(PRICES["Aluminum kg"], total_aluminums_weight)
            total_handles_price = self._calculate_price(PRICES["Handle"], total_handles)
            total_cornerjoints_price = self._calculate_price(PRICES["Corner Joint"], total_cornerjoints)
            total_wheels_price = self._calculate_price(PRICES["Wheel"], total_wheels)
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

            total_windows_cost_sum += total_cost

        print(f"total sum cost of windows: $ {round(total_windows_cost_sum, 2)}")


    def door(self, doors):
        frames_count = 1


        for door in doors:
            ...

    # Private functions
    def _convert_length_to_weight(self, tube_type, length):
        std_length = STD_ALUMINUM_TUBE_MEASUREMENTS[tube_type]["length"]
        std_weight = STD_ALUMINUM_TUBE_MEASUREMENTS[tube_type]["weight"]
        weight = (std_weight * length) / std_length

        return weight


    def _calculate_price(self, price, quantity):
        total_price = price * quantity

        return total_price