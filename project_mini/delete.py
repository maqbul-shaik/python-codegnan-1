from users import user
def delete(Id):
    if Id in user:
        del user[Id]
        return "student ID is deleted"
    return "student ID is not found"