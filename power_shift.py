import sublime_plugin
import os

def get_view_name(view):
    """Returns the name for the passed view"""
    return view.name() or os.path.basename(view.file_name())

def get_views_names(views):
    """Returns a list of the names of the passed views"""
    names = []
    for view in views:
        names.append(get_view_name(view))
    return names

class PowerShiftCommand(sublime_plugin.WindowCommand):
    """Opens up a list of all currently open files"""

    def run(self):
        """Displays the pop-up list and saves the current group index"""
        self.group = self.window.active_group()
        self.views = self.window.views()

        self.window.show_quick_panel(
            get_views_names(self.views),
            self.shift_view
        )

    def shift_view(self, index):
        """Shifts the selected view into focus"""
        if index < 0:
            return

        self.window.set_view_index(self.views[index], self.group, 0)
        self.window.focus_view(self.views[index])
