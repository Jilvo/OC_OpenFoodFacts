#  V0.6 fin création programme principal et boucle pour programme avec vérification pour savoir si la DB est vide ou non
from request_data import *
from connexion_db import *
from program import *

go_to_db = Access_to_data_base()
go_to_db.open_data_base()
# go_to_db.close_data_base
connection= go_to_db.connection
run= Get_data('list_category.txt',connection)
run.find_if_db_is_empty()
# operation = run.access_to_api()
# run.cursor_to_add()
test = Programm(connection)
test.main_program()