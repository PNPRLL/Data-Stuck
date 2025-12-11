"""SwapVar"""
def convert_string_to_tuples(text_in):
    """Start"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

laongdao_data = convert_string_to_tuples(input())

def swap_values(data):
    """Swap"""
    return (data[1], data[0])

print(swap_values(laongdao_data))
