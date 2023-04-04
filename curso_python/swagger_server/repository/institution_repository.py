sql_select = "select * from institution where status = 'A'"
sql_delete = "delete from institution where id =  "

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def delete_institution(self, institution_id):
        with self.session_factory() as session:
            rows = session.execute(sql_delete+str(institution_id))
            session.execute("commit;")
            return {"code" : "0",
                    "message" : "proceso satisfactorio"}
