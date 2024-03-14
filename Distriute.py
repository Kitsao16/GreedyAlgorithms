def distribute_aid(supplies, affected_areas):
    # Sort affected areas based on urgency (e.g., number of people affected)
    sorted_areas = sorted(affected_areas, key=lambda x: x['urgency'], reverse=True)

    # Initialize distribution plan
    distribution_plan = {}

    # Iterate through affected areas
    for area in sorted_areas:
        # Determine the most urgently needed supply based on available supplies
        needed_supply = max(area['needs'], key=lambda x: supplies.get(x, 0))

        # Distribute the supply to the affected area
        if needed_supply not in distribution_plan:
            distribution_plan[needed_supply] = []
        distribution_plan[needed_supply].append(area['name'])

        # Update available supplies
        supplies[needed_supply] -= 1

    return distribution_plan

# Example usage:
supplies_available = {'food': 100, 'water': 50, 'medical': 20}
affected_areas = [
    {'name': 'Area A', 'urgency': 100, 'needs': ['food', 'water']},
    {'name': 'Area B', 'urgency': 80, 'needs': ['medical', 'water']},
    {'name': 'Area C', 'urgency': 50, 'needs': ['food']}
]

distribution_plan = distribute_aid(supplies_available, affected_areas)
print("Distribution Plan:")
for supply, areas in distribution_plan.items():
    print(f"Supply: {supply}, Areas: {', '.join(areas)}")

