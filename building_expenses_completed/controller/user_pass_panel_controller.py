from model.da.da import DataAccess
from model.entity import Users, Units, UnitUserConnector

def save(username, password, role, unit_no_str):
    try:
        user = Users(username, password, role)
        user_da = DataAccess(Users)
        user_da.save(user)

        unit_da = DataAccess(Units)
        matching_units = unit_da.find_by(Units._unit_no == unit_no_str)
        if not matching_units:
            raise Exception(f"unit {unit_no_str} not found!")
        unit = matching_units[0]

        connector = UnitUserConnector(unit, user)
        connector_da = DataAccess(UnitUserConnector)
        connector_da.save(connector)

        return True, user
    except Exception as e:
        return False, f"{e}"

def edit(id, username, password, role, unit_no_str):
    try:
        # ۱. ویرایش خودِ کاربر
        user = Users(username, password, role)
        user.id = id
        user_da = DataAccess(Users)
        user_da.edit(user)

        # ۲. پاک کردن هر ردیف قبلی واسط این کاربر
        connector_da = DataAccess(UnitUserConnector)
        old_connectors = connector_da.find_by(UnitUserConnector.user_id == id)
        for c in old_connectors:
            connector_da.remove(c)

        # ۳. پیدا کردن واحد جدید بر اساس unit_no_str
        unit_da = DataAccess(Units)
        matches = unit_da.find_by(Units._unit_no == unit_no_str)
        if not matches:
            raise Exception(f"unit {unit_no_str} not found!")
        unit = matches[0]

        # ۴. ایجاد و ذخیره ردیف جدید در unit_user_connector
        new_conn = UnitUserConnector(unit, user)
        connector_da.save(new_conn)

        return True, user

    except Exception as e:
        return False, f"{e}"


def remove(id):
    try:
        # ۱. حذف ارتباط‌های واسط
        connector_da = DataAccess(UnitUserConnector)
        conns = connector_da.find_by(UnitUserConnector.user_id == id)
        for c in conns:
            connector_da.remove(c)

        # ۲. حذف خودِ کاربر
        user_da = DataAccess(Users)
        user = user_da.remove_by_id(id)

        return True, user

    except Exception as e:
        return False, f"{e}"


def find_all_users():
    try:
        user_da = DataAccess(Users)
        user_list = user_da.find_all()
        return True, user_list
    except Exception as e:
        return False, f"{e}"

def find_all_units():
    try:
        unit_da = DataAccess(Units)
        unit_list = unit_da.find_all()
        return True, unit_list
    except Exception as e:
        return False, f"{e}"

def get_unit_no():
    try:
        status, unit_list = find_all_units()

        unit_no_list = []
        if status:
            for item in unit_list:
                unit_no_list.append(item.unit_no)
        # print(unit_no_list)
        return True, unit_no_list

    except Exception as e:
        return False, f"{e}"

def table_unit_no():
    try:
        unit_user_da = DataAccess(UnitUserConnector)
        unit_user_item_list = unit_user_da.find_all()

        unit_no_list = []
        for item in unit_user_item_list:
            unit_id = item.unit_id

            unit_da = DataAccess(Units)
            unit = unit_da.find_by_id(unit_id)

            unit_no = unit.unit_no
            unit_no_list.append(unit_no)

        return True, unit_no_list

    except Exception as e:
        return False, f"{e}"

