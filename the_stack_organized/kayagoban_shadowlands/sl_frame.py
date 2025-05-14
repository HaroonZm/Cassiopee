from asciimatics.event import KeyboardEvent, MouseEvent
from abc import abstractmethod
from asciimatics.exceptions import NextScene
from asciimatics.widgets import (
    Frame, ListBox, Layout, Divider, Text, Button, Label, FileBrowser, RadioButtons, CheckBox, QRCode
)
import pyperclip

from shadowlands.block_callback_mixin import BlockCallbackMixin
from cached_property import cached_property
from shadowlands.tui.debug import debug, end_debug
import pdb
import logging


class SLFrame(BlockCallbackMixin, Frame):
    def __init__(self, dapp, height, width, **kwargs):
        self._dapp = dapp
        self._screen = dapp._screen

        # Add as block listener
        dapp._block_listeners.append(self)

        super(SLFrame, self).__init__(self._screen,
                                      height,
                                      width,
                                      can_scroll=False,
                                      is_modal=True,
                                      **kwargs)

        self.set_theme('shadowlands')
        self.initialize()
        self.fix()

    @abstractmethod
    def initialize(self):
        pass


    # Ctrl-d drops you into a pdb session.
    # look around, have fun.
    # executing the next line will get you back to the dapp.
    def process_event(self, event):
        if isinstance(event, MouseEvent):
            return None

        if event.key_code is 4:
            # drop to debug console
            debug(); pdb.set_trace()
            print("end_debug();; continue will get you back to the app")

        return super(SLFrame, self).process_event(event)


    def add_button(self, ok_fn, text, layout=[100], layout_index=0, add_divider=True):
        _layout = Layout(layout)
        self.add_layout(_layout)
        _layout.add_widget(Button(text, ok_fn), layout_index)
        if add_divider:
            _layout.add_widget(Divider(draw_line=False))

    def add_qrcode(self, data):
        layout = Layout([100])
        self.add_layout(layout)
        layout.add_widget(QRCode(data))

    def add_checkbox(self, text, on_change=None, default=False, **kwargs):
        layout = Layout([100])
        self.add_layout(layout)
        box = CheckBox(text, None, None, on_change, **kwargs)
        box._value = default
        layout.add_widget(box)

        return lambda: box._value


    # named arguments will be passed on to the asciimatics Text() constructor
    def add_textbox(self, label_text, default_value=None, add_divider=True, **kwargs):
        layout = Layout([100])
        self.add_layout(layout)
        text_widget = Text(label_text, **kwargs)
        if default_value is not None:
            text_widget._value = default_value
        layout.add_widget(text_widget)
        if add_divider:
            layout.add_widget(Divider(draw_line=False))
        return lambda: text_widget._value

    def add_divider(self, draw_line=False, **kwargs):
        layout = Layout([100])
        self.add_layout(layout)
        layout.add_widget(Divider(draw_line=draw_line, **kwargs))

    def add_radiobuttons(self, options, default_value=None, layout=[100], layout_index=0, add_divider=True, **kwargs):
        _layout = Layout(layout)
        self.add_layout(_layout)
        radiobuttons_widget = RadioButtons(options, **kwargs)
        _layout.add_widget(radiobuttons_widget, layout_index)
        if add_divider:
            _layout.add_widget(Divider(draw_line=False))
        if default_value is not None:
            radiobuttons_widget._value = default_value
        return lambda: radiobuttons_widget.value


    def add_listbox(self, height, options, default_value=None, on_select=None, layout=[100], layout_index=0, add_divider=True, **kwargs):
        _layout = Layout(layout)
        self.add_layout(_layout)
        list_widget = ListBox(height, options, on_select=on_select, **kwargs)
        _layout.add_widget(list_widget, layout_index)
        if add_divider:
            _layout.add_widget(Divider(draw_line=False))
        if default_value is not None:
            list_widget._value = default_value
        return lambda: list_widget.value
         
    def add_label(self, label_text, layout=[100], layout_index=0, add_divider=True):
        _layout = Layout(layout)
        self.add_layout(_layout)
        _layout.add_widget(Label(label_text), layout_index) 
        if add_divider:
            _layout.add_widget(Divider(draw_line=False))

    def add_label_with_button(self, label_text, button_text, button_fn, add_divider=True, layout=[70, 30]):
        _layout = Layout(layout)
        self.add_layout(_layout)
        _layout.add_widget(Label(label_text), 0) 
        _layout.add_widget(Button(button_text, button_fn), 1) 
        if add_divider:
            _layout.add_widget(Divider(draw_line=False))

    def add_label_row(self, labels, layout=[1, 1, 1, 1], add_divider=True):
        lyt = Layout(layout)
        self.add_layout(lyt)
        for b in labels:
            lyt.add_widget(Label(b[0]), b[1])
        if add_divider:
            lyt.add_widget(Divider(draw_line=False))
 
    # buttons = (("Nuke Tx", self.nuke_tx, 0), ...)
    def add_button_row(self, buttons, layout=[1, 1, 1, 1], add_divider=True):
        lyt = Layout(layout)
        self.add_layout(lyt)
        for b in buttons:
            lyt.add_widget(Button(b[0], b[1]), b[2])
        if add_divider:
            lyt.add_widget(Divider(draw_line=False))
 

    def add_file_browser(self, path='/', height=15, on_change_fn=None, add_divider=True):
        layout = Layout([100])
        self.add_layout(layout)
        browser = FileBrowser(height, path, on_change=on_change_fn)
        layout.add_widget(browser)
        if add_divider: 
            layout.add_widget(Divider(draw_line=False))
        return lambda: browser._value

    def close(self):
        # deregister from new_block callbacks
        self.dapp.remove_block_listener(self)
        self._destroy_window_stack()
        raise NextScene(self._scene.name)

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)
        self.dapp.add_message_dialog("Text copied to clipboard")

    @property
    def dapp(self):
        return self._dapp


class SLWaitFrame(SLFrame):
    def initialize(self):
        self.add_label(self.message)

    def __init__(self, dapp, wait_message, height, width, **kwargs):
        self.message = wait_message
        super(SLWaitFrame, self).__init__(dapp, height, width, **kwargs)

    def process_event(self, event):
        # Swallows every damn event while the user twiddles his thumbs
        return None

 
class AskClipboardFrame(SLFrame):
    def initialize(self):
        self.add_button_row([
            ("Ok", self._copy_digest, 0),
            ("Cancel", self.close, 2)
        ],
        layout=[20, 60, 20])

    def _copy_digest(self):
        pyperclip.copy(self.dapp.rx)
        self.dapp.rx = None
        self.close()


