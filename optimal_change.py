# Constant variables - Only used for the sake of readability -
PREFIX_OUTPUT = 'The optimal change for an item that costs'
AMOUNT_GIVEN_OUTPUT = 'with an amount paid of'

def optimal_change(item_cost , amount_paid):
    """This is a solution to obtaining, and determining the optimal change for any given
    amount

    Args:
        item_cost (float): This is our cost of the item.
        amount_paid (float): This is the 'currency' or 'money' given to pay for the amount, which is higher than the cost of the item.

    Returns:
        boolean: true or false if the output string is equal to the test case output.
    """

    # We need to first find out how much change is due, so math
    # round to fix any of these (0.01999999999999999999999994 would turn into 0.02)
    change_due = round(amount_paid - item_cost, 2)

    # We built a 'map' that we will traverse to obtain the optimal change
    # Take note some of the small text short cuts that were taken
    currency_map = {
        '$100 bill': 100,
        '$50 bill': 50,
        '$20 bill': 20,
        '$10 bill': 10,
        '$5 bill': 5,
        '$1 bill': 1,
        'quarter': 0.25,
        'dime': 0.1,
        'nickle': 0.05,
        'penny': 0.01,
    }

    # This is our output string that we initialize with what information we know already
    output = f"{PREFIX_OUTPUT} ${item_cost} {AMOUNT_GIVEN_OUTPUT} ${amount_paid} is "

    # We now traverse the map starting at the top going down
    for currency in currency_map:
        # Initialize a variable that we use to track the amount of the same currency is required
        amount_of_repeated_currency = 0

        while change_due >= currency_map[currency]:
            amount_of_repeated_currency += 1
            change_due -= currency_map[currency]
            # We need to round to accurately do math
            change_due = round(change_due, 2)

        # We initialize 2 string variables to assist us in displaying a verbose string
        plural = ""
        display_currency = ""
        if amount_of_repeated_currency > 0:
            # We set our display now - this is used as a special case catch
            display_currency = currency
            # If we have multiples of the same currency used - let's fix our plural string accordingly
            if amount_of_repeated_currency > 1:
                # Here's yet another special case catch - 
                # Penny is the only word that requires additional changes than a simple "s"
                if (currency == "penny"):
                    # We already utilize our plural variable, so don't use it when fixing penny
                    display_currency = "pennie"
                plural = "s"
            # Apply our formatted string to the current output
            output += f"{amount_of_repeated_currency} {display_currency}{plural}, "

    # This is a neat 'trick' - we start from the end of the string and find the first occurrence and replace it
    # Example of what's happening: replace the first occurrence of ", " with "."
    output = ".".join(output.rsplit(", ", 1))
    # We do it again, because we want to put and for our very last currency in the output string
    # Example of what's happening: replace the first occurrence of ", " with ", and "
    output = ", and ".join(output.rsplit(", ", 1))

    # For debugging the final output string
    # print(output)
    return output