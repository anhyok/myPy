# user_category.py

def categorize_user(age):
    if age < 0:
        return "유효하지 않은 나이"
    elif age < 13:
        return "어린이"
    elif age < 18:
        return "청소년"
    else:
        return "성인"
