def oxford_comma(elements):
    if len(elements) == 0:
        return ""
    elif len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        # Join all elements with commas, except for the last one, which is preceded by "and"
        comma_separated = ", ".join(elements[:-1])
        return f"{comma_separated}, and {elements[-1]}"
