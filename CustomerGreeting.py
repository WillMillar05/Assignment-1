def format_greeting(name, title="Customer"):
    clean_name = name.strip()

    if clean_name == "":
        return "Hello, Valued Customer!"

    clean_name = clean_name.title()
    first_name = clean_name.split()[0]
    return f"Hello, {first_name} ({title})!"


# Main
full_name = input("Please enter your full name: ")
greeting = format_greeting(full_name)
print(greeting)
