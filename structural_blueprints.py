STRUCTURAL_BLUEPRINTS = {
    "slide window": {
        "frame": {
            "tube": "Slide L tube",
            "accessories counts": {
                "cornerjoint": 8,
            },
            "dimension counts": {"w": 2, "h": 2},
            "dimension ratios": {"w": 1, "h": 1},
            "count": 1,
        },
        "sash": {
            "tube": "Slide Z tube",
            "accessories counts": {
                "cornerjoint": 4, 
                "sliding sash handle": 1, 
                "sliding sash wheel": 2
            },
            "dimension counts": (sash_dimensions_multipliers := {"w": 2, "h": 2}),
            "dimension ratios": (sash_dimension_ratios := {"w": 0.5, "h": 1}),
            "count": (sash_count := 2),
        },
        "antifly": {
            "tube": "Antifly tube",
            "accessories counts": {},
            "dimension counts": sash_dimensions_multipliers,
            "dimension ratios": sash_dimension_ratios,
            "count": 1,
        },
        "slit": {
            "tube": "Slide Slit tube",
            "accessories counts": {},
            "dimension counts": {"w": 0, "h": 1},
            "dimension ratios": {"w": 0, "h": sash_dimension_ratios["h"]},
            "count": sash_count,
        },
    },
    "normal window": {
        "frame": {
            "tube": "Slide L tube",
            "accessories counts": {
                "cornerjoint": 8,
            },
            "dimension counts": {"w": 2, "h": 2},
            "dimension ratios": {"w": 1, "h": 1},
            "count": 1,
        },
        "sash": {
            "tube": "Slide Z tube",
            "accessories counts": {
                "cornerjoint": 4, 
                "sliding sash handle": 1, 
                "sliding sash wheel": 2
            },
            "dimension counts": (sash_dimensions_multipliers := {"w": 2, "h": 2}),
            "dimension ratios": (sash_dimension_ratios := {"w": 0.5, "h": 1}),
            "count": (sash_count := 2),
        },
    },
    "slide window 2 curve": {
        "frame": {
            "tube": "Slide 2 Curved",
            "accessories counts": {
                "cornerjoint": 8,
            },
            "dimension counts": {"w": 2, "h": 2},
            "dimension ratios": {"w": 1, "h": 1},
            "count": 1,
        },
        "sash": {
            "tube": "Slide Z tube",
            "accessories counts": {
                "cornerjoint": 4, 
                "sliding sash handle": 1, 
                "sliding sash wheel": 2
            },
            "dimension counts": (sash_dimensions_multipliers := {"w": 2, "h": 2}),
            "dimension ratios": (sash_dimension_ratios := {"w": 0.5, "h": 1}),
            "count": (sash_count := 2),
        },
        "antifly": {
            "tube": "Antifly tube",
            "accessories counts": {},
            "dimension counts": sash_dimensions_multipliers,
            "dimension ratios": sash_dimension_ratios,
            "count": 1,
        },
        "slit": {
            "tube": "Slide Slit tube",
            "accessories counts": {},
            "dimension counts": {"w": 0, "h": 1},
            "dimension ratios": {"w": 0, "h": sash_dimension_ratios["h"]},
            "count": sash_count,
        },
    },
}
