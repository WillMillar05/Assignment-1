#Prompt the user for a product name and match it to a category
Product = (input("What's the product name? ").strip().lower())

# Find category using match-case 
match Product:
    case p if p.startswith("tech") or p in ("electronics", "gadget"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Unknown Category - Further Review Needed"

    # output result
print(f"Product: {Product} | Category: {category}")