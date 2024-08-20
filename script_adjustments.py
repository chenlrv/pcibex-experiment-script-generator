def load_scripts():
    """
    Loads and processes text scripts from specified files. Each script is read, and certain formatting
    adjustments are applied, such as replacing non-breaking spaces with regular spaces, stripping
    leading/trailing whitespace, and replacing tabs with four spaces.

    Returns:
        list: A list containing the processed scripts in the following order:
              [spr_moving_script, spr_centered_script, rsvp_moving_window, rsvp_centered_script]
    """
    with open('rsvp_centered.txt', 'r') as f:
        rsvp_centered_script = f.read()
        rsvp_centered_script = rsvp_centered_script.replace('\u00a0', ' ')  # Replaces non-breaking space with a regular space
        rsvp_centered_script = rsvp_centered_script.strip()
        rsvp_centered_script = rsvp_centered_script.replace('\t', '    ')  # Replace tabs with 4 spaces
    with open('spr_centered.txt', 'r') as f:
        spr_centered_script = f.read()
        spr_centered_script = spr_centered_script.replace('\u00a0', ' ')  # Replaces non-breaking space with a regular space
        spr_centered_script = spr_centered_script.strip()
        spr_centered_script = spr_centered_script.replace('\t', '    ')  # Replace tabs with 4 spaces
    with open('rsvp_moving_window.txt', 'r') as f:
        rsvp_moving_window = f.read()
        rsvp_moving_window = rsvp_moving_window.replace('\u00a0', ' ')  # Replaces non-breaking space with a regular space
        rsvp_moving_window = rsvp_moving_window.strip()
        rsvp_moving_window = rsvp_moving_window.replace('\t', '    ')  # Replace tabs with 4 spaces
    with open('spr_moving_window.txt', 'r') as f:
        spr_moving_script = f.read()
        spr_moving_script = spr_moving_script.replace('\u00a0', ' ')  # Replaces non-breaking space with a regular space
        spr_moving_script = spr_moving_script.strip()
        spr_moving_script = spr_moving_script.replace('\t', '    ')  # Replace tabs with 4 spaces

    scripts = [spr_moving_script, spr_centered_script, rsvp_moving_window, rsvp_centered_script]

    return scripts


def retrieve_script(gui_output: dict):
    """
    Retrieves the appropriate script based on the user's GUI output selection.

    Parameter:
        gui_output (dict): A dictionary containing the user's selections from the GUI.
                            Expected keys are 'paradigm' and 'display_config'.

    Returns:
        str: The script corresponding to the selected paradigm and display configuration.
    """
    scripts = load_scripts()
    if gui_output['paradigm'] == 'SPR':
        if gui_output['display_config'] == 'Moving Window':
            my_script = scripts[0]
        elif gui_output['display_config'] == 'Centered':
            my_script = scripts[1]
    elif gui_output['paradigm'] == 'RSVP':
        if gui_output['display_config'] == 'Moving Window':
            my_script = scripts[2]
        elif gui_output['display_config'] == 'Centered':
            my_script = scripts[3]

    return my_script


def custom_parameters_assigment(gui_output: dict):
    """
    Assigns custom parameters based on the user's GUI output.

    Parameter:
        gui_output (dict): A dictionary containing the user's selections from the GUI.
                            Expected keys are 'paradigm', 'context_choice', 'trials_before_break',
                            'word_presentation_duration', 'inter_word_break_duration',
                            'context_sentence_interval', 'completion_text', 'break_screen_text',
                            and 'practice_end_text'.

    Returns:
        dict: A dictionary containing the assigned custom parameters for script customization.
    """
    custom_parameters = {}

    if gui_output['paradigm'] == 'RSVP':
        custom_parameters['word_duration'] = gui_output['duration_config']['word_presentation_duration']
        custom_parameters['break_duration'] = gui_output['duration_config']['inter_word_break_duration']

    if gui_output['sections']['context'] == 'Yes':
        context_break_duration = gui_output['sections']['context_sentence_interval']
        custom_parameters['context_break_duration'] = context_break_duration

    if gui_output['sections']['trials_before_breaks'] != 0:
        custom_parameters['trials_before_break'] = gui_output['sections']['trials_before_breaks']

    custom_parameters = {**custom_parameters, 'completion_text': gui_output['sections']['completion_screen_text'],
                         'break_screen_text': gui_output['sections']['break_screen_text'],
                         'practice_end_text': gui_output['sections']['practice_end_text']}
    return custom_parameters


def customize_script(gui_output: dict):
    """
    Customizes the script based on user-specified parameters and context settings.

    Parameter:
        gui_output (dict): A dictionary containing the user's selections from the GUI.
                            It includes parameters for the script and configurations for context
                            presentation and follow-up question handling.

        Returns:
            str: The fully customized script as a string, ready to be saved to a file.
        """
    custom_parameters = custom_parameters_assigment(gui_output)
    # Initialize an empty list to hold each line
    lines = []

    # Iterate over the dictionary and format each key-value pair
    for key, value in custom_parameters.items():
        if isinstance(value, str):
            # Format string values with quotes
            line = f'{key} = "{value}";'
        else:
            # Format non-string values directly
            line = f'{key} = {value};'

        # Append the formatted line to the list
        lines.append(line)

    # Join all lines into a single string with newline characters
    variables_assignment_string = '\n'.join(lines)

    # Join lines to the script
    my_script = retrieve_script(gui_output)
    my_script = variables_assignment_string + '\n' + my_script + '\n\n'

    # Remove context presentation parts if needed
    if gui_output['sections']['context'] == 'No':

        # Substrings to remove:
        substring_to_remove1 = '''
                // Show context
        newText("context", row.context)
            .center() // Center the context text
            .print()
        ,
        newKey(" ")
            .wait()
        ,
        getText("context")
            .remove()
        ,
        newTimer(context_break_duration).start().wait()  // context_break_duration ms break after context
        ,

        '''
        substring_to_remove2 = """
                // Show context
        newText("context", row.context)
            .center() // Center the context text
            .print()
        ,
        newKey(" ")
            .wait()
        ,
        getText("context")
            .remove()
        ,
        """

        # Remove the substrings. Both substrings are needed because of indentation differences in the txt files.
        my_script = my_script.replace(substring_to_remove1.strip(), '')
        my_script = my_script.replace(substring_to_remove2.strip(), '')

        # Modifying answers to follow-up questions
        if gui_output['sections']['answers'] != 'Custom':
            substring_to_replace1 = 'row.FIRST'
            substring_to_replace2 = 'row.SECOND'
            my_script = my_script.replace(substring_to_replace1, "\"כן\"")
            my_script = my_script.replace(substring_to_replace2, "\"לא\"")

    return my_script


def write_script(gui_output: dict):
    """
    Customizes and writes the final script to a text file.

    Input:
        gui_output (dict): A dictionary containing the user's selections from the GUI.

    Saves:
        A text file named "customized_script.txt" containing the fully customized script.
    """
    my_script = customize_script(gui_output)
    with open("customized_script.txt", "w") as text_file:
        text_file.write(my_script)


