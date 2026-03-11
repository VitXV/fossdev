def calculate_ndfl_tax(x):
    tiers = [
        (0.0, 0.0, 0.13),
        (2_400_000.0, 312_000.0, 0.15),
        (5_000_000.0, 702_000.0, 0.18),
    ]

    for start, additive, rate in tiers[::-1]:
        if x > start:
            return additive + (x - start) * rate
    return