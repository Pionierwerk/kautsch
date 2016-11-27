import ablauf
import ablauf.model


# global application model
# =============================================================================
class GlobalApplicationModel(ablauf.model.DefaultModel):
    def __init__(self, process_name, controller_name):
        ablauf.model.DefaultModel.__init__(self, process_name, controller_name)

        self.margin_left = 20
        self.margin_right = 20
        self.margin_top = 20
        self.margin_bottom = 20

        self.panel_rounding = 4

        # info bar
        self.info_bar_height = 30
        self.info_bar_margin_left = 10
        self.info_bar_margin_top = 5
        self.info_bar_vertical_space = 10
        self.info_bar_font_height = 30

        # icon
        self.icon_width = 30
        self.icon_height = 30
        self.icon_margin_left = 3
        self.icon_margin_top = 3
        self.icon_horizontal_space = 2

        # colors
        self.color_background = (44, 62, 80)
        self.color_level1 = (52, 73, 94)
        self.color_default_font_color = (255,255,255)
        self.color_selected = (127, 140, 141)

# <ab> end id: info_form
