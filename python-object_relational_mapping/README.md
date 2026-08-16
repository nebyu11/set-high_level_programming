# Python - Object-relational mapping

This project links Python to MySQL databases using `MySQLdb` (raw SQL queries with protection against SQL injection) and `SQLAlchemy` (Object-Relational Mapping with declarative base models and entity relationships).

## Tasks
- **0-select_states.py**: Lists all states from the database `hbtn_0e_0_usa`.
- **1-filter_states.py**: Lists all states with a name starting with `N` (upper N).
- **2-my_filter_states.py**: Takes an argument and displays all matching values in the `states` table.
- **3-my_safe_filter_states.py**: SQL injection-safe script filtering states by user input.
- **4-cities_by_state.py**: Lists all cities from the database `hbtn_0e_4_usa`.
- **5-filter_cities.py**: Takes in the name of a state as an argument and lists all cities of that state.
- **model_state.py**: Class definition of a `State` and an instance `Base = declarative_base()`.
- **7-model_state_fetch_all.py**: Lists all `State` objects via SQLAlchemy.
- **8-model_state_fetch_first.py**: Prints the first `State` object via SQLAlchemy.
- **9-model_state_filter_a.py**: Lists all `State` objects containing the letter `a`.
- **10-model_state_my_get.py**: Prints the `State` object with the name passed as argument.
- **11-model_state_insert.py**: Adds the `State` object "Louisiana" to the database.
- **12-model_state_update_id_2.py**: Changes the name of a `State` object with `id = 2` to "New Mexico".
- **13-model_state_delete_a.py**: Deletes all `State` objects with a name containing the letter `a`.
- **model_city.py**: Class definition of a `City` linking to the MySQL table `cities`.
- **14-model_city_fetch_by_state.py**: Prints all `City` objects from the database.
- **relationship_city.py**: Definition of `City` model for relationship mappings.
- **relationship_state.py**: Definition of `State` model with relationship to `City`.
- **100-relationship_states_cities.py**: Creates the `State` "California" with the `City` "San Francisco".
- **101-relationship_states_cities_list.py**: Lists all `State` objects and corresponding `City` objects.
- **102-relationship_cities_states_list.py**: Lists all `City` objects and corresponding `State` objects.
