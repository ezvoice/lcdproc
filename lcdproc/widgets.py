"""Available widgets for LCDProc Python module."""


class StringWidget(object):
    """String widget.

    This widget displays a string. Length doesn't have to b specified.
    """

    def __init__(self, screen, ref, x, y, text, frame=None):
        """Initialization method for the String widget."""
        self.screen = screen
        self.ref = ref
        self.x = x
        self.y = y
        self.text = text
        self.frame = frame

        if self.frame:
            self.screen.server.request("widget_add %s %s %s -in %s" % (self.screen.ref, self.ref, "string", self.frame))
        else:
            self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "string"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request('widget_set %s %s %s %s "%s"' % (self.screen.ref, self.ref, self.x, self.y, self.text))

    def set_x(self, x):
        """Set the x value for the current widget."""
        self.x = x
        self.update()

    def set_y(self, y):
        """Set the y value for the current widget."""
        self.y = y
        self.update()

    def set_text(self, text):
        """Set the text value for the current widget."""
        self.text = text
        self.update()


class TitleWidget(object):
    """Title Widget; Should use only 1 per frame or screen."""

    def __init__(self, screen, ref, text):
        """Initialization method for the Title widget."""
        self.screen = screen
        self.ref = ref
        self.text = text

        self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "title"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request(
            'widget_set %s %s "%s"' %
            (self.screen.ref, self.ref, self.text))

    def set_text(self, text):
        """Set the text value for the current widget."""
        self.text = text
        self.update()


class HBarWidget(object):
    """Horizontal Bar widget.

    This displays a bar on the display, starting from x, y and going a number of pixels as specified in length.
    """

    def __init__(self, screen, ref, x, y, length, frame=None):
        """Initialization method for the HBar widget."""
        self.screen = screen
        self.ref = ref
        self.x = x
        self.y = y
        self.length = length
        self.frame = frame

        if self.frame:
            self.screen.server.request("widget_add %s %s %s -in %s" % (self.screen.ref, self.ref, "hbar", self.frame))
        else:
            self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "hbar"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request("widget_set %s %s %s %s %s" % (self.screen.ref, self.ref, self.x, self.y, self.length))

    def set_x(self, x):
        """Set the x value for the current widget."""
        self.x = x
        self.update()

    def set_y(self, y):
        """Set the y value for the current widget."""
        self.y = y
        self.update()

    def set_length(self, length):
        """Set the length value for the current widget."""
        self.length = length
        self.update()


class VBarWidget(object):
    """Vertical Bar widget.

    This displays a bar on the display, starting from x, y and going a number of pixels as specified in length.
    """

    def __init__(self, screen, ref, x, y, length, frame=None):
        """Initialization method for the VBar widget."""
        self.screen = screen
        self.ref = ref
        self.x = x
        self.y = y
        self.length = length
        self.frame = frame

        if self.frame:
            self.screen.server.request("widget_add %s %s %s -in %s" % (self.screen.ref, self.ref, "vbar", self.frame))
        else:
            self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "vbar"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request("widget_set %s %s %s %s %s" % (self.screen.ref, self.ref, self.x, self.y, self.length))

    def set_x(self, x):
        """Set the x value for the current widget."""
        self.x = x
        self.update()

    def set_y(self, y):
        """Set the y value for the current widget."""
        self.y = y
        self.update()

    def set_length(self, length):
        """Set the length value for the current widget."""
        self.length = length
        self.update()


class IconWidget(object):
    """Icon widget.

    Display an icon at the specified x and y values.
    Possible icons:
        BLOCK_FILLED
        HEART_OPEN
        HEART_FILLED
        ARROW_UP
        ARROW_DOWN
        ARROW_LEFT
        ARROW_RIGHT
        CHECKBOX_OFF
        CHECKBOX_ON
        CHECKBOX_GRAY
        SELECTOR_AT_LEFT
        SELECTOR_AT_RIGHT
        ELLIPSIS
        STOP
        PAUSE
        PLAY
        PLAYR
        FF
        FR
        NEXT
        PREV
        REC
    """

    def __init__(self, screen, ref, x, y, name, frame=None):
        """Initialization method for the Icon widget."""
        self.screen = screen
        self.ref = ref
        self.x = x
        self.y = y
        self.name = name
        self.frame = frame

        if self.frame:
            self.screen.server.request("widget_add %s %s %s -in %s" % (self.screen.ref, self.ref, "icon", self.frame))
        else:
            self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "icon"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request("widget_set %s %s %s %s %s" % (self.screen.ref, self.ref, self.x, self.y, self.name))

    def set_x(self, x):
        """Set the x value for the current widget."""
        self.x = x
        self.update()

    def set_y(self, y):
        """Set the y value for the current widget."""
        self.y = y
        self.update()

    def set_name(self, name):
        """Set the name value for the current widget."""
        self.name = name
        self.update()


class ScrollerWidget(object):
    """Scroller widget.

    This widget displays a text that flows in the vertical (v) or horizontal (h) direction at the specified speed.
    WARNING: for vertical displays this is not working on certain displays!
    """

    def __init__(self, screen, ref, left, top, right, bottom, direction, speed, text, frame=None):
        """Initialization method for the Scroller widget."""
        self.screen = screen
        self.ref = ref
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.direction = direction
        self.speed = speed
        self.text = text
        self.frame = frame

        if self.frame:
            self.screen.server.request("widget_add %s %s %s -in %s" % (self.screen.ref, self.ref, "scroller", self.frame))
        else:
            self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "scroller"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request(
            'widget_set %s %s %s %s %s %s %s %s "%s"' %
            (self.screen.ref,
             self.ref,
             self.left,
             self.top,
             self.right,
             self.bottom,
             self.direction,
             self.speed,
             self.text))

    def set_left(self, left):
        """Set the left value for the current widget."""
        self.left = left
        self.update()

    def set_top(self, top):
        """Set the top value for the current widget."""
        self.top = top
        self.update()

    def set_right(self, right):
        """Set the right value for the current widget."""
        self.right = right
        self.update()

    def set_bottom(self, bottom):
        """Set the bottom value for the current widget."""
        self.bottom = bottom
        self.update()

    def set_direction(self, direction):
        """Set the direction value for the current widget. This can be v for vertical or h for horizontal."""
        self.direction = direction
        self.update()

    def set_speed(self, speed):
        """Set the speed value for the current widget. Speed is the number of movements per rendering stroke (8 times/second)."""
        self.speed = speed
        self.update()

    def set_text(self, text):
        """Set the text value for the current widget."""
        self.text = text
        self.update()


class FrameWidget(object):
    """Frame widget.

    This is a special widget. If you save the reference for this frame, you can create new widgets passing the frame
    identifier. The widget will be contained within the frame, and the frame can have an arbitrary size in any direction,
    scrolling on the specified direction at a determinated speed.
    Note that the frame cannot control directly the widgets inside it! If you resize the frame widget, be sure to delete the
    remaining widgets!
    """

    def __init__(self, screen, ref, left, top, right, bottom, width, height, direction, speed):
        """Initialization method for the Frame widget."""
        self.screen = screen
        self.ref = ref
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.direction = direction
        self.speed = speed

        self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "frame"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request(
            'widget_set %s %s %s %s %s %s %s %s %s %s' %
            (self.screen.ref,
             self.ref,
             self.left,
             self.top,
             self.right,
             self.bottom,
             self.width,
             self.height,
             self.direction,
             self.speed))

    def set_left(self, left):
        """Set the left value for the current widget."""
        self.left = left
        self.update()

    def set_top(self, top):
        """Set the top value for the current widget."""
        self.top = top
        self.update()

    def set_right(self, right):
        """Set the right value for the current widget."""
        self.right = right
        self.update()

    def set_bottom(self, bottom):
        """Set the bottom value for the current widget."""
        self.bottom = bottom
        self.update()

    def set_width(self, width):
        """Set the width value for the current widget."""
        self.width = width
        self.update()

    def set_height(self, height):
        """Set the height value for the current widget."""
        self.height = height
        self.update()

    def set_direction(self, direction):
        """Set the direction value for the current widget. This can be v for vertical or h for horizontal."""
        self.direction = direction
        self.update()

    def set_speed(self, speed):
        """Set the speed value for the current widget. Speed is the number of movements per rendering stroke (8 times/second)."""
        self.speed = speed
        self.update()


class NumberWidget(object):
    """Scroller widget.

    This widget displays a text that flows in the vertical (v) or horizontal (h) direction at the specified speed.
    WARNING: for vertical displays this is not working on certain displays!
    """

    def __init__(self, screen, ref, x, value, frame=None):
        """Initialization method for the Number widget."""
        self.screen = screen
        self.ref = ref
        self.x = x
        self.value = value
        self.frame = frame

        if self.frame:
            self.screen.server.request("widget_add %s %s %s -in %s" % (self.screen.ref, self.ref, "num", self.frame))
        else:
            self.screen.server.request("widget_add %s %s %s" % (self.screen.ref, self.ref, "num"))
        self.update()

    def update(self):
        """Send a widget_set command with the current configuration for this widget."""
        self.screen.server.request('widget_set %s %s %s %s' % (self.screen.ref, self.ref, self.x, self.value))

    def set_x(self, x):
        """Set the x value for the current widget."""
        self.x = x
        self.update()

    def set_value(self, value):
        """Set the value field value for the current widget."""
        self.value = value
        self.update()
