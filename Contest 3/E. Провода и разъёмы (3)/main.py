from collections import defaultdict


def sort(dictionary: dict) -> dict:
    sorted_values = sorted(dictionary.values())
    sorted_dictionary = {}

    for value in sorted_values:
        for key in dictionary.keys():
            if dictionary[key] == value and key not in sorted_dictionary.keys():
                sorted_dictionary[key] = dictionary[key]
                break
    return sorted_dictionary


def output(dictionary: dict, count: int) -> None:
    values = tuple(dictionary.values())
    values = values[-1: -count - 1: -1][::-1]
    for value in values:
        print(value)


number_of_connectors = int(input())
number_of_output_wires = int(input())
number_of_wire_occurrences = defaultdict(int)

for index in range(number_of_connectors):
    wires = {int(wire) for wire in input().split()}
    for wire in wires:
        number_of_wire_occurrences[wire] += 1

rejected_wires = {int(wire) for wire in input().split()}

number_of_wire_occurrences = dict(item for item in number_of_wire_occurrences.items() if item[0] not in rejected_wires)
number_of_wire_occurrences = sort(number_of_wire_occurrences)

output(number_of_wire_occurrences, number_of_output_wires)
