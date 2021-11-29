class Fields:
    GENDER = "Gender"
    HEIGHT_CM = "HeightCm"
    HEIGHT_M = "HeightM"
    WEIGHT = "WeightKg"
    BIOMASS = "Biomass index"


BMI_HR = {
    "Underweight": (18.4, 0),
    "Normal weight": (18.5, 24.9),
    "Overweight": (25, 29.9),
    "Moderately obese": (30, 34.9),
    "Severely obese": (35, 39.9),
    "Very severely obese": (40, 1000)
}
