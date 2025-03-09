# English to Kurdish translation mapping
KURDISH_NAMES = {
    "Slide 2 Curved": "بوري جرجوب",
    "Slide Z tube": "بوری زیت",
    "Antifly tube": "بوری مانعزواب",
    "Slide Slit tube": "بوری چەقوو",
    "cornerjoint": "زاویە",
    "sliding sash handle": "یەدە",
    "sliding sash wheel": "تایە",
    "Structs total cost": "نرخی گشتی"
}

def format_output(data, indent=0):
    output_lines = []
    spaces = "    " * indent
    
    for item in data:
        for key, value in item.items():
            output_lines.append(f"{spaces}{key}:")
            if isinstance(value, dict):
                for k, v in value.items():
                    if "tubes counts" in key:  # Check if we're handling tubes
                        output_lines.append(f"{spaces}    {k}: {round(v, 1)}")
                    elif isinstance(v, float):
                        output_lines.append(f"{spaces}    {k}: {round(v, 2)}")
                    else:
                        output_lines.append(f"{spaces}    {k}: {v}")
            else:
                output_lines.append(f"{spaces}    {value}")
        output_lines.append("")
    
    return "\n".join(output_lines)

def translate_accessories(accessories_counts):
    kurdish_accessories = {}
    for acc, count in accessories_counts.items():
        kurdish_name = KURDISH_NAMES.get(acc, acc)
        kurdish_accessories[kurdish_name] = count
    return {"پێداویستیەکان": kurdish_accessories}

def translate_tubes(tubes_counts):
    kurdish_tubes = {}
    for tube, count in tubes_counts.items():
        kurdish_name = KURDISH_NAMES.get(tube, tube)
        kurdish_tubes[kurdish_name] = count
    return {"بۆریەکان": kurdish_tubes}

def get_kurdish_output(structures_total_accessories_counts, structures_total_tubes_counts, 
                      structures_total_length, structures_total_cost):
    output_kurdish = []
    output_kurdish.append(translate_accessories(structures_total_accessories_counts))
    output_kurdish.append(translate_tubes(structures_total_tubes_counts))
    output_kurdish.append({"درێژی گشتی": round(structures_total_length, 2)})
    output_kurdish.append({KURDISH_NAMES["Structs total cost"]: round(structures_total_cost, 2)})
    return output_kurdish


def print_output(output):
    print("\nEnglish Output:")
    print("=" * 40)
    print(format_output(output))