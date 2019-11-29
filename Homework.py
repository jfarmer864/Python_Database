import pyodbc

class Region:
    def __init__(self, region_id, region_description):
        self.table_name = 'Region'
        self.RegionID = region_id
        self.RegionDescription = region_description

class Shippers:
    def __init__(self, shipper_id, company_name, phone):
        self.table_name = 'Shippers'
        self.shipper_id = shipper_id
        self.company_name = company_name
        self.phone = phone

class Connection:
    def __init__(self, server, database_name, user_name, password):
        self.server = server
        self.database_name = database_name
        self.user_name = user_name
        self.password = password

    def make_connection(self):
        docker_northwind = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                                          'SERVER='+self.server+';'
                                          'DATABASE='+self.database_name+';'
                                          'UID='+self.user_name+';'
                                          'PWD='+self.password)
        cursor = docker_northwind.cursor()
        return(cursor)

class ReadOperation:
    def __init__(self, connection_object, table, select_string):
        self.select_string = select_string
        self.table = table
        self.connection_object = connection_object

    def do_it(self):
        sql_select = "SELECT {} FROM {}".format(self.select_string, self.table)
        self.connection_object.execute(sql_select)
        for row in self.connection_object:
            print(row)

class AddOperation:
    def __init__(self, record):
        for key, value in record.__dict__.items():
            setattr(self, key, value)

    def do_it(self):
        column_string = ""
        columns = iter(self.__dict__.keys())
        next(columns, None)
        for key in columns:
            column_string += key+','
        if column_string.endswith(','):
            column_string = column_string[:-1]
        value_string = ""
        values = iter(self.__dict__.values())
        next(values, None)
        for value in values:
            value_string += value+','
        if value_string.endswith(','):
            value_string = value_string[:-1]
        sql_add = "INSERT INTO " + self.table_name + "(" + column_string + ") VALUES(" + value_string + ")"
        # print(sql_add)
        connect = Connection('localhost,1433', 'Northwind', 'sa', 'Passw0rd2018').make_connection()
        connect.execute(sql_add)
        connect.commit()



class ProgramMain:
    def __init__(self):
        self.result = ""

    def run(self):
        #run program
        return

    def crud_operation(self):
        # I need an object representing the table
        # I need a SQL statement to run
        # I need the connection object to send query to the database
        result = ""

# main_prog = ProgramMain()
# main_prog.run()

# connect = Connection('localhost,1433','Northwind','sa','Passw0rd2018').make_connection()
# print(connect)

region = Region("'5'","'centre'")
ship = Shippers('12','Big Ships','999')
test1 = AddOperation(region)
test2 = AddOperation(ship)
test1.do_it()
