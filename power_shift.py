import sublime_plugin
import os

def get_folder_for_view(view, folders):
    for folder in folders:
        if view.file_name() and view.file_name().startswith(folder):
            return os.path.relpath(view.file_name(), folder)

    return ""

def get_view_info(view, folders):
    """Returns the name for the passed view"""
    return [
        view.name() or os.path.basename(view.file_name()),
        get_folder_for_view(view, folders)
    ]

def get_view_list(views, folders):
    """Returns a list of the names of the passed views"""
    names = []
    for view in views:
        if view.file_name() or view.name():
            names.append(get_view_info(view, folders))
    return names

class PowerShiftCommand(sublime_plugin.WindowCommand):
    """Opens up a list of all currently open files"""

    def run(self):
        """Displays the pop-up list and saves the current group index"""
        self.group = self.window.active_group()
        self.views = self.window.views()

        self.window.show_quick_panel(
            get_view_list(self.views, self.window.folders()),
            self.shift_view
        )

    def shift_view(self, index):
        """Shifts the selected view into focus"""
        if index < 0:
            return

        self.window.set_view_index(self.views[index], self.group, 0)
        self.window.focus_view(self.views[index])
