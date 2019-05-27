

# Method to compare two versions.
# Return 1 if v2 is smaller,
# -1 if v1 is smaller,,
# 0 if equal
def version_compare(v1, v2):
    # This will split both the versions by '.'
    arr1 = v1.split(".")
    arr2 = v2.split(".")

    # Initializer for the version arrays
    i = 0

    # We have taken into consideration that both the
    # versions will contains equal number of delimiters
    while i < len(arr1):

        # Version 2 is greater than version 1
        if int(arr2[i]) > int(arr1[i]):
            return -1

        # Version 1 is greater than version 2
        if int(arr1[i]) > int(arr2[i]):
            return 1

        # We can't conclude till now
        i += 1

    # Both the versions are equal
    return 0
