import tkinter as tk
import os
import string
from tkinter import StringVar, font, filedialog, messagebox


class PcibexScriptGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PcIBEX Experiment Script Generator")
        self.root.geometry("600x480")
        self.root.resizable(False, False)

        self.large_font = font.Font(family="Helvetica", size=16)
        self.medium_font = font.Font(family="Helvetica", size=13)
        self.button_font = font.Font(family="Helvetica", size=14, weight="bold")

        self.paradigm = StringVar(value="none_selected")
        self.display_config = StringVar(value="none_selected")
        self.demographics = StringVar(value="none_selected")
        self.instructions = StringVar(value="none_selected")
        self.practice = StringVar(value="none_selected")
        self.practice_file = None
        self.practice_end = StringVar(value="none_selected")
        self.done = StringVar(value="none_selected")
        self.debriefing = StringVar(value="none_selected")
        self.completion_screen = StringVar(value="none_selected")
        self.breaks = StringVar(value="none_selected")
        self.presentation_duration = tk.IntVar()
        self.inter_word_break_duration = tk.IntVar()
        self.context_sentence_interval = tk.IntVar()
        self.number_of_breaks = tk.IntVar()
        self.break_text = tk.StringVar()
        self.configurations = {}

        self.create_first_screen()

    def create_first_screen(self):
        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Welcome to PcIBEX Experiment Script Generator",
                           font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        label2 = tk.Label(frame, text="Choose a paradigm:", font=self.large_font, anchor='w')
        label2.pack(anchor='w', padx=30, pady=(10, 0))

        rb_frame = tk.Frame(frame)
        rb_frame.pack(anchor='w', padx=20, pady=(10, 30))
        rb1 = tk.Radiobutton(rb_frame, text="SPR", variable=self.paradigm, value="SPR", font=self.medium_font,
                             command=self.enable_next_button)
        rb2 = tk.Radiobutton(rb_frame, text="RVSP", variable=self.paradigm, value="RVSP", font=self.medium_font,
                             command=self.enable_next_button)
        rb1.pack(anchor='w', pady=10, padx=20)
        rb2.pack(anchor='w', pady=10, padx=20)

        self.next_button = tk.Button(self.root, text="Next", command=self.create_second_screen, state=tk.DISABLED,
                                     font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.next_button.pack(pady=20)

    def create_second_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Display Configuration",
                           font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        label2 = tk.Label(frame, text="Choose display configuration:", font=self.large_font, anchor='w')
        label2.pack(anchor='w', padx=30, pady=(10, 0))

        rb_frame = tk.Frame(frame)
        rb_frame.pack(anchor='w', padx=20, pady=(10, 30))
        rb1 = tk.Radiobutton(rb_frame, text="Moving Window", variable=self.display_config, value="Moving Window",
                             font=self.medium_font, command=self.enable_next_button)
        rb2 = tk.Radiobutton(rb_frame, text="Center", variable=self.display_config, value="Center",
                             font=self.medium_font, command=self.enable_next_button)
        rb1.pack(anchor='w', pady=10, padx=20)
        rb2.pack(anchor='w', pady=10, padx=20)

        self.next_button = tk.Button(self.root, text="Next", command=self.create_third_screen, state=tk.DISABLED,
                                     font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.next_button.pack(pady=20)

    def enable_next_button(self):
        if self.paradigm.get() or self.display_config.get():
            self.next_button.config(state=tk.NORMAL)

    def create_third_screen(self):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.geometry("600x750")
        # Third Screen Elements
        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Section Configurations",
                           font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        label2 = tk.Label(frame, text="Choose which sections to include:", font=self.large_font, anchor='w')
        label2.pack(anchor='w', padx=20, pady=(20, 20))

        sections = [
            ("Demographics", self.demographics),
            ("Instructions", self.instructions),
            ("Practice", self.practice),
            ("Practice End", self.practice_end),
            ("Done", self.done),
            ("Debriefing", self.debriefing),
            ("Completion Screen", self.completion_screen)
        ]

        for section, var in sections:
            section_frame = tk.Frame(frame)
            section_frame.pack(fill='x', pady=10)

            # Section Label
            label = tk.Label(section_frame, text=section + ":", font=self.medium_font, anchor='w')
            label.pack(side='left', padx=(20, 10))

            # Yes/No Radio Buttons
            rb_frame = tk.Frame(section_frame)
            rb_frame.pack(side='left', padx=(10, 0))
            rb_yes = tk.Radiobutton(rb_frame, text="Yes", variable=var, value="Yes", font=self.medium_font,
                                    command=self.check_next_screen)
            rb_no = tk.Radiobutton(rb_frame, text="No", variable=var, value="No", font=self.medium_font,
                                   command=self.check_next_screen)
            rb_yes.pack(side='left', padx=10)
            rb_no.pack(side='left', padx=10)

        if self.paradigm.get() == "SPR":
            breaks_frame = tk.Frame(frame)
            breaks_frame.pack(fill='x', pady=10)

            label = tk.Label(breaks_frame, text="Breaks:", font=self.medium_font, anchor='w')
            label.pack(side='left', padx=(20, 10))

            rb_frame = tk.Frame(breaks_frame)
            rb_frame.pack(side='left', padx=(10, 0))
            rb_yes = tk.Radiobutton(rb_frame, text="Yes", variable=self.breaks, value="Yes", font=self.medium_font,
                                    command=self.check_next_screen)
            rb_no = tk.Radiobutton(rb_frame, text="No", variable=self.breaks, value="No", font=self.medium_font,
                                   command=self.check_next_screen)
            rb_yes.pack(side='left', padx=10)
            rb_no.pack(side='left', padx=10)

        # Bottom frame to hold the Next button
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill='x', pady=20)

        self.next_button = tk.Button(bottom_frame, text="Next", state=tk.DISABLED, command=self.create_fourth_screen,
                                     font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.next_button.pack(anchor='center', pady=15, padx=15)

    def create_next_screen_based_on_practice(self):
        if self.practice.get() == "Yes":
            self.create_practice_file_upload_screen()
        else:
            self.create_fourth_screen()

    def check_next_screen(self):
        # Check if all section configurations have been chosen
        all_selected = all([
            self.demographics.get() != "none_selected",
            self.instructions.get() != "none_selected",
            self.practice.get() != "none_selected",
            self.practice_end.get() != "none_selected",
            self.done.get() != "none_selected",
            self.debriefing.get() != "none_selected",
            self.completion_screen.get() != "none_selected",
            (self.breaks.get() != "none_selected" if self.paradigm.get() == "SPR" else True)
        ])

        # Enable the Next button if all are selected
        if all_selected:
            self.next_button.config(state=tk.NORMAL)

            # Set the appropriate command based on the Practice selection
            if self.practice.get() == "Yes":
                self.next_button.config(command=self.create_practice_file_upload_screen)
            else:
                self.next_button.config(command=self.create_fourth_screen)
        else:
            self.next_button.config(state=tk.DISABLED)

    def create_practice_file_upload_screen(self):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Practice File Upload Screen Elements
        label = tk.Label(self.root, text="Upload Practice File", font=self.large_font)
        label.pack(pady=20)

        upload_button = tk.Button(self.root, text="Browse", command=self.upload_practice_file, font=self.button_font,
                                  bg="lightblue", activebackground="lightgreen")
        upload_button.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.create_fourth_screen, state=tk.DISABLED,
                                     font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.next_button.pack(pady=20)

    def upload_practice_file(self):
        try:
            self.practice_file = filedialog.askopenfilename(title="Select Practice File",
                                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if not self.is_english_filename(self.practice_file):
                self.practice_file = None
                raise ValueError(
                    "Practice file name must contain only English letters, digits, dots, underscores, or hyphens")

            if self.practice_file:
                self.next_button.config(state=tk.NORMAL)
        except BaseException as e:
            messagebox.showerror("Invalid",
                                 "Practice file name must contain only English letters, digits, dots, underscores, or hyphens")

    def is_english_filename(self, filename):
        return all(char in string.ascii_letters + string.digits + "._-" for char in os.path.basename(filename))

    def create_fourth_screen(self):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("600x480")

        # Fourth Screen Elements
        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Context Configuration",
                           font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        frame1 = tk.Frame(frame)
        frame1.pack(fill='x', pady=10)
        tk.Label(frame1, text="Presentation Duration (ms):", font=self.medium_font, anchor='w').pack(side='left',
                                                                                                     padx=(20, 10))
        tk.Entry(frame1, textvariable=self.presentation_duration, font=self.medium_font, width=10).pack(side='left',
                                                                                                        padx=10)

        frame2 = tk.Frame(frame)
        frame2.pack(fill='x', pady=10)
        tk.Label(frame2, text="Inter-word Break Duration (ms):", font=self.medium_font, anchor='w').pack(side='left',
                                                                                                         padx=(20, 10))
        tk.Entry(frame2, textvariable=self.inter_word_break_duration, font=self.medium_font, width=10).pack(side='left',
                                                                                                            padx=10)

        frame3 = tk.Frame(frame)
        frame3.pack(fill='x', pady=10)
        tk.Label(frame3, text="Context Sentence Interval (ms):", font=self.medium_font, anchor='w').pack(side='left',
                                                                                                         padx=(20, 10))
        tk.Entry(frame3, textvariable=self.context_sentence_interval, font=self.medium_font, width=10).pack(side='left',
                                                                                                            padx=10)

        # Bottom frame to hold the Next/Generate button
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill='x', pady=20)

        if self.paradigm.get() == "SPR" and self.breaks.get() == "Yes":
            next_button = tk.Button(bottom_frame, text="Next", command=self.validate_and_proceed, font=self.button_font,
                                    bg="lightblue", activebackground="lightgreen")
        else:
            next_button = tk.Button(bottom_frame, text="Generate", command=self.validate_and_proceed,
                                    font=self.button_font, bg="lightblue", activebackground="lightgreen")

        next_button.pack(anchor='center', pady=15, padx=15)

    def validate_and_proceed(self):
        try:
            presentation_duration = int(self.presentation_duration.get())
            inter_word_break_duration = int(self.inter_word_break_duration.get())
            context_sentence_interval = int(self.context_sentence_interval.get())

            if presentation_duration <= 0 or inter_word_break_duration <= 0 or context_sentence_interval <= 0:
                raise ValueError("All durations must be greater than 0")

            if self.paradigm.get() == "SPR" and self.breaks.get() == "Yes":
                self.create_break_config_screen()
            else:
                self.generate_output()
        except BaseException as e:
            messagebox.showerror("Invalid Input", "All durations must be integer greater than 0")

    def create_break_config_screen(self):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("600x480")

        # Break Configuration Screen Elements
        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Break Configuration",
                           font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        frame1 = tk.Frame(frame)
        frame1.pack(fill='x', pady=10)
        tk.Label(frame1, text="Number of Breaks:", font=self.medium_font, anchor='w').pack(side='left', padx=(20, 10))
        tk.Entry(frame1, textvariable=self.number_of_breaks, font=self.medium_font, width=10).pack(side='left', padx=10)

        frame2 = tk.Frame(frame)
        frame2.pack(fill='x', pady=10)
        tk.Label(frame2, text="Text of the Break:", font=self.medium_font, anchor='w').pack(side='left', padx=(20, 10))
        tk.Entry(frame2, textvariable=self.break_text, font=self.medium_font, width=30).pack(side='left', padx=10)

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill='x', pady=20)

        generate_button = tk.Button(bottom_frame, text="Generate", command=self.validate_break_config,
                                    font=self.button_font, bg="lightblue", activebackground="lightgreen")
        generate_button.pack(anchor='center', pady=15, padx=15)

    def validate_break_config(self):
        try:
            number_of_breaks = int(self.number_of_breaks.get())
            break_text = self.break_text.get()

            if number_of_breaks <= 0:
                raise ValueError("Number of breaks must be greater than 0")
            if not break_text.strip():
                raise ValueError("Text of the break cannot be empty")

            self.generate_output()
        except BaseException as e:
            messagebox.showerror("Invalid Input", str(e))

    def generate_output(self):
        self.configurations = {
            "paradigm": self.paradigm.get(),
            "display_config": self.display_config.get(),
            "sections": {
                "demographics": self.demographics.get(),
                "instructions": self.instructions.get(),
                "practice": self.practice.get(),
                "practice_file": self.practice_file,
                "practice_end": self.practice_end.get(),
                "done": self.done.get(),
                "debriefing": self.debriefing.get(),
                "completion_screen": self.completion_screen.get(),
                "breaks": self.breaks.get() if self.paradigm.get() == "SPR" else None
            },
            "context": {
                "presentation_duration": self.presentation_duration.get(),
                "inter_word_break_duration": self.inter_word_break_duration.get(),
                "context_sentence_interval": self.context_sentence_interval.get()
            },
            "break_config": {
                "number_of_breaks": self.number_of_breaks.get() if self.breaks.get() == "Yes" else None,
                "break_text": self.break_text.get() if self.breaks.get() == "Yes" else None
            }
        }
        print(self.configurations)
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = PcibexScriptGeneratorApp(root)
    root.mainloop()
