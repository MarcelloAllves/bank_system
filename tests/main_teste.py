from datetime import datetime, timezone
import random

def gerar_id_conta() -> int:
    """Gera um id_conta entre 4 e 6 dígitos."""
    return random.randint(1000, 999999) 
def _now() -> datetime:
        """Timestamp UTC para created_at/updated_at."""
        
        return datetime.now(timezone.utc)
    
id = gerar_id_conta()
agora = _now()

print(f"ID -> {id}, Agora é {agora.isoformat()}")
    
    