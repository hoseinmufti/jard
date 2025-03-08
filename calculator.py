from tubes import STD_ALUMINUM_TUBE_INFO

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

def calculate_tube_count(total_tube_length, tube):
    std_tube_length = STD_ALUMINUM_TUBE_INFO[tube]["measurements"]["length"]
    return total_tube_length / std_tube_length

def calculate_workerfee(w, h, fee_per_m2, conversion_factor):
    area = (w * h) / conversion_factor
    return fee_per_m2 * area
