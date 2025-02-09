from structural_blueprints import STRUCTURAL_BLUEPRINTS
from prices import PRICES
from check import check

WORKERFEE_PER_METER_SQUARED = 5
CM2_TO_M2_CONVERSION_FACTOR = 10000


class Jard:
    def slide_window(self, windows):
        def calculate_total_part_length(w, h, structural_blueprint):
            parts_multiplied_total_length = {}
            parts_combined_total_length = 0
            
            for part in structural_blueprint:
                dimension_multipliers = structural_blueprint[part]["dimension multipliers"]
                dimension_ratios = structural_blueprint[part]["dimension ratios"]

                w_count = dimension_multipliers["w"]
                h_count = dimension_multipliers["h"]
                w_ratio = dimension_ratios["w"]
                h_ratio = dimension_ratios["h"]
                part_count = structural_blueprint[part]["count"]

                total_w_length = (w * w_ratio) * w_count
                total_h_length = (h * h_ratio) * h_count
                part_total_length = total_w_length + total_h_length

                part_multiplied_total_length = part_total_length * part_count

                parts_multiplied_total_length[part] = part_multiplied_total_length
                parts_combined_total_length += part_multiplied_total_length
            
            return parts_multiplied_total_length, parts_combined_total_length
        

        def calculate_total_aluminums_weights(structural_blueprint, parts_length):
            parts_weights = {}
            combined_weight = 0
            for part in structural_blueprint:
                std_length = structural_blueprint[part]["std_tube_measurements"]["length"]
                std_weight = structural_blueprint[part]["std_tube_measurements"]["weight"]
                weight = (std_weight * parts_length[part]) / std_length

                parts_weights[part] = weight
                combined_weight += weight

            return parts_weights, combined_weight


        def count_total_accesories(structural_blueprint):
            total_part_accessories_details = {}
            combined__total_accessories_details = {}

            for part in structural_blueprint:
                accessories_details = structural_blueprint[part]["accessories"]

                if accessories_details:
                    part_count = structural_blueprint[part]["count"]

                    for accessory in accessories_details:
                        accessory_count = accessories_details[accessory]["count"]
                        accessory_price = accessories_details[accessory]["price"]

                        accessory_total_count = accessory_count * part_count
                        accessory_total_price = accessory_total_count * accessory_price

                        # Add accessory details to total_part_accessories_details
                        if part in total_part_accessories_details:
                            total_part_accessories_details[part][accessory] = {
                                "total count": accessory_total_count,
                                "total price": accessory_total_price,
                            }
                        else:
                            total_part_accessories_details[part] = {
                                accessory:{
                                    "total count": accessory_total_count,
                                    "total price": accessory_total_price,
                                }
                            }

                        if accessory in combined__total_accessories_details:
                            combined__total_accessories_details[accessory]["total count"] += accessory_total_count
                            combined__total_accessories_details[accessory]["total price"] += accessory_total_price
                        else:
                            combined__total_accessories_details[accessory] = {
                            "total count": accessory_total_count,
                            "total price": accessory_total_price,
                            }

            return combined__total_accessories_details, total_part_accessories_details


        slidewindow_str_blu = STRUCTURAL_BLUEPRINTS["slide window"]

        total_windows_cost_sum = 0

        for i, window in enumerate(windows):
            # Assign window width and height
            window_w = window["w"]
            window_h = window["h"]
            # Calculate window area
            window_area = (window_w * window_h) / CM2_TO_M2_CONVERSION_FACTOR

            # Calculate total parts lengths
            parts_multiplied_total_length, parts_combined_length = calculate_total_part_length(window_w, window_h, slidewindow_str_blu)
            # Calculate alumnium weight
            parts_aluminum_weights, combined_aluminum_weight = calculate_total_aluminums_weights(slidewindow_str_blu, parts_multiplied_total_length)
            # Calculate total accessories
            combined_total_accessories_details, total_part_accessories_details = count_total_accesories(slidewindow_str_blu)
            # Calculate total accessories price
            total_accessories_cost = 0
            for accessory in combined_total_accessories_details:
                total_accessories_cost += combined_total_accessories_details[accessory]["total price"]

            # Calculate prices
            total_aluminums_price = self._calculate_price(PRICES["aluminum kg"], combined_aluminum_weight)
            workerfee = window_area * WORKERFEE_PER_METER_SQUARED

            # Calculate total cost
            prices_to_sum = [
                total_aluminums_price,
                total_accessories_cost,
                workerfee,
            ]
            total_cost = sum(prices_to_sum)

            # Calculate price per meter
            price_per_meter = total_cost / window_area

            # Assign counts with prices
            debug = [
                {"Window:": f"width = {window_w} height = {window_h}"},
                {
                    "Total Aluminums Weight": f"{combined_aluminum_weight} kg",
                    "Price": f"$ {total_aluminums_price}",
                },
                total_part_accessories_details,
                {"Total Worker Fee": f"$ {workerfee}"},
                {"Total Cost": f"$ {total_cost}"},
                {"Total Aluminum Kg": f"{combined_aluminum_weight} kg"},
            ]

            output = [
                {"Window:": f"id: {i + 1} w: {window_w} h:{window_h}"},
                {"Total Aluminum Kg": f"{combined_aluminum_weight} kg"},
                {"Total Cost": f"$ {(total_cost):.2f}"},
                {"Price per meter": f"$ {price_per_meter:.2f}"},
            ]

            for dict in debug:
                for key, value in dict.items():
                    print(key, value)
            print("\n")

            total_windows_cost_sum += total_cost

        print(f"total sum cost of windows: $ {round(total_windows_cost_sum, 2)}")

    def door(self, doors):
        for door in doors:
            ...

    # Private functions
    def _calculate_price(self, price, quantity):
        total_price = price * quantity

        return total_price
