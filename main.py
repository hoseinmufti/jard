### Program to survey a list of frames (windows, doors) to calculate total cost and items required

from jard import Jard

def main():
    structures = [
        {"w": 193, "h": 245, "strbluprnt code": "slide window"},
        {"w": 200, "h": 125, "strbluprnt code": "slide window"},
        {"w": 200, "h": 250, "strbluprnt code": "slide window"},
        {"w": 200, "h": 275, "strbluprnt code": "slide window"},
        {"w": 150, "h": 125, "strbluprnt code": "slide window"},
        {"w": 150, "h": 150, "strbluprnt code": "slide window"},
        {"w": 180, "h": 250, "strbluprnt code": "slide window"},
        {"w": 200, "h": 250, "strbluprnt code": "slide window"},
    ]
    
    # doors = [
    #     {"w": 120, "h": 200},
    # ]
    
    jard = Jard()
    jard.slide_window(structures)



if __name__ == "__main__":
    main()