from collections import OrderedDict


def handle_duplicate_values(timeseries, validation=None):
    """
    Remove Duplicate time values in the timeseries
    TODO: Currently handle by taking last occurrence. Need to introduce better alternative.
    :param validation:
    :param timeseries:
    :return: list of [time, value]
    """
    if validation is None:
        validation = {'max_value': 1000, 'min_value': 0}

    MAX_VALUE = float(validation.get('max_value'))
    MIN_VALUE = float(validation.get('min_value'))

    ordered_dict = OrderedDict()
    for time, value in timeseries:
        if ordered_dict.get(time, None) is not None:
            print('duplicate', time, value, validation)
            ordered_dict[time] = value if MIN_VALUE <= value <= MAX_VALUE else ordered_dict.get(time)
        else:
            ordered_dict[time] = value

    # new_timeseries = []
    # for index, step in enumerate(timeseries):
    #     sub_series = timeseries[index+1:min(index+3, len(timeseries))]
    #     if step in sub_series:
    #         duplicate_index = timeseries[index+1:min(index+3, len(timeseries))].index(step)
    #         print('Duplicate:', step, duplicate_index)
    #     else:
    #         new_timeseries.append(step)

    return [list(x) for x in ordered_dict.items()]