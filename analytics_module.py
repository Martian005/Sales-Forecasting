def calculate_average_sales(total_sales, records):

    return total_sales / records


def sales_category(average_sales):

    if average_sales >= 1000000:

        return "High Sales"

    elif average_sales >= 500000:

        return "Medium Sales"

    else:

        return "Low Sales"