
  

# Grid Interface for Computer Graphics Algorithms

  

This project provides Grid python class to display an interface for demonstrating computer graphics algorithms.

  

> <b>Important:</b> <br/>
The file [example.py](./example.py) contains a full example of using a grid interface with two simple algorithms. **The file can be used as a starting point to add your own algorithms**. Feel free to skip this documentation and come back only when needed.

  

## API Reference:

  

<a  name=“grid”  href=“#grid”>#</a> grid(*extent*, *size*)

  

Constructs a new *Grid* object.

- *extent*: the number of cells in the x and y directions, with (0,0) in the middle. For example, a grid with extent 5 has cells ranging from (-5, -5) to (5, 5)

- *size*: the size of the grid in pixels.

  

For example, to create a grid of extent 5 and 600 pixels:

  

```python
from grid import Grid

grid =  Grid(extent=5, size=600)
```

  
---
<a  name=“grid_show”  href=“#grid_show”>#</a> grid<b>.show</b>()

  

  

Displays the grid in a graphical user interface. Should be called **at the end of the script** after defining all the algorithms.

  

```python
grid.show()
```
  
> **Important: Cell states**<br>
> By default, all of the cells are *EMPTY*. They can also be *SELECTED* or *RENDERED*. 
>- *EMPTY*: Empty cells are not rendered nor selected. They are displayed with a transparent color.
>- *SELECTED*: Selected cells are inputs for the algorithms. For example, the Bresenham algorithm needs start and end cells as inputs. **To select cells, simply click on then**. They are displayed with the color red and a number with the order of selection.
>- *RENDERED*: Rendered cells are cells painted by the algorithms. They are displayed with the color black.

  
  
 ---
<a  name=“grid_render_cell”  href=“#grid_render_cell”>#</a> grid<b>.render_cell</b>(*cell*)

  

Renders the specified cell of the grid.

- *cell*: A tuple representing the X and Y coordinates of the cell to be rendered.

  

For example, to render a list of cells:

  

```python
cells = [(1,1), (2,2), (3,3)]
for c in cells:
	grid.render_cell(c)
```

  
  
---
<a  name=“grid_clear_cell”  href=“#grid_clear_cell”>#</a> grid<b>.clear_cell</b>(*cell*)

  

Clears the specified cell of the grid, returning it to the EMPTY state.

- *cell*: A tuple representing the X and Y coordinates of the cell to be cleared.

  

For example, to clear a list of cells:

  
```python
cells = [(2,2), (3,3)]
for c in cells:
	grid.clear_cell(c)
```

  
---
<a  name=“grid_clear_all”  href=“#grid_clear_all”>#</a> grid<b>.clear_all()</b>

  

Clears all cells in the grid.

  

```python
grid.clear_all()
```

  
---
<a  name=“grid_add_algorithm”  href=“#grid_add_algorithm”>#</a> grid.<b>add_algorithm</b>(*name*[, *parameters*[, *algorithm*]])

  

Adds a new algorithm functionality to the grid. **Adding an algorithm automatically creates an interface for it with inputs and a "Run" button**.

  

- *name*: a string representing the name of the algorithm. (E.g., "Rotate").

- *parameters*: a list of strings with the names of parameters the algorithm needs (E.g., "Angle").

- *algorithm*: a function to be called when the “Run” button is clicked.

  

For example, to add a rotation algorithm, which needs an "Angle" parameter to specify the angle of rotation:

  

```python
grid.add_algorithm("Rotate", parameters=["Angle"], algorithm=my_rotation_algorithm)
```

  

The *algorithm* function must accept three arguments: *selected_cells*, *rendered_cells*, and *parameters*:

- *selected_cells*: A list of cells currently marked as selected (e.g., `[(0,0), (1,1)]`)

- *rendered_cells*: A list of cells currently rendered (e.g., `[(2,2), (3,3)]`)

- *parameters*: A python dictionary that maps the defined parameters of the algorithm to their current value in the UI inputs (e.g., `{'Angle': '20'}`)

  

For example, to define `my_rotation_algorithm` used in the previous example:

  

```python
def my_rotation_algorithm(selected_cells, rendered_cells, parameters):
	angle =  int(parameters['Angle'])
	# algorithm goes here
	return
```

  
### **Example: adding an algorithm that simply renders the selected cells:**

  

- Step 1: Define the algorithm:

  

```python
def render_selected(selected_cells, rendered_cells, parameters):
	for cell in selected_cells:
		grid.render_cell(cell)
```

  

- Step 2: Add the algorithm to the grid with its *name* and *parameters* (in this case, None):

  

```python
grid.add_algorithm('Render Selected', parameters=None, algorithm=render_selected)
```

