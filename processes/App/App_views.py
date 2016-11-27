import pygame

import os
import math

import ablauf.pygamekern
import ablauf.pygamekern.utils
import ablauf


# Views
# =============================================================================
# <ab> start id:library
# library view
# =============================================================================
class libraryView(ablauf.View):
    def __init__(self, name, model):
        ablauf.View.__init__(self, name, model)

        self.rendered = False
        pass

    # <ab> start container id: library_dialog
    def render_library_dialog(self, segment):
        # background
        _x = segment.x
        _y = segment.y
        _w = ablauf.Data.configuration["width"]
        _h = ablauf.Data.configuration["height"]

        ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h, self.model.color_background)

    # <ab> end container id: library_dialog

    # <ab> start container id: menu
    def render_menu(self, segment):
        # options
        _x = segment.x + self.model.margin_left
        _y = segment.y + self.model.margin_top
        _w = ablauf.Data.configuration["width"] - self.model.margin_left - self.model.margin_right - (self.model.number_of_options * (self.model.icon_width + self.model.icon_horizontal_space))
        _h = self.model.info_bar_height
        _xt = _x + self.model.info_bar_margin_left
        _yt = _y + self.model.info_bar_margin_top

        ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h, self.model.color_level1, self.model.panel_rounding, self.model.color_background)
        ablauf.pygamekern.utils.scalable_text("Games library", _xt, _yt, None, self.model.info_bar_font_height, self.model.color_text)

    # <ab> end container id: menu

    # <ab> start container id: config
    def render_config(self, segment):
        _x = ablauf.Data.configuration["width"] - self.model.margin_right - (self.model.enum_options_config * self.model.icon_width) - self.model.icon_horizontal_space
        _y = segment.y + self.model.margin_top
        _w = self.model.icon_width
        _h = self.model.icon_height
        _xt = _x + self.model.icon_margin_left
        _yt = _y + self.model.icon_margin_top

        if segment.key == self.model.actual_path:
            _color = self.model.color_text
            _color_background = self.model.color_selected
        else:
            _color = self.model.color_text
            _color_background = self.model.color_level1

        ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h,_color_background, self.model.panel_rounding, self.model.color_background)

        _path = os.path.join("gfx", "configuration.png")
        _surface = ablauf.pygamekern.utils.get_image(_path)
        if _surface is not None:
            ablauf.pygamekern.Kernel.screen.blit(_surface, (_xt, _yt))

    # <ab> end container id: config

    # <ab> start container id: quit
    def render_quit(self, segment):
        _x = ablauf.Data.configuration["width"] - self.model.margin_right - ((self.model.enum_options_quit * self.model.icon_width) - self.model.icon_horizontal_space)
        _y = segment.y + self.model.margin_top
        _w = self.model.icon_width
        _h = self.model.icon_height
        _xt = _x + self.model.icon_margin_left
        _yt = _y + self.model.icon_margin_top

        if segment.key == self.model.actual_path:
            _color = self.model.color_text
            _color_background = self.model.color_selected
        else:
            _color = self.model.color_text
            _color_background = self.model.color_level1

        ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h, _color_background, self.model.panel_rounding, self.model.color_background)

        _path = os.path.join("gfx", "exit.png");
        _surface = ablauf.pygamekern.utils.get_image(_path)
        if _surface is not None:
            ablauf.pygamekern.Kernel.screen.blit(_surface, (_xt, _yt))

    # <ab> end container id: quit

    # <ab> start container id: pager
    def render_pager(self, segment):
        # status
        _x = segment.x + self.model.margin_left
        _y = segment.y + ablauf.Data.configuration["height"] - (self.model.margin_bottom + self.model.icon_height)
        _w = ablauf.Data.configuration["width"] - self.model.margin_left - self.model.margin_right - (self.model.pager_number_of_options * (self.model.icon_width + self.model.icon_horizontal_space))
        _h = self.model.icon_height
        _xt = _x + self.model.info_bar_margin_left
        _yt = _y + self.model.info_bar_margin_top

        ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h, self.model.color_level1, self.model.panel_rounding, self.model.color_background)

        if ablauf.Data.session["game_count"] > 0:
            ablauf.pygamekern.utils.scalable_text("Page {0} of {1}".format(str(self.model.segment_by_name["library_dialog/game/game_0_0"].parent.page + 1), str(int(math.ceil(ablauf.Data.session["game_count"] / self.model.number_of_cards)))), _xt, _yt, None, self.model.info_bar_font_height, self.model.color_text)
        else:
            ablauf.pygamekern.utils.scalable_text("Page 1 of 1", _xt, _yt, None, self.model.info_bar_font_height, self.model.color_text)

    # <ab> end container id: pager

    # <ab> start container id: back
    def render_back(self, segment):
        _x = ablauf.Data.configuration["width"] - self.model.margin_right - (self.model.pager_enum_options_back * self.model.icon_width) - self.model.icon_horizontal_space
        _y = segment.y + ablauf.Data.configuration["height"] - (self.model.margin_bottom + self.model.icon_height)
        _w = self.model.icon_width
        _h = self.model.icon_height
        _xt = _x + self.model.icon_margin_left
        _yt = _y + self.model.icon_margin_top

        if segment.key == self.model.actual_path:
            _color = self.model.color_text
            _color_background = self.model.color_selected
        else:
            _color = self.model.color_text
            _color_background = self.model.color_level1

        ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h,_color_background, self.model.panel_rounding, self.model.color_background)

        _game_grid = ablauf.Automate.model.grid_by_name['game']
        _game_segment = _game_grid.segments[_game_grid.actual_segment]
        if _game_grid.page > 0:
            _path = os.path.join("gfx", "back.png")
        else:
            _path = os.path.join("gfx", "unavailable.png")

        _surface = ablauf.pygamekern.utils.get_image(_path)
        if _surface is not None:
            ablauf.pygamekern.Kernel.screen.blit(_surface, (_xt, _yt))

    # <ab> end container id: back

    # <ab> start container id: forward
    def render_forward(self, segment):
        _x = ablauf.Data.configuration["width"] - self.model.margin_right - ((self.model.pager_enum_options_forward * self.model.icon_width) - self.model.icon_horizontal_space)
        _y = segment.y + ablauf.Data.configuration["height"] - (self.model.margin_bottom + self.model.icon_height)
        _w = self.model.icon_width
        _h = self.model.icon_height
        _xt = _x + self.model.icon_margin_left
        _yt = _y + self.model.icon_margin_top

        if segment.key == self.model.actual_path:
            _color = self.model.color_text
            _color_background = self.model.color_selected
        else:
            _color = self.model.color_text
            _color_background = self.model.color_level1

        ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h, _color_background, self.model.panel_rounding, self.model.color_background)

        _game_grid = ablauf.Automate.model.grid_by_name['game']
        _game_segment = _game_grid.segments[_game_grid.actual_segment]
        if ablauf.Data.session["game_count"] > (_game_grid.page + 1) * _game_grid.max_segments:
            _path = os.path.join("gfx", "forward.png");
        else:
            _path = os.path.join("gfx", "unavailable.png")

        _surface = ablauf.pygamekern.utils.get_image(_path)
        if _surface is not None:
            ablauf.pygamekern.Kernel.screen.blit(_surface, (_xt, _yt))

    # <ab> end container id: forward

    #  <ab> start container id: game
    def render_game(self, segment):
        if segment.segment_number < ablauf.Data.session["game"].__len__():
            _x = segment.x
            _y = segment.y
            _w = self.model.card_width
            _h = self.model.card_height

            _text = ablauf.Data.session["game"][segment.segment_number].name

            _xt = segment.x
            _yt = segment.y + self.model.card_margin_top

            if segment.key == self.model.actual_path:
                _color = self.model.color_text
                _color_background = self.model.color_selected
            else:
                _color = self.model.color_text
                _color_background = self.model.color_level1

            """"
            if "text" in segment.model:
                _session_data = ""
                if "data" in segment.model:
                    for _element in segment.model["data"]:
                        _session_data += "ablauf.Data.session" + _element + ","
                    _session_data = _session_data[:-1]

                exec ("_text = '{0}'.format({1})".format(segment.model["text"], _session_data))
            else:
                _text = segment.name
            """

            ablauf.pygamekern.utils.filled_rectangle(_x, _y, _w, _h, _color_background, self.model.panel_rounding, self.model.color_background)

            ablauf.pygamekern.utils.scalable_text(_text, _xt, _yt, None, self.model.card_font_height, _color,background_width=400)

            _x = segment.x + self.model.card_margin_left
            _y = segment.y + self.model.card_picture_top

            if ablauf.Data.session["game"][segment.segment_number].id is not None:
                _path = os.path.join("gfx", "game", str(ablauf.Data.session["game"][segment.segment_number].id));
                _surface = ablauf.pygamekern.utils.get_image(_path)
                if _surface is not None:
                    _surface = pygame.transform.scale(_surface, (320, 200))
                    ablauf.pygamekern.Kernel.screen.blit(_surface, (_x, _y))

                    # <ab> end container id: game

                    # <ab> next container id:library

# <ab> end id: library
