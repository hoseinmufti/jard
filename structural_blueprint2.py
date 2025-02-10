STRUCTURAL_BLUEPRINTS = {
    "slide window": {
        "parts": {
            "frame": {
                "info": {
                    "tube": "at-0A",
                    "accessories counts": {
                        "ac-0A": 8,
                    },
                    "dimension counts": {"w": 2, "h": 2},
                    "dimension ratios": {"w": 1, "h": 1},
                    "count": 1,
                },
                "parts": {
                    "sash": {
                        "info": {
                            "tube": "at-0B",
                            "accessories counts": {"ac-0B": 4, "ac-0C": 1, "ac-0D": 2},
                            "dimension counts": (
                                sash_dimensions_multipliers := {"w": 2, "h": 2}
                            ),
                            "dimension ratios": (
                                sash_dimension_ratios := {"w": 0.5, "h": 1}
                            ),
                            "count": (sash_count := 2),
                        },
                        "parts": {
                            "antifly": {
                                "info": {
                                    "tube": "at-0C",
                                    "accessories counts": {},
                                    "dimension counts": sash_dimensions_multipliers,
                                    "dimension ratios": sash_dimension_ratios,
                                    "count": 1,
                                },
                                "parts": {},
                            },
                            "slit": {
                                "info": {
                                    "tube": "at-0D",
                                    "accessories counts": {},
                                    "dimension counts": {"w": 0, "h": 1},
                                    "dimension ratios": {
                                        "w": 0,
                                        "h": sash_dimension_ratios["h"],
                                    },
                                    "count": sash_count,
                                },
                                "parts": {},
                            },
                        },
                    },
                },
            },
        }
    }
}
