from tkinter import Tk, Canvas, Label, Frame, Button, Entry
from .grid_data_structure import GridDataStructure


class Grid:
    MARGIN_SIZE = 10

    def __init__(self, extent, size):
        self.raster = GridDataStructure(extent)
        self.window_size = size, size
        self.grid_size = size - 2 * Grid.MARGIN_SIZE, size - 2 * Grid.MARGIN_SIZE
        dimension = 2 * extent + 1
        self.cell_size = self.grid_size[0] / dimension, self.grid_size[1] / dimension
        self.root = Tk()

        self.main_frame = Frame(self.root)
        self.main_frame.pack(anchor='center', expand=True, fill='both')

        self.grid_frame = Frame(self.main_frame)
        self.grid_frame.pack(side='left')

        clear_frame = Frame(self.grid_frame)
        clear_frame.pack()
        Button(clear_frame, text='Clear All', command=self._clear_all).pack(side='left')
        Button(clear_frame, text='Clear Selected Cells', command=self._clear_selected_cells).pack(side='left')

        self.controls_frame = Frame(self.main_frame)
        self.controls_frame.pack(side='left')

        self.canvas = Canvas(self.grid_frame, width=size, height=size)
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self._on_canvas_click)


    def add_algorithm(self, name, parameters=None, algorithm=None):
        frame = Frame(self.controls_frame)
        frame.pack(anchor='w')
        label = Label(frame, text=name)
        label.pack(side='left')
        entries = []
        if parameters:
            for variable in parameters:
                var_label = Label(frame, text=variable)
                var_label.pack(side='left')
                var_entry = Entry(frame, width=5)
                var_entry.pack(side='left')
                entries.append((variable, var_entry))
        if algorithm:
            run_button = Button(frame, text='Run', command=lambda: self._on_run_click(algorithm, entries))
            run_button.pack(side='left')
        return frame

    def render_cell(self, cell):
        self.raster.render_cell(cell)


    def clear_cell(self, cell):
        self.raster.clear_cell(cell)
        self._redraw()

    def show(self):
        self._redraw()
        self.root.mainloop()


    def _select_cell(self, cell):
        self.raster.select_cell(cell)
        
    def _on_canvas_click(self, event):
        x = event.x - Grid.MARGIN_SIZE
        raw_y = event.y - Grid.MARGIN_SIZE
        y = (self.grid_size[1]) - raw_y

        if 0 <= x <= self.grid_size[0] and 0 <= y <= self.grid_size[1]:
            print(x, y)
            cell_x = int(x // self.cell_size[0]) - self.raster.extent
            cell_y = int(y  // self.cell_size[1]) - self.raster.extent
            self._select_cell((cell_x, cell_y))
            self._redraw()


    def _redraw(self):
        self.canvas.delete('all')

        dimension = 2 * self.raster.extent + 1
        for i in range(dimension):
            for j in range(dimension):
                x1 = i * self.cell_size[0] + Grid.MARGIN_SIZE
                y1 = (dimension - j - 1) * self.cell_size[1] + Grid.MARGIN_SIZE
                x2 = x1 + self.cell_size[0]
                y2 = y1 + self.cell_size[1]
                x, y = i - (self.raster.extent*2 + 1), j - (self.raster.extent*2 + 1)
                if self.raster.selected_cells[x][y]:
                    color = 'red'
                    text_color = 'white'
                    text = str(self.raster.selected_cells[x][y])
                elif self.raster.rendered_cells[x][y]:
                    color = '#444444'
                    text_color = ''
                    text = ''
                else:
                    color = ''
                    text_color = ''
                    text = ''
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='gray')
                if text:
                    x_center = (x1 + x2) / 2
                    y_center = (y1 + y2) / 2
                    font_size = int(min(self.cell_size) * 0.8)
                    font = f'Helvetica {font_size} bold'
                    self.canvas.create_text(x_center, y_center, text=text, fill=text_color, font=font)

                zero_x = self.raster.extent * self.cell_size[0] + Grid.MARGIN_SIZE + self.cell_size[0] / 2
                zero_y = self.raster.extent * self.cell_size[1] + Grid.MARGIN_SIZE + self.cell_size[1] / 2
                self.canvas.create_line(zero_x, Grid.MARGIN_SIZE, zero_x, self.window_size[1] - Grid.MARGIN_SIZE, fill='#222222', width=3)
                self.canvas.create_line(Grid.MARGIN_SIZE, zero_y, self.window_size[0] - Grid.MARGIN_SIZE, zero_y, fill='#222222', width=3)


    def _on_run_click(self, action, entries):
        selected_cells = self.raster.get_selected_cells()
        rendered_cells = self.raster.get_rendered_cells()
        parameters = {entry[0]: entry[1].get() for entry in entries}
        action(selected_cells, rendered_cells, parameters)
        self._clear_selected_cells()

    def _clear_all(self):
        self.raster.clear_all()
        self._redraw()

    def _clear_selected_cells(self):
        self.raster.clear_selected_cells()
        self._redraw()
