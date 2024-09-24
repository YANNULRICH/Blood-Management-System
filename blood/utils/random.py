import random
import string

'''
def generate_random_code(length=3):
    """Generates a random string of given length."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_random_code(length=7):
    """Generates a random string of given length with characters and integers."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def generate_unique_code(model_instance):
    """Generates a unique code based on the model instance."""
    model_name = model_instance.__class__.__name__.lower()
    unique_identifier = getattr(model_instance, 'name', '')  # Use 'name' if available
    random_part = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))

    if model_name == "bloodbank":
        return f"blbk_{unique_identifier}_{random_part}"
    elif model_name == "bloodbag":
        return f"blbg_{model_instance.quantity}_{random_part}"
    else:
        raise ValueError("Unsupported model")


 def generate_unique_code(model_instance):
    """Generates a unique code based on the model instance."""
    model_name = model_instance.__class__.__name__.lower()
    unique_identifier = getattr(model_instance, 'name', '')  # Use 'name' if available
    random_part = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))

    if model_name == "bloodbank":
        return f"blbk_{unique_identifier}_{random_part[:3]}"
    elif model_name == "bloodbag":
        return f"blbg_{model_instance.quantity}_{random_part}"
    else:
        raise ValueError("Unsupported model")

'''


def generate_unique_code(model_instance):
    from blood.mblood.models import Command
    """Generates a unique code based on the model instance."""
    model_name = model_instance.__class__.__name__.lower()
    unique_identifier = getattr(model_instance, 'name', '')  # Use 'name' if available
    random_part = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))

    if model_name == "bloodbank":
        return f"blbk_{unique_identifier}_{random_part[:3]}"
    elif model_name == "bloodbag":
        return f"blbg_{model_instance.quantity}_{random_part}"
    elif model_name == "command":
        return f"comd_{model_instance.command_number}_{model_instance.quantity}"

    '''
    elif model_name == "command":

        # Retrieve current sequence number
        sequence_number = model_instance.sequence_number

        # Increment for next command and save the updated value
        model_instance.sequence_number += 1
        model_instance.save(update_fields=['sequence_number'])  # Update only sequence_number

        quantity = model_instance.quantity
        number_str = str(sequence_number).zfill(1)
        return f"comd_{number_str}_{quantity}"
        '''


'''
    elif model_name == "command":
        # Count the existing commands
        command_count = Command.objects.count()

        # Increment the count for the new command
        sequence_number = command_count + 1

        # Save the new command with the incremented sequence number
        model_instance.sequence_number = sequence_number
        model_instance.save()

        quantity = model_instance.quantity
        number_str = str(sequence_number).zfill(1)
        code = f"comd_{number_str}_{quantity}"  # Generate the code as a string
        return code  # Return the generated code

    else:
        raise ValueError("Unsupported model")
'''

def generate_code(command_number, autogen_number):
    """Generates a code in the format comd_autogen_command_number.

    Args:
        command_number: The command number to include in the code.
        autogen_number: The auto-generated number for the command.

    Returns:
        The generated code string.
    """

    return f"comd_{autogen_number}_{command_number}"

