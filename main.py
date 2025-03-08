### Program to survey a list of frames (windows, doors) to calculate total cost and items required

from jard import Jard

def main():
    slide_windows = [
        { "strbluprnt": "slide window 2 curve", "w": 145.4, "h": 270.9},
        { "strbluprnt": "slide window 2 curve", "w": 186, "h": 205},
        { "strbluprnt": "slide window 2 curve", "w": 139, "h": 235},
        { "strbluprnt": "slide window 2 curve", "w": 200, "h": 244},
        { "strbluprnt": "slide window 2 curve", "w": 211.2, "h": 270.9},
        { "strbluprnt": "slide window 2 curve", "w": 149.3, "h": 229},
        { "strbluprnt": "slide window 2 curve", "w": 200, "h": 252},
        { "strbluprnt": "slide window 2 curve", "w": 200, "h": 252},
        { "strbluprnt": "slide window 2 curve", "w": 200, "h": 252},
        { "strbluprnt": "slide window 2 curve", "w": 186.4, "h": 230},
        { "strbluprnt": "slide window 2 curve", "w": 114, "h": 170},
        { "strbluprnt": "slide window 2 curve", "w": 240, "h": 128},
        { "strbluprnt": "slide window 2 curve", "w": 190, "h": 127},
        { "strbluprnt": "slide window 2 curve", "w": 134, "h": 80},









    ]
    
    # doors = [
    #     {"w": 120, "h": 200},
    # ]
    
    jard = Jard()
    jard.slide_window(slide_windows)



if __name__ == "__main__":
    main()