### Program to survey a list of frames (windows, doors) to calculate total cost and items required

from jard import Jard

def main():
    slide_windows = [
        {"w": 193, "h": 245},
        # {"w": 200, "h": 125},
        # {"w": 200, "h": 250},
        # {"w": 200, "h": 275},
        # {"w": 150, "h": 125},
        # {"w": 150, "h": 150},
        # {"w": 180, "h": 250},
        # {"w": 200, "h": 250},
    ]
    
    # doors = [
    #     {"w": 120, "h": 200},
    # ]
    
    jard = Jard()
    jard.slide_window(slide_windows)



if __name__ == "__main__":
    main()