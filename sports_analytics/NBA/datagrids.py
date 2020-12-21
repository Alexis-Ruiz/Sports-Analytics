from djblets.datagrid.grids import DataGrid, Column

class PlayerGrid(DataGrid):
    first_name = Column(sortable = True)
    last_name = Column(sortable = True)
    is_active = Column(sortable = True)

class TeamGrid(DataGrid):
    full_name = Column(sortable = True)
    abbreviation = Column(sortable = True)
    city = Column(sortable = True)
    state = Column(sortable = True)
    year_founded = Column(sortable = False)