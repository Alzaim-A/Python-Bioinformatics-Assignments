"""input_to_protocol.py"""


def main():
    """Get user inputs"""
    final_volume = float(input("Please enter the final volume of the solution (ml): "))

    # For NaCl
    nacl_stock = float(input("Please enter the NaCl stock (mM): "))
    nacl_final = float(input("Please enter the NaCl final (mM): "))
    nacl_volume = calculate_volume(nacl_stock, nacl_final, final_volume)

    # For MgCl2
    mgcl2_stock = float(input("Please enter the MgCl2 stock (mM): "))
    mgcl2_final = float(input("Please enter the MgCl2 final (mM): "))
    mgcl2_volume = calculate_volume(mgcl2_stock, mgcl2_final, final_volume)

    # Calculate water volume
    water_volume = final_volume - (nacl_volume + mgcl2_volume)

    # Print the results
    print(f"Add {nacl_volume:.3f} ml NaCl")
    print(f"Add {mgcl2_volume:.3f} ml MgCl2")
    print(f"Add water to a final volume of {water_volume:.1f} ml and mix")


def calculate_volume(stock_concentration, final_concentration, final_volume):
    """
    Calculate the volume of stock solution needed to achieve the final concentration
    in the given final volume.
    """
    return (final_concentration * final_volume) / stock_concentration


if __name__ == "__main__":
    main()
