from request_data import *
from connexion_db import *

go_to_db = Access_to_data_base()
go_to_db.open_data_base()
# go_to_db.close_data_base
connection= go_to_db.connection
run= Get_data('list_category.txt',connection)
run.access_to_api()
# operation = run.access_to_api()
# run.cursor_to_add()

    