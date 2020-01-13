""" V1.0--cleaning coding"""
from request_data import Getdata
from connexion_db import Fill
from program import Programm
GO_TO_DB = Fill()
GO_TO_DB.open_data_base()
# go_to_db.close_data_base
CONNECTION = GO_TO_DB.connection
RUN = Getdata('list_category.txt', CONNECTION)
RUN.find_if_db_is_empty()
# operation = run.access_to_api()
# run.cursor_to_add()
TEST = Programm(CONNECTION)
TEST.main_program()
