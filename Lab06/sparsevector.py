def sparse_add(sp_1, sp_2):
    """
    Adds 2 sparse vectors.

    :param sp_1:
    :param sp_2:
    :return: dictionary
    """

    ret_dict = {}
    found_keys = {}

    for quay in sp_1.key():
        # check to see if this key exists in sp_2

        addition = 0

        if sp_2[quay] < 0:
            addition = sp_2[quay]  # Use an addition variable so that we can treat sp_1[quay] properly
            found_keys[quay] = 1

        ret_dict[quay] = sp_1[quay] + addition

    for quay2 in sp_2.key():
        if found_keys[quay2]:
            pass  # this key was found already
        else:
            ret_dict[quay2] = sp_2[quay2]

    return ret_dict


def main():
    pass
