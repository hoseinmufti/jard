from structural_blueprints import STRUCTURAL_BLUEPRINTS
from tubes import STD_ALUMINUM_TUBE_INFO
from prices import PRICES
from utils import format_output, get_kurdish_output, print_output

WORKERFEE_PER_METER_SQUARED = 5
CM2_TO_M2_CONVERSION_FACTOR = 10000


class Jard:
    def slide_window(self, structures):
        def calculate_tube_length(w, h, dimension_counts, dimension_ratios, part_count):
            w_count = dimension_counts["w"]
            h_count = dimension_counts["h"]
            w_ratio = dimension_ratios["w"]
            h_ratio = dimension_ratios["h"]

            scaled_w = w * w_ratio
            scaled_h = h * h_ratio

            total_w_length = (scaled_w) * w_count
            total_h_length = (scaled_h) * h_count
            part_length = total_w_length + total_h_length

            total_part_length = part_length * part_count
            return total_part_length
        

        def calculate_aluminum_weight(part_length, tube):
            tube_std_measurements = STD_ALUMINUM_TUBE_INFO[tube]["measurements"]
            std_length = tube_std_measurements["length"]
            std_weight = tube_std_measurements["weight"]
            weight = (std_weight * part_length) / std_length
            
            return weight


        structures_total_accessories_counts = {}
        structures_total_tubes_counts = {}
        structures_total_cost = 0
        structures_total_length = 0

        for structure in structures:
            structure_total_accessories_counts = {}
            structure_total_tubes_counts = {}
            structure_total_cost = 0
            structure_total_length = 0

            structural_blueprint_code = structure["strbluprnt"]
            structural_blueprint = STRUCTURAL_BLUEPRINTS[structural_blueprint_code]
            # Assign structure width and height
            w = structure["w"]
            h = structure["h"]

            for part, info in structural_blueprint.items():
                part_count = info["count"]
                # Add accessories to total structures' accessories counts dict
                for accessory, accessory_count in info["accessories counts"].items():
                    total_accessory_count = accessory_count * part_count
                    structure_total_accessories_counts[accessory] = structure_total_accessories_counts.get(accessory, 0) + total_accessory_count
                    structures_total_accessories_counts[accessory] = structures_total_accessories_counts.get(accessory, 0) + total_accessory_count

                    accessory_cost = PRICES[accessory]["price"]
                    total_accessory_cost = accessory_cost * total_accessory_count

                    structure_total_cost += total_accessory_cost
                    structures_total_cost += total_accessory_cost
                    # debug_accessories_cost += total_accessory_cost

                # Add total part tubes onto structures' total tubes counts dict
                tube = info["tube"]
                total_tube_length = calculate_tube_length(w, h, info["dimension counts"], 
                                                        info["dimension ratios"], 
                                                        info["count"])
                
                structure_total_length += total_tube_length
                structures_total_length += total_tube_length

                std_tube_length = STD_ALUMINUM_TUBE_INFO[tube]["measurements"]["length"]
                tube_count = total_tube_length / std_tube_length

                structure_total_tubes_counts[tube] = structure_total_tubes_counts.get(tube, 0) + tube_count
                structures_total_tubes_counts[tube] = structures_total_tubes_counts.get(tube, 0) + tube_count

                # Add aluminum cost
                structure_total_weight = calculate_aluminum_weight(total_tube_length, tube)
                aluminum_kg_cost = PRICES["aluminum kg"]
                aluminum_kg_total_cost = aluminum_kg_cost * structure_total_weight

                structure_total_cost += aluminum_kg_total_cost
                structures_total_cost += aluminum_kg_total_cost
                # debug_aluminum_cost += aluminum_kg_total_cost


            # Calculate structure area
            area = (w * h) / CM2_TO_M2_CONVERSION_FACTOR

            workerfee = WORKERFEE_PER_METER_SQUARED * area

            structure_total_cost += workerfee
            structures_total_cost += workerfee
            # debug_workerfee += workerfee

            # debug_costs = {"Total Aluminum cost": debug_aluminum_cost, 
            #                 "Total Accessories cost": debug_accessories_cost,
            #                 "Total Workerfee cost": debug_workerfee}

        output_en = [{"Structs total accessories counts": structures_total_accessories_counts},
                  {"Structs total tubes counts": structures_total_tubes_counts},
                  {"Structs total length": round(structures_total_length, 2)},
                  {"Structs total cost": round(structures_total_cost, 2)}]

        output_kr = get_kurdish_output(structures_total_accessories_counts,
                                          structures_total_tubes_counts,
                                          structures_total_length,
                                          structures_total_cost)
        
        print_output(output_en)
        

    def casement_window(self, structures):
        ...