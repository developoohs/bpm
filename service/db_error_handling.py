
def error_handling(db):
    try:
        db
    except Exception as error:
        db.rollback()
        return str(error)

