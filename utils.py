def create_question_object(question, qno):
    # Placeholder function
    return {"question": question, "number": qno}

def create_score_object(user):
    # Placeholder function
    return {"user": user, "score": 0}

def get_field(user, index):
    # Placeholder function to simulate getting a field from user data
    return user.split(",")[index] if index < len(user.split(",")) else None
