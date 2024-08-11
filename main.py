from Super import Super

if __name__ == "__main__":
    try:
        supermarket_system = Super()
        supermarket_system.run()
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the required files are present.")
    except ValueError as e:
        print(f"Input error: {e}. Please enter valid data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
