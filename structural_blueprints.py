from prices import PRICES
from tubes import STD_ALUMINUM_TUBE_MEASUREMENTS


def get_price(structure, part, accessory):
    price = PRICES[structure][part][accessory]

    return price


STRUCTURAL_BLUEPRINTS = {
    "slide window": {
        "frame": {
            "std_tube_measurements": STD_ALUMINUM_TUBE_MEASUREMENTS["slide window frame L"],
            "accessories": {
                "cornerjoint": {
                    "count": 8,
                    "price": get_price("slide window", "frame", "cornerjoint"),
                }
            },
            "dimension multipliers": {"w": 2, "h": 2},
            "dimension ratios": {"w": 1, "h": 1},
            "count": 1,
        },
        "sash": {
            "std_tube_measurements": STD_ALUMINUM_TUBE_MEASUREMENTS["slide sash Z"],
            "accessories": {
                "cornerjoint": {
                    "count": 4,
                    "price": get_price("slide window", "sash", "cornerjoint"),
                },
                "wheel": {
                    "count": 2,
                    "price": get_price("slide window", "sash", "wheel"),
                },
                "handle": {
                    "count": 1,
                    "price": get_price("slide window", "sash", "handle"),
                },
            },
            "dimension multipliers": (sash_dimensions_multipliers := {"w": 2, "h": 2}),
            "dimension ratios": (sash_dimension_ratios := {"w": 0.5, "h": 1}),
            "count": (sash_count := 2),
        },
        "antifly": {
            "std_tube_measurements": STD_ALUMINUM_TUBE_MEASUREMENTS["slide sash antifly"],
            "accessories": {},
            "dimension multipliers": sash_dimensions_multipliers,
            "dimension ratios": sash_dimension_ratios,
            "count": 1,
        },
        "slit": {
            "std_tube_measurements": STD_ALUMINUM_TUBE_MEASUREMENTS["slide sash slit"],
            "accessories": {},
            "dimension multipliers": {"w": 0, "h": 1},
            "dimension ratios": {"w": 0, "h": sash_dimension_ratios["h"]},
            "count": sash_count,
        }
    },
    # # TODO: Check values with real values
    # "normal door": {
    #     "frame": {
    #         "cornerjoint": {
    #             "count": 8,
    #             "price": get_price("normal door", "frame", "cornerjoint"),
    #         }
    #     },
    #     "door": {
    #         "cornerjoint": {
    #             "amount": 4,
    #             "price": get_price("normal door", "door", "cornerjoint"),
    #         },
    #         "handle": {"count": 1, "price": get_price("normal door", "door", "handle")},
    #     },
    #     "bathroom vent": ...,
    # },
}