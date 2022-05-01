init python in _wm_snake:
    from store import Color
    from random import randrange
    import pygame_sdl2 as pygame
    import math

    grid_line_width = 1
    grid_line_color = "#cecece"
    grid_size = 30
    xcells = 21
    ycells = 21

    width = xcells * grid_size + (xcells - 1) * grid_line_width
    height = ycells * grid_size + (ycells - 1) * grid_line_width

    target_fps = 10

    class Direction(object):
        Up = (0, -1)
        Down = (0, 1)
        Left = (-1, 0)
        Right = (1, 0)

    direction_keys = {
        pygame.K_UP: Direction.Up,
        pygame.K_DOWN: Direction.Down,
        pygame.K_LEFT: Direction.Left,
        pygame.K_RIGHT: Direction.Right,
    }

    opposites = {
        Direction.Up: Direction.Down,
        Direction.Down: Direction.Up,
        Direction.Left: Direction.Right,
        Direction.Right: Direction.Left
    }

    def draw_cell(canvas, x, y, color, padding=(0, 0)):
        if isinstance(padding, (float, int)):
            xpadding = ypadding = padding
        else:
            xpadding, ypadding = padding

        x0 = x * (grid_size + grid_line_width)
        y0 = y * (grid_size + grid_line_width)

        rect = pygame.Rect(x0 + xpadding, y0 + xpadding, grid_size - 2 * xpadding, grid_size - 2 * ypadding)
        return canvas.rect(color, rect)

    class Block(object):
        def __init__(self, x, y, padding, color):
            self.x = x
            self.y = y
            self.padding = padding
            self.color = Color(color)

        def __repr__(self):
            return "<Block x: {self.x} y: {self.y} padding: {self.padding} color: {self.color}>".format(self=self)

        def render(self, canvas):
            return draw_cell(canvas, self.x, self.y, self.color, self.padding)

    class LineGrid(renpy.Displayable):
        def __init__(self, xcells, ycells, grid_size, grid_line_width, grid_line_color, **kwargs):
            super(LineGrid, self).__init__(**kwargs)
            self.xcells = xcells
            self.ycells = ycells
            self.grid_size = grid_size
            self.grid_line_width = grid_line_width
            self.grid_line_color = Color(grid_line_color)

            self.width = xcells * grid_size + (xcells - 1) * grid_line_width
            self.height = ycells * grid_size + (ycells - 1) * grid_line_width

        def render(self, width, height, st, at):
            rv = renpy.Render(self.width, self.height)
            canvas = rv.canvas()

            grid_size = self.grid_size
            grid_line_width = self.grid_line_width
            grid_line_color = self.grid_line_color

            for i in range(1, self.xcells):
                x = i * grid_size + (i - 1) * grid_line_width
                canvas.line(grid_line_color, (x, 0), (x, width), grid_line_width)

            for i in range(1, self.ycells):
                y = i * grid_size + (i - 1) * grid_line_width
                canvas.line(grid_line_color, (0, y), (height, y), grid_line_width)

            return rv

    def create_fruit(color):
        x = randrange(1, xcells - 1)
        y = randrange(1, ycells - 1)
        return Block(x, y, 5, color)

    def default_snake_body(color):
        xcenter = xcells // 2
        ycenter = ycells // 2

        rv = [ ]

        for i in range(4):
            y = ycenter + i
            rv.append(Block(
                xcenter,
                y,
                0,
                color
            ))

        return rv

    class Snake(renpy.Displayable):
        duration = 2.0

        def __init__(self, snake_color, fruit_color, start_delay=2.0, **kwargs):
            super(Snake, self).__init__(**kwargs)
            self.snake_color = Color(snake_color)
            self.fruit_color = Color(fruit_color)
            self.start_delay = start_delay

            self.reset()

        def pause(self):
            self.paused = True

        def unpause(self):
            self.paused = False
            self.done_start_delay = False

        def reset(self):
            self.done_start_delay = False
            self.paused = True
            self.game_over = False
            self.game_over_st = None
            self.fruit = create_fruit(self.fruit_color)
            self.snake_body = default_snake_body(Color(self.snake_color))
            self.current_position = [ self.snake_body[0].x, self.snake_body[0].y ]
            self.current_direction = Direction.Up

        def render(self, width, height, st, at):
            if self.paused and not self.done_start_delay:
                if st > self.start_delay:
                    self.paused = False                    
                    self.done_start_delay = True

                renpy.redraw(self, 0.0)
            elif self.game_over:
                renpy.redraw(self, 0.0)
            else:
                renpy.redraw(self, 1.0 / target_fps)

            if not (self.paused or self.game_over):
                self.current_position[0] += self.current_direction[0]
                self.current_position[1] += self.current_direction[1]

                self.current_position[0] %= xcells
                self.current_position[1] %= ycells

                x, y = self.current_position[0], self.current_position[1]
                new_block = Block(x, y, 0, self.snake_color)

                self.snake_body.insert(0, new_block)

                if x == self.fruit.x and y == self.fruit.y:
                    self.fruit = create_fruit(self.fruit_color)
                else:
                    self.snake_body.pop()

                for b in self.snake_body[1:]:
                    if x == b.x and y == b.y:
                        self.game_over = True

            rv = renpy.Render(width, height)

            canvas = rv.canvas()

            for b in self.snake_body:
                b.render(canvas)

            self.fruit.render(canvas)

            if self.game_over:
                if self.game_over_st is None:
                    self.game_over_st = self.game_over_st or st

                else:
                    delta = st - self.game_over_st
                    alpha = (1.0 + math.cos(math.pi * delta / (0.5 * self.duration))) * 0.5

                    rv.alpha = alpha
                    
                    rv.add_shader("renpy.alpha")
                    rv.add_uniform("u_renpy_alpha", alpha)
                    rv.add_uniform("u_renpy_over", 1.0)

            return rv

        def event(self, ev, x, y, st):
            ignore_event = False

            if self.paused:
                return None

            if not self.game_over:
                direction_change_to = self.current_direction

                if ev.type == pygame.KEYDOWN:
                    if ev.key in direction_keys:
                        direction_change_to = direction_keys[ev.key]
                        ignore_event = True

                if opposites[self.current_direction] != direction_change_to:
                    self.current_direction = direction_change_to

            if ignore_event:
                raise renpy.IgnoreEvent()
            else:
                return None

    def snake_new(**kwargs):
        return Snake("#000", "#000", **kwargs)

    class SnakeOverlay(renpy.Displayable):
        def __init__(self, background="#fff", grid_color="#888", **kwargs):
            super(SnakeOverlay, self).__init__(**kwargs)
            self.background = Color(background)

            self.line_grid = LineGrid(xcells, ycells, grid_size, 1, Color(grid_color))
            self.snake = snake_new()

            self.width = self.line_grid.width
            self.height = self.line_grid.height

        def render(self, width, height, st, at):
            width, height = self.width, self.height

            lgr = renpy.render(self.line_grid, width, height, st, at)
            cr = renpy.render(self.snake, width, height, st, at)

            rv = renpy.Render(width, height)
            rv.fill(self.background)
            rv.blit(lgr, (0, 0))
            rv.blit(cr, (0, 0))

            return rv

        def event(self, ev, x, y, st):
            return self.snake.event(ev, x, y, st)

        def visit(self):
            return [ self.snake ]
