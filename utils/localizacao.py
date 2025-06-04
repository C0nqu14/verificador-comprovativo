import requests

def obter_localizacao_por_ip(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        if r.status_code == 200:
            data = r.json()
            return {
                'ip': ip,
                'cidade': data.get('city'),
                'regiao': data.get('region'),
                'pais': data.get('country'),
                'org': data.get('org'),
                'coordenadas': data.get('loc')
            }
    except:
        pass
    return {'erro': 'Não foi possível determinar localização via IP'}
