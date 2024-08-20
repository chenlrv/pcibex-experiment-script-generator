def load_scripts():
    with open('rsvp_centered.txt', 'r') as f:
        rsvp_centered_script = f.read()
        rsvp_centered_script = rsvp_centered_script.replace('\u00a0', ' ')  # Replaces non-breaking space with a regular space
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
    scripts = load_scripts()
    if gui_output['paradigm'] == 'SPR':
        if gui_output['display_config'] == 'Moving window':
            my_script = scripts[0]
        elif gui_output['display_config'] == 'Centered':
            my_script = scripts[1]
    elif gui_output['paradigm'] == 'RSVP':
        if gui_output['display_config'] == 'Moving window':
            my_script = scripts[2]
        elif gui_output['display_config'] == 'Centered':
            my_script = scripts[3]

    return my_script


def custom_parameters_assigment(gui_output: dict):
    custom_parameters = {}

    if gui_output['paradigm'] == 'RSVP':
        custom_parameters['word_duration'] = gui_output['word_presentation_duration']
        custom_parameters['break_duration'] = gui_output['inter_word_break_duration']

    if gui_output['context_choice'] == 'Yes':
        context_break_duration = gui_output['context_sentence_interval']
        custom_parameters['context_break_duration'] = context_break_duration

    if gui_output['trials_until_break'] != 0:
        custom_parameters['trials_until_break'] = gui_output['trials_until_break']

    custom_parameters = {**custom_parameters, 'completion_text': gui_output['completion_text'],
                         'break_screen_text': gui_output['break_screen_text'],
                         'practice_end_text': gui_output['practice_end_text']}
    return custom_parameters


def customize_script(gui_output: dict):
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
    if gui_output['context_choice'] == 'No':

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
        substring_to_remove2= """
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

        # another substring to remove

        # Modifying answers to follow-up questions:
        if gui_output['question_type'] == 'yes/no':
            substring_to_replace1 = 'row.FIRST'
            substring_to_replace2 = 'row.SECOND'
            my_script = my_script.replace(substring_to_replace1, "\"כן\"")
            my_script = my_script.replace(substring_to_replace2, "\"לא\"")

    return my_script


def load_stimuli(experimental_stimuli, practice_stimuli):
    import pandas as pd

    with open(experimental_stimuli) as f:
        experimental_trials = pd.read_csv(f)
    with open(practice_stimuli) as f:
        practice_trials = pd.read_csv(f)
    stimuli = [experimental_trials, practice_trials]

    return stimuli

