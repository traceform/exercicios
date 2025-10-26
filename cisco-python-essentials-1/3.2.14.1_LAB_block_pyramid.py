smallest_pyramid = 1 # global

block_amount = int(input("Enter the amount of blocks you have: "))

if block_amount <= smallest_pyramid:
    print(f"It is not possible to build a pyramid with {block_amount} blocks!")    
else:
    remaining_blocks, current_layer, total_layers = block_amount, 1, 0
    
    can_be_built = remaining_blocks >= current_layer

    while can_be_built:
        remaining_blocks -= current_layer        
        total_layers += 1
        current_layer += 1
        can_be_built = remaining_blocks >= current_layer

print(f"The height of the pyramid: {total_layers}")
