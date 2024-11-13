from datetime import datetime

class Task:
    def __init__(self, id: int, description: str, status: str = 'to-do', created_at=None, updated_at=None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()
        self.updated_at = updated_at or datetime.now().isoformat()


    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update_description(self, description):
        self.description = description
        self.updated_at = datetime.now().isoformat()
        print(f'description was successfully updated to: {description}')

    def update_status(self, status):
        self.status = status
        self.updated_at = datetime.now().isoformat()
        print(f'status was successfully updated to: {status}')


