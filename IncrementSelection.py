import sublime_plugin

class IncrementSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, inc=1):
        start_value_str = self.view.substr(self.view.sel()[0])
        try:
            start_value = int(start_value_str)
            is_digit = True
        except ValueError:
            start_value = ord(start_value_str)
            is_digit = False
        except TypeError:
            return

        counter = 0
        for selection in self.view.sel():
            new_value = start_value + counter
            if not is_digit: new_value = chr(new_value)
            self.view.insert(edit, selection.begin(), str(new_value))
            counter = counter + int(inc)

        for selection in self.view.sel():
            self.view.erase(edit, selection)
