import uuid
from datetime import datetime

def create_xapi_statement(student_id, question, student_answer, correct_answer, is_correct):
    return {
        "id": str(uuid.uuid4()),
        "actor": {
            "objectType": "Agent",
            "name": f"Student {student_id}"
        },
        "verb": {
            "id": "answered",
            "display": {"en-US": "answered"}
        },
        "object": {
            "id": "question",
            "definition": {
                "name": {"en-US": question}
            }
        },
        "result": {
            "response": student_answer,
            "success": is_correct,
            "correct_answer": correct_answer
        },
        "timestamp": datetime.utcnow().isoformat()
    }
