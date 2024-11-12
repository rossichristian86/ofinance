import pandas as pd

# Converte in milioni
def Millions(Obj):
    return round(Obj / 1_000_000, 2)

# Converte in milioni
def M(Obj):
    return Millions(Obj)

# Converte in migliaia
def Tousands(Obj):
    return round(Obj / 1_000, 2)

# Converte in migliaia
def K(Obj):
    return Tousands(Obj)


"""Converte ricorsivamente tutte le chiavi in stringhe per JSON."""
def convert_keys_to_str(data):
    if isinstance(data, dict):
        return {str(k): convert_keys_to_str(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_str(i) for i in data]
    else:
        return data
    
"""Converte ricorsivamente le chiavi stringa in Timestamps dove possibile."""
def convert_keys_to_timestamp(data):
    if isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            # Prova a convertire la chiave in Timestamp, altrimenti lasciala come stringa
            try:
                new_key = pd.Timestamp(k)
            except ValueError:
                new_key = k
            new_data[new_key] = convert_keys_to_timestamp(v)
        return new_data
    elif isinstance(data, list):
        return [convert_keys_to_timestamp(i) for i in data]
    else:
        return data