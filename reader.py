import csv

def get_element_data(element_number):
    with open('elements.csv', 'r') as file:
        reader = csv.reader(file)
        for parts in reader:
            if parts[0] == element_number:
                element_data = {
                    'Atomic_number': parts[0],
                    'Symbol': parts[1],
                    'Element': parts[2],
                    'Origin_of_name': parts[3],
                    'Group': parts[4],
                    'Period': parts[5],
                    'Atomic_weight': parts[6],
                    'Density': parts[7],
                    'Melting_point': parts[8],
                    'Boiling_point': parts[9],
                    'Specific_heat_capacity': parts[10],
                    'Electronegativity': parts[11],
                    'Abundance_in_earth\'s_crust': parts[12]
                }
                return element_data
    return None
