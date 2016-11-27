import ablauf
import model

# Models
# =============================================================================
class InitModel(model.GlobalApplicationModel):
    def __init__(self, process_name, controller_name):
        model.GlobalApplicationModel.__init__(self, process_name, controller_name)

# <ab> start id:Stema
# Stema model
# =============================================================================
class StemaModel(model.GlobalApplicationModel):
    def __init__(self,process_name, controller_name):
        model.GlobalApplicationModel.__init__(self, process_name, controller_name)
# <ab> end id: Stema

# <ab> start id:library
# library model
# =============================================================================
class libraryModel(model.GlobalApplicationModel):
    def __init__(self,process_name, controller_name):
        model.GlobalApplicationModel.__init__(self, process_name, controller_name)

        self.card_width = 400
        self.card_height = 250
        self.card_margin_left = 40
        self.card_margin_top = 10
        self.card_picture_top = 35
        self.card_header_height = 10
        self.card_horizontal_space = 10
        self.card_vertical_space = 10
        self.card_font_height = 30

        self.number_of_options = 2
        self.enum_options_config = 2
        self.enum_options_quit = 1

        self.pager_number_of_options = 2
        self.pager_enum_options_back = 2
        self.pager_enum_options_forward = 1

        self.number_of_cards = 9.0

# <ab> end id: library

# <ab> start id:Info
# Info model
# =============================================================================
class InfoModel(model.GlobalApplicationModel):
    def __init__(self,process_name, controller_name):
        model.GlobalApplicationModel.__init__(self, process_name, controller_name)
# <ab> end id: Info

# <ab> start id:Filter
# Filter model
# =============================================================================
class FilterModel(model.GlobalApplicationModel):
    def __init__(self,process_name, controller_name):
        model.GlobalApplicationModel.__init__(self, process_name, controller_name)
# <ab> end id: Filter
