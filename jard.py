from structural_blueprints import STRUCTURAL_BLUEPRINTS
from tubes import STD_ALUMINUM_TUBE_INFO
from prices import PRICES
from utils import format_output, get_kurdish_output, print_output
from calculator import (calculate_tube_length, calculate_aluminum_weight,
                      calculate_tube_count, calculate_workerfee)

WORKERFEE_PER_METER_SQUARED = 5
CM2_TO_M2_CONVERSION_FACTOR = 10000

class Jard:
    def slide_window(self, structures):
        structures_total_accessories_counts = {}
        structures_total_tubes_counts = {}
        structures_total_cost = 0
        structures_total_length = 0

        for structure in structures:
            # Unpack structure dimensions
            w = structure["w"]
            h = structure["h"]
            structural_blueprint = STRUCTURAL_BLUEPRINTS[structure["strbluprnt"]]

            for part, info in structural_blueprint.items():
                part_count = info["count"]
                
                # Calculate accessories
                for accessory, accessory_count in info["accessories counts"].items():
                    total_accessory_count = accessory_count * part_count
                    structures_total_accessories_counts[accessory] = structures_total_accessories_counts.get(accessory, 0) + total_accessory_count
                    
                    accessory_cost = PRICES[accessory]["price"]
                    structures_total_cost += accessory_cost * total_accessory_count

                # Calculate tubes
                tube = info["tube"]
                total_tube_length = calculate_tube_length(w, h, info["dimension counts"], 
                                                        info["dimension ratios"], 
                                                        info["count"])
                
                structures_total_length += total_tube_length
                tube_count = calculate_tube_count(total_tube_length, tube)
                structures_total_tubes_counts[tube] = structures_total_tubes_counts.get(tube, 0) + tube_count

                # Calculate aluminum cost
                structure_total_weight = calculate_aluminum_weight(total_tube_length, tube)
                aluminum_kg_cost = PRICES["aluminum kg"]
                structures_total_cost += aluminum_kg_cost * structure_total_weight

            # Add workerfee
            structures_total_cost += calculate_workerfee(w, h, WORKERFEE_PER_METER_SQUARED, 
                                                       CM2_TO_M2_CONVERSION_FACTOR)

        # Prepare outputs
        output_en = [
            {"Structs total accessories counts": structures_total_accessories_counts},
            {"Structs total tubes counts": structures_total_tubes_counts},
            {"Structs total length": round(structures_total_length, 2)},
            {"Structs total cost": round(structures_total_cost, 2)}
        ]

        output_kr = get_kurdish_output(structures_total_accessories_counts,
                                     structures_total_tubes_counts,
                                     structures_total_length,
                                     structures_total_cost)
        
        print_output(output_en)