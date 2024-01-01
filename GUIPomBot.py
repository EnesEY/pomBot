import customtkinter
from pathlib import Path
from source.reactEmojiLists import ReactEmojiLists
from config.config import *
from source.pomBot import PomBot
from logging import Logger
import logging
from tkinter import INSERT
from customtkinter import CTkTextbox

customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"

react_emoji_list_pom_start = ReactEmojiLists.sparkles  # default sparkles
react_emoji_list__pom_end = ReactEmojiLists.numbers  # default numbers


class WidgetLogger(logging.Handler):
    def __init__(self, widget: CTkTextbox):
        logging.Handler.__init__(self)
        self.setLevel(logging.INFO)
        self.widget = widget
        self.widget.configure(state="disabled")

    def emit(self, record):
        self.widget.configure(state="normal")
        # Append message (record) to the widget
        self.widget.insert(customtkinter.END, self.format(record) + "\n")
        self.widget.see(customtkinter.END)  # Scroll to the bottom
        self.widget.configure(state="disabled")


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x400")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 2), weight=0)
        self.grid_rowconfigure(1, weight=1)

        # pom start react emojis configuration
        self.react_emoji_start_label = customtkinter.CTkLabel(
            self, text="Pom-Start React Emojis:", anchor="w"
        )
        self.react_emoji_start_label.grid(row=0, column=0, padx=20, pady=(8, 0))

        self.react_emoji_start_text_box = customtkinter.CTkTextbox(self)
        self.react_emoji_start_text_box.grid(
            row=1, column=0, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        # pom end react emojis configuration
        self.react_emoji_end_label = customtkinter.CTkLabel(
            self, text="Pom-Start React Emojis:", anchor="w"
        )
        self.react_emoji_end_label.grid(row=0, column=1, padx=20, pady=(8, 0))

        self.react_emoji_end_text_box = customtkinter.CTkTextbox(self)
        self.react_emoji_end_text_box.grid(
            row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # save button
        self.save_react_emoji_config_button = customtkinter.CTkButton(
            self,
            command=self.save_new_react_emojis,
            text="Save",
        )
        self.save_react_emoji_config_button.grid(row=3, column=1, padx=20, pady=10)

        # load default values:
        for i, item in enumerate(react_emoji_list_pom_start):
            formatted_value = "{:.1f}".format(i)
            self.react_emoji_start_text_box.insert(formatted_value, f"{item}\n")

        for i, item in enumerate(react_emoji_list__pom_end):
            formatted_value = "{:.1f}".format(i)
            self.react_emoji_end_text_box.insert(formatted_value, f"{item}\n")

    def save_new_react_emojis(self):
        react_emoji_list_pom_start = []  # reset values
        react_emoji_list__pom_end = []
        for i in range(9):  # add new values
            formatted_value_1 = "{:.1f}".format(i)
            formatted_value_2 = "{:.1f}".format(i + 1)

            react_emoji_list_pom_start.append(
                self.react_emoji_start_text_box.get(
                    formatted_value_1, formatted_value_2
                )
            )
            react_emoji_list__pom_end.append(
                self.react_emoji_end_text_box.get(formatted_value_1, formatted_value_2)
            )
        # filter whitespace
        react_emoji_list_pom_start = [
            entry.strip() for entry in react_emoji_list_pom_start if entry.strip() != ""
        ]
        react_emoji_list__pom_end = [
            entry.strip() for entry in react_emoji_list__pom_end if entry.strip() != ""
        ]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("PomBot")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1), weight=1)
        self.toplevel_window = None
        self.secret_token = None

    def load_secret_token(self) -> str:
        token_file_path = Path("secret_token.txt")
        if token_file_path.exists():
            with token_file_path.open("r") as file:
                self.secret_token = file.read().strip()
                self.logger.info("Discord secret token loaded successfully!\n")
        else:
            self.logger.error(
                "No discord secret token found.\n\nGet your discord secret token as described here: \nhttps://www.youtube.com/watch?v=DArlLAq56Mo \nor here: \nhttps://www.androidauthority.com/get-discord-token-3149920/\n"
            )

    def create_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="PomBot",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.add_secret_token_button = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.add_secret_token_event,
            text="Add Secret Token",
        )
        self.add_secret_token_button.grid(row=1, column=0, padx=20, pady=10)
        self.configure_react_emojis_button = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.configure_react_emojis_event,
            text="Configure React Emojis",
        )
        self.configure_react_emojis_button.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def create_main_entry_button(self):
        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="Start Bot",
            command=self.main_button_start_event,
        )
        self.main_button_1.grid(
            row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

    def create_pom_time_config_frame(self):
        self.message_config_frame = customtkinter.CTkFrame(self)
        self.message_config_frame.grid(
            row=0,
            column=1,
            padx=(20, 0),
            pady=(20, 0),
            sticky="nsew",
        )
        self.message_config_frame.grid_columnconfigure(0, weight=1)
        self.message_config_frame.grid_rowconfigure(5, weight=1)
        self.create_pom_start_config()
        self.create_pom_end_config()
        self.create_channel_id_config()

    def create_pom_start_config(self):
        self.label_pom_start = customtkinter.CTkLabel(
            self.message_config_frame, text="Pom-Start Message:", anchor="w"
        )
        self.label_pom_start.grid(row=0, column=0, padx=20, pady=(8, 0))

        self.entry_pom_start = customtkinter.CTkEntry(
            self.message_config_frame, placeholder_text="pom-start-message"
        )
        self.entry_pom_start.grid(
            row=1,
            column=0,
            padx=20,
            pady=3,
            sticky="new",
        )

    def create_pom_end_config(self):
        self.label_pom_end = customtkinter.CTkLabel(
            self.message_config_frame, text="Pom-End Message:", anchor="w"
        )
        self.label_pom_end.grid(row=2, column=0, padx=20, pady=(8, 0))
        self.entry_pom_end = customtkinter.CTkEntry(
            self.message_config_frame, placeholder_text="pom-end-message"
        )
        self.entry_pom_end.grid(
            row=3, column=0, padx=20, pady=3, sticky="new", columnspan=2
        )

    def create_channel_id_config(self):
        self.label_channel_id = customtkinter.CTkLabel(
            self.message_config_frame, text="Channel-Id:", anchor="w"
        )
        self.label_channel_id.grid(row=4, column=0, padx=20, pady=(8, 0))
        self.entry_channel_id = customtkinter.CTkEntry(
            self.message_config_frame, placeholder_text="Channel-Id"
        )
        self.entry_channel_id.grid(
            row=5, column=0, padx=20, pady=3, sticky="new", columnspan=2
        )

    def create_textbox(self):
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(
            row=1, column=1, rowspan=1, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )

    def create_pom_duration_config_frame(self):
        self.pom_duration_config_frame = customtkinter.CTkFrame(self)
        self.pom_duration_config_frame.grid(
            row=0, column=3, rowspan=1, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )
        self.pom_start_duration_config()
        self.pom_break_duration_config()
        self.pom_start_min_config()

    def pom_start_duration_config(self):
        self.pom_duration_label = customtkinter.CTkLabel(
            self.pom_duration_config_frame, text="Pom Duration in min", anchor="w"
        )
        self.pom_duration_label.grid(row=0, column=0, padx=20, pady=(8, 0))
        self.pom_duration_config_entry = customtkinter.CTkEntry(
            self.pom_duration_config_frame, placeholder_text="Pom Duration in min"
        )
        self.pom_duration_config_entry.grid(
            row=1, column=0, padx=20, pady=3, sticky="new"
        )

    def pom_break_duration_config(self):
        self.pom_break_duration_label = customtkinter.CTkLabel(
            self.pom_duration_config_frame, text="Pom Break Duration in min", anchor="w"
        )
        self.pom_break_duration_label.grid(row=2, column=0, padx=20, pady=(6, 0))
        self.pom_break_duration_config_entry = customtkinter.CTkEntry(
            self.pom_duration_config_frame, placeholder_text="Pom Break Duration in min"
        )
        self.pom_break_duration_config_entry.grid(
            row=3, column=0, padx=20, pady=3, sticky="new"
        )

    def pom_start_min_config(self):
        self.pom_break_min_label = customtkinter.CTkLabel(
            self.pom_duration_config_frame, text="Pom Starting Minute", anchor="w"
        )
        self.pom_break_min_label.grid(row=4, column=0, padx=20, pady=(6, 0))
        self.pom_start_min_config_entry = customtkinter.CTkEntry(
            self.pom_duration_config_frame, placeholder_text="Pom Starting Minute"
        )
        self.pom_start_min_config_entry.grid(
            row=5, column=0, padx=20, pady=3, sticky="new"
        )

    def create_checkbox_frame(self):
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(
            row=1, column=3, rowspan=1, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )
        self.send_messages_activated_checkbox = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame, text="Send Messages"
        )
        self.send_messages_activated_checkbox.grid(
            row=0, column=0, pady=(20, 0), padx=20, sticky="nw"
        )
        self.react_emoji_activated_checkbox = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame, text="React Emojis"
        )
        self.react_emoji_activated_checkbox.grid(
            row=1, column=0, pady=(20, 0), padx=20, sticky="nw"
        )
        self.dad_jokes_activated_checkbox = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame, text="Dad-Jokes"
        )
        self.dad_jokes_activated_checkbox.grid(
            row=2, column=0, pady=(20, 0), padx=20, sticky="nw"
        )

        self.check_afks_activated_checkbox = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame, text="Check Afks"
        )
        self.check_afks_activated_checkbox.grid(
            row=3, column=0, pady=(20, 0), padx=20, sticky="nw"
        )
        self.check_afks_label = customtkinter.CTkLabel(
            self.checkbox_slider_frame, text="Afk time in s", anchor="w"
        )
        self.check_afks_label.grid(row=4, column=0, padx=20, pady=(10, 0))
        self.check_aks_time_entry = customtkinter.CTkEntry(
            self.checkbox_slider_frame, placeholder_text="Check Afk Time in s"
        )
        self.check_aks_time_entry.grid(
            row=5, column=0, padx=20, pady=3, sticky="new", columnspan=2
        )

    def set_default_values(self):
        self.send_messages_activated_checkbox.select()
        self.send_messages_activated_checkbox.configure(state="disabled")
        self.check_afks_activated_checkbox.select()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.entry_pom_start.insert(0, "@here pom start")
        self.entry_pom_end.insert(0, "@here pom end")
        self.check_aks_time_entry.insert(0, "8000")
        self.pom_duration_config_entry.insert(0, "25")
        self.pom_break_duration_config_entry.insert(0, "5")
        self.pom_start_min_config_entry.insert(0, "0")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def add_secret_token_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Enter your discord secret token:", title="Discord token input"
        )
        secret_token = dialog.get_input()
        if secret_token is None:
            return
        token_file_path = Path("secret_token.txt")
        with token_file_path.open("w") as file:
            file.write(secret_token)
        self.logger.info(f"Token saved to {token_file_path}")

    def configure_react_emojis_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(
                self
            )  # create window if its None or destroyed
            self.toplevel_window.focus = True  # if window exists focus it
        else:
            self.toplevel_window.focus = True  # if window exists focus it

    def create_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = WidgetLogger(self.textbox)
        formatter = logging.Formatter("%(levelname)s %(asctime)s:  %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def main_button_start_event(self):
        if self.entry_channel_id.get() is None or self.entry_channel_id.get() is "":
            self.logger.warning(f"Please input a valid channel id")
            return
        if self.secret_token is None:
            self.logger.warning(f"Please load a discord secret token")
            return

        my_config = Config(
            messagesConfig=MessagesConfig(
                sendMessagesJobActivated=self.send_messages_activated_checkbox.get(),
                pomStartMessage=self.entry_pom_start.get(),
                pomEndMessage=self.entry_pom_end.get(),
            ),  # pom start and end messages can be configured here
            reactEmojisConfig=ReactEmojisConfig(
                reactEmojisJobActivated=self.react_emoji_activated_checkbox.get(),
                pomStartReactEmojis=react_emoji_list_pom_start,
                pomEndReactEmojis=react_emoji_list__pom_end,
            ),  # lists with emojis that are reacted on pom start and end messages
            afkCheckConfig=AfkCheckConfig(
                checkAfksJobActivated=self.check_afks_activated_checkbox.get(),
                maxSecondsOld=int(self.check_aks_time_entry.get()),
            ),  # if someone didn't send messages for maxSecondsOld they are marked as afk
            markOwnMessagesUnreadConfig=MarkOwnMessagesUnreadConfig(
                markOwnMessageUnreadActivated=False
            ),
            dadJokesConfig=DadJokesConfig(
                dadJokeJobActivated=self.dad_jokes_activated_checkbox.get()
            ),  # activates dad jokes
            pomTimeConfig=PomTimeConfig(
                pom_duration=int(self.pom_duration_config_entry.get()),
                pom_break_duration=int(self.pom_break_duration_config_entry.get()),
                pom_start_time=int(self.pom_start_min_config_entry.get()),
            ),  # configure pom timer
            channel_id=int(self.entry_channel_id.get()),  # id of the dm-group
            secret_token=self.secret_token,
        )
        try:
            pomBot = PomBot(my_config, self.logger)
            pomBot.start_cycle()
        except Exception as general_error:
            print(f"Unexpected error occurred: {general_error}")


if __name__ == "__main__":
    app = App()
    app.create_textbox()
    app.create_logger()
    app.create_sidebar()
    app.create_main_entry_button()
    app.create_pom_time_config_frame()
    app.create_pom_duration_config_frame()
    app.create_checkbox_frame()
    app.set_default_values()
    app.load_secret_token()
    app.mainloop()
