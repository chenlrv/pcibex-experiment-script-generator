my_dict = {'paradigm': 'RSVP', 'display_config': 'Centered', 'word_presentation_duration': 300,
           'inter_word_break_duration': 100, 'context_choice': 'Yes', 'trials_until_break': 10,
           'context_sentence_interval': 100, 'completion_text': 'תודה על ההשתתפות!', 'break_screen_text':
           'זה הזמן לקחת הפסקה קצרה. לחזרה, יש ללחוץ על מקש הרווח', 'practice_end_text':
               'שלב האימון הסתיים. להמשך לניסוי, יש ללחוץ על מקש הרווח.'}

from loading_stuff import *

fff = retrieve_script(my_dict)
b = custom_parameters_assigment(my_dict)
a = 1

