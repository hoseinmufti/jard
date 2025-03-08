# Jard - Window Structure Calculator

A Python application for calculating materials, costs, and specifications for aluminum window structures. This tool was developed to solve real-world calculation challenges faced in an aluminum window manufacturing factory.

## Motivation

This project was born from a practical need at my father's aluminum window manufacturing factory. The manual calculation of materials, costs, and specifications for multiple window structures was time-consuming and error-prone. What used to take hours of manual calculations can now be done in seconds with high accuracy.

## How It Works

### Calculation Process

1. **Structure Input**
   - Each window structure is defined by its width (w) and height (h)
   - Structures follow predefined blueprints that specify their components

2. **Materials Calculation**
   - **Tubes**: Calculates required aluminum tube lengths based on dimensions
   - **Accessories**: Determines necessary components (screws, handles, etc.)
   - **Weight**: Computes total aluminum weight for cost calculations

3. **Cost Components**
   - Material costs (aluminum tubes and accessories)
   - Labor costs (calculated per square meter)
   - Total cost aggregation

### Technical Implementation

The calculator uses:
- Predefined structural blueprints for different window types
- Standard aluminum tube specifications
- Current market prices for materials
- Worker fees per square meter

Output is provided in both English and Kurdish to serve the local market needs.

## Usage

```python
jard = Jard()
structures = [
    {"w": 100, "h": 150, "strbluprnt": "2_PIECE_SLIDE"},
    {"w": 200, "h": 180, "strbluprnt": "3_PIECE_SLIDE"}
]
jard.slide_window(structures)
```

## Project Structure

- `jard.py`: Main calculation orchestrator
- `calculator.py`: Core calculation functions
- `structural_blueprints.py`: Window structure definitions
- `prices.py`: Material and labor costs
- `utils.py`: Output formatting and language support
