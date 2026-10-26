resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    """Display all resources with their details."""
    print("\nAll Resources")
    print("-" * 55)
    print(f"{'ID':<6}{'Name':<15}{'Category':<15}{'Quantity':<8}")
    print("-" * 55)
    for r in resources:
        print(f"{r[0]:<6}{r[1]:<15}{r[2]:<15}{r[3]:<8}")


def search_by_category(resources, category):
    """Display all resources belonging to a given category."""
    print(f"\nResources in category '{category}'")
    print("-" * 55)
    found = False
    for r in resources:
        if r[2].lower() == category.lower():
            print(f"ID: {r[0]}, Name: {r[1]}, Category: {r[2]}, Quantity: {r[3]}")
            found = True
    if not found:
        print("No resources found in this category.")


def find_unavailable(resources):
    """Identify resources whose available quantity is zero."""
    print("\nUnavailable Resources (quantity = 0)")
    print("-" * 55)
    found = False
    for r in resources:
        if r[3] == 0:
            print(f"ID: {r[0]}, Name: {r[1]}, Category: {r[2]}")
            found = True
    if not found:
        print("All resources are available.")


# Main program
display_resources(resources)

cat = input("\nEnter a category to search: ")
search_by_category(resources, cat)

find_unavailable(resources)
