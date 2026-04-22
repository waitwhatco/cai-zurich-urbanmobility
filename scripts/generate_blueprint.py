import json
import re
from pathlib import Path


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

base_nodes = [
    ("Zürich HB", "Zürich 1 (City)", 47.3780, 8.5402, "Regional Hub", "S-Bahn, Tram, Bus, Bike-Share, Car-Share", 250000, "High", "Full", 1, 1, 1, "Scooters, Bikes, Walk", "High", 1, "Major Regional Hub"),
    ("Stadelhofen", "Zürich 1 (City)", 47.3665, 8.5486, "City Hub", "S-Bahn, Tram, Bus, Bike-Share", 85000, "High", "Full", 0, 1, 0, "Bikes, Walk", "High", 0, "City Hub"),
    ("Zürich Oerlikon", "Zürich 11 (Affoltern/Oerlikon/Seebach)", 47.4114, 8.5442, "Regional Hub", "S-Bahn, Tram, Bus, Bike-Share, Car-Share", 120000, "High", "Full", 1, 1, 1, "Scooters, Bikes, Walk", "High", 1, "Major Regional Hub"),
    ("Zürich Altstetten", "Zürich 9 (Altstetten/Albisrieden)", 47.3912, 8.4898, "Regional Hub", "S-Bahn, Tram, Bus, Bike-Share, Car-Share", 95000, "High", "Full", 1, 1, 1, "Bikes, Walk", "High", 1, "Major Regional Hub"),
    ("Zürich Wiedikon", "Zürich 3 (Wiedikon)", 47.3710, 8.5200, "City Hub", "S-Bahn, Tram, Bus, Bike-Share", 70000, "High", "Full", 0, 1, 1, "Scooters, Bikes, Walk", "High", 0, "City Hub"),
    ("Zürich Hardbrücke", "Zürich 5 (Industriequartier)", 47.3853, 8.5174, "City Hub", "S-Bahn, Tram, Bus, Bike-Share", 80000, "High", "Full", 0, 1, 1, "Bikes, Walk", "High", 0, "City Hub"),
    ("Zürich Enge", "Zürich 2 (Wollishofen/Leimbach/Enge)", 47.3655, 8.5309, "Interchange", "S-Bahn, Tram, Bus, Bike-Share", 42000, "Medium", "Full", 0, 1, 1, "Walk, Bikes", "Medium", 0, "City Hub"),
    ("Zürich Flughafen", "Region (Glatt Valley)", 47.4506, 8.5622, "Regional Hub", "S-Bahn, Bus, Car-Share", 110000, "High", "Full", 1, 0, 1, "Bus, Car-Share", "High", 1, "Major Regional Hub"),
    ("Zürich Tiefenbrunnen", "Zürich 8 (Riesbach)", 47.3502, 8.5765, "Interchange", "S-Bahn, Tram, Bus, Bike-Share", 28000, "Medium", "Full", 1, 1, 0, "Walk, Bikes", "Medium", 0, "Interchange Station"),
    ("Zürich Wollishofen", "Zürich 2 (Wollishofen/Leimbach/Enge)", 47.3478, 8.5316, "Interchange", "S-Bahn, Tram, Bus, Bike-Share", 24000, "Medium", "Full", 0, 1, 1, "Walk, Scooters", "Medium", 0, "Interchange Station"),
    ("Zürich Seebach", "Zürich 11 (Affoltern/Oerlikon/Seebach)", 47.4242, 8.5448, "Local Station", "S-Bahn, Bus", 13000, "Medium", "Full", 1, 0, 0, "Bus, Walk", "Medium", 0, "Local Station"),
    ("Zürich Affoltern", "Zürich 11 (Affoltern/Oerlikon/Seebach)", 47.4178, 8.5127, "Local Station", "S-Bahn, Bus, Bike-Share", 18000, "Medium", "Full", 1, 1, 0, "Bikes, Bus", "Medium", 0, "Local Station"),
    ("Zürich Leimbach", "Zürich 2 (Wollishofen/Leimbach/Enge)", 47.3294, 8.5275, "Local Station", "S-Bahn, Bus", 9000, "Low", "Partial", 0, 0, 0, "Walk, Bus", "Low", 0, "Local Station"),
    ("Zürich Giesshübel", "Zürich 3 (Wiedikon)", 47.3632, 8.5186, "Local Station", "S-Bahn, Bus, Bike-Share", 11000, "Low", "Full", 0, 1, 0, "Walk, Bikes", "Low", 0, "Local Station"),
    ("Zürich Triemli", "Zürich 3 (Wiedikon)", 47.3615, 8.4996, "Interchange", "Tram, Bus, Bike-Share", 16000, "Medium", "Full", 0, 1, 0, "Scooters, Walk", "Medium", 0, "Local Station"),
    ("Zürich Albisrieden", "Zürich 9 (Altstetten/Albisrieden)", 47.3757, 8.4918, "Interchange", "Tram, Bus, Bike-Share", 19000, "Medium", "Full", 0, 1, 0, "Walk, Bikes", "Medium", 0, "Interchange Station"),
    ("Zürich Escher-Wyss-Platz", "Zürich 5 (Industriequartier)", 47.3906, 8.5203, "Interchange", "Tram, Bus, Bike-Share", 26000, "Medium", "Full", 0, 1, 1, "Bikes, Scooters", "Medium", 0, "Interchange Station"),
    ("Zürich Central", "Zürich 1 (City)", 47.3778, 8.5432, "Interchange", "Tram, Bus, Walk", 38000, "High", "Partial", 0, 1, 0, "Walk, Bikes", "High", 0, "Interchange Station"),
    ("Zürich Bellevue", "Zürich 1 (City)", 47.3662, 8.5469, "Interchange", "Tram, Bus, Walk, Bike-Share", 45000, "High", "Full", 0, 1, 0, "Walk, Scooters, Bikes", "High", 0, "Interchange Station"),
    ("Zürich Paradeplatz", "Zürich 1 (City)", 47.3695, 8.5388, "Interchange", "Tram, Bus, Walk", 52000, "High", "Full", 0, 1, 0, "Walk, Bikes", "High", 0, "Interchange Station"),
    ("Zürich Sihlcity Nord", "Zürich 3 (Wiedikon)", 47.3586, 8.5234, "Micro-hub", "Tram, Bus, Bike-Share, Car-Share", 12000, "Medium", "Full", 1, 1, 1, "Scooters, Bikes, Walk", "Medium", 0, "Micro Hub"),
    ("Zürich Binz", "Zürich 3 (Wiedikon)", 47.3599, 8.5278, "Local Station", "S-Bahn, Bus, Bike-Share", 10000, "Low", "Full", 0, 1, 0, "Walk, Bikes", "Low", 0, "Local Station"),
    ("District 1 City Center", "Zürich 1 (City)", 47.3710, 8.5410, "Micro-hub", "Tram, Bus, Walk, Bike-Share", 30000, "Medium", "Full", 0, 1, 0, "Walk, Bikes, Scooters", "High", 0, "District Center"),
    ("District 2 Wollishofen Center", "Zürich 2 (Wollishofen/Leimbach/Enge)", 47.3552, 8.5327, "Micro-hub", "Tram, Bus, Bike-Share", 14000, "Medium", "Full", 0, 1, 1, "Bikes, Walk", "Medium", 0, "District Center"),
    ("District 3 Wiedikon Center", "Zürich 3 (Wiedikon)", 47.3708, 8.5189, "Micro-hub", "Tram, Bus, Bike-Share", 16000, "Medium", "Full", 0, 1, 1, "Scooters, Bikes", "Medium", 0, "District Center"),
    ("District 4 Aussersihl Center", "Zürich 4 (Aussersihl)", 47.3774, 8.5269, "Micro-hub", "Tram, Bus, Bike-Share", 20000, "Medium", "Full", 0, 1, 0, "Walk, Bikes", "Medium", 0, "District Center"),
    ("District 5 Industriequartier Center", "Zürich 5 (Industriequartier)", 47.3859, 8.5230, "Micro-hub", "Tram, Bus, Bike-Share, Car-Share", 22000, "Medium", "Full", 0, 1, 1, "Scooters, Bikes", "Medium", 0, "District Center"),
    ("District 6 Unterstrass Center", "Zürich 6 (Unterstrass/Oberstrass)", 47.3926, 8.5366, "Micro-hub", "Tram, Bus, Bike-Share", 15000, "Medium", "Full", 0, 1, 0, "Walk, Bikes", "Medium", 0, "District Center"),
    ("District 7 Fluntern Center", "Zürich 7 (Fluntern/Hottingen/Hirslanden)", 47.3788, 8.5660, "Micro-hub", "Tram, Bus, Bike-Share", 12000, "Low", "Partial", 0, 1, 0, "Walk, Bikes", "Low", 0, "District Center"),
    ("District 8 Riesbach Center", "Zürich 8 (Riesbach)", 47.3594, 8.5539, "Micro-hub", "Tram, Bus, Bike-Share", 14000, "Medium", "Full", 0, 1, 0, "Walk, Bikes", "Medium", 0, "District Center"),
    ("District 9 Altstetten Center", "Zürich 9 (Altstetten/Albisrieden)", 47.3913, 8.4849, "Micro-hub", "Tram, Bus, Bike-Share, Car-Share", 18000, "Medium", "Full", 1, 1, 1, "Scooters, Bikes, Walk", "Medium", 0, "District Center"),
    ("District 10 Wipkingen Center", "Zürich 10 (Wipkingen/Höngg)", 47.3981, 8.5217, "Micro-hub", "Bus, Tram, Bike-Share", 13000, "Medium", "Partial", 0, 1, 0, "Walk, Bikes", "Medium", 0, "District Center"),
    ("District 11 Affoltern Center", "Zürich 11 (Affoltern/Oerlikon/Seebach)", 47.4189, 8.5219, "Micro-hub", "Bus, Tram, Bike-Share", 15000, "Medium", "Full", 0, 1, 0, "Bikes, Walk", "Medium", 0, "District Center"),
    ("District 12 Schwamendingen Center", "Zürich 12 (Schwamendingen)", 47.4038, 8.5714, "Micro-hub", "Tram, Bus, Bike-Share", 17000, "Medium", "Full", 0, 1, 0, "Scooters, Walk", "Medium", 0, "District Center"),
    ("Wiedikon Bahnhofplatz", "Zürich 3 (Wiedikon)", 47.3702, 8.5194, "Micro-hub", "Tram, Bus, Bike-Share, Car-Share", 9000, "Low", "Full", 0, 1, 1, "Scooters, Bikes, Walk", "Medium", 0, "Micro Hub"),
    ("Hongg Meierhofplatz", "Zürich 10 (Wipkingen/Höngg)", 47.4042, 8.5049, "Micro-hub", "Tram, Bus, Bike-Share", 8000, "Low", "Partial", 0, 1, 0, "Walk, Bikes", "Low", 0, "Micro Hub"),
    ("Affoltern Zehntenhausplatz", "Zürich 11 (Affoltern/Oerlikon/Seebach)", 47.4183, 8.5124, "Micro-hub", "Bus, Bike-Share, Car-Share", 7000, "Low", "Full", 0, 1, 1, "Bikes, Walk, Car-Share", "Low", 0, "Micro Hub"),
    ("Schwamendingerplatz", "Zürich 12 (Schwamendingen)", 47.4061, 8.5752, "Micro-hub", "Tram, Bus, Bike-Share", 9500, "Low", "Full", 0, 1, 0, "Scooters, Walk", "Low", 0, "Micro Hub"),
    ("Altstetten Lindenplatz", "Zürich 9 (Altstetten/Albisrieden)", 47.3919, 8.4789, "Micro-hub", "Tram, Bus, Bike-Share, Car-Share", 11000, "Medium", "Full", 0, 1, 1, "Scooters, Bikes, Walk", "Medium", 0, "Micro Hub"),
    ("Wollishofen Bahnhof", "Zürich 2 (Wollishofen/Leimbach/Enge)", 47.3468, 8.5308, "Micro-hub", "S-Bahn, Tram, Bus, Bike-Share", 8500, "Low", "Full", 0, 1, 0, "Walk, Bikes", "Low", 0, "Micro Hub"),
    ("Glattpark", "Region (Glatt Valley)", 47.4224, 8.5634, "Interchange", "Tram, Bus, Bike-Share, Car-Share", 21000, "Medium", "Full", 1, 1, 1, "Scooters, Bikes, Walk", "Medium", 0, "Interchange Station"),
    ("Opfikon", "Region (Glatt Valley)", 47.4311, 8.5771, "Interchange", "S-Bahn, Bus, Car-Share", 26000, "Medium", "Full", 1, 0, 1, "Bus, Car-Share", "Medium", 1, "Regional Station"),
    ("Wallisellen", "Region (Glatt Valley)", 47.4145, 8.5967, "Interchange", "S-Bahn, Tram, Bus", 34000, "High", "Full", 1, 1, 1, "Bus, Bikes", "High", 1, "Regional Station"),
    ("Dietikon", "Region (Limmat Valley)", 47.4010, 8.3993, "Regional Hub", "S-Bahn, Bus, Car-Share", 42000, "High", "Full", 1, 0, 1, "Bus, Car-Share", "Medium", 1, "Regional Station"),
    ("Schlieren", "Region (Limmat Valley)", 47.3966, 8.4473, "Interchange", "S-Bahn, Bus, Bike-Share", 30000, "Medium", "Full", 1, 1, 1, "Bikes, Bus", "Medium", 0, "Regional Station"),
    ("Urdorf", "Region (Limmat Valley)", 47.3844, 8.4247, "Local Station", "S-Bahn, Bus", 12000, "Low", "Full", 1, 0, 0, "Bus, Walk", "Low", 0, "Regional Station"),
    ("Adliswil", "Region (Sihl Valley)", 47.3098, 8.5248, "Interchange", "S-Bahn, Bus, Bike-Share", 22000, "Medium", "Full", 1, 1, 1, "Bikes, Bus", "Medium", 0, "Regional Station"),
    ("Thalwil", "Region (Lake Zurich Left Bank)", 47.2962, 8.5646, "Regional Hub", "S-Bahn, Bus, Car-Share", 36000, "High", "Full", 1, 0, 1, "Bus, Car-Share", "Medium", 1, "Regional Station"),
    ("Kilchberg", "Region (Lake Zurich Left Bank)", 47.3239, 8.5488, "Local Station", "S-Bahn, Bus", 9000, "Low", "Partial", 0, 0, 0, "Walk, Bus", "Low", 0, "Regional Station"),
    ("Zollikon", "Region (Lake Zurich Right Bank)", 47.3407, 8.5756, "Local Station", "S-Bahn, Bus, Bike-Share", 10000, "Low", "Full", 0, 1, 0, "Walk, Bikes", "Low", 0, "Regional Station"),
    ("Dübendorf", "Region (Glatt Valley)", 47.3981, 8.6180, "Interchange", "S-Bahn, Bus, Car-Share", 28000, "Medium", "Full", 1, 0, 1, "Bus, Car-Share", "Medium", 0, "Regional Station"),
    ("Stettbach", "Region (Glatt Valley)", 47.3974, 8.6006, "Interchange", "S-Bahn, Tram, Bus, Bike-Share", 46000, "High", "Full", 1, 1, 1, "Scooters, Bikes, Bus", "High", 1, "Regional Station"),
    ("Regensdorf-Watt", "Region (Furttal)", 47.4342, 8.4701, "Interchange", "S-Bahn, Bus, Car-Share", 17000, "Medium", "Full", 1, 0, 1, "Bus, Car-Share", "Low", 0, "Regional Station"),
    ("Kloten", "Region (Glatt Valley)", 47.4512, 8.5862, "Interchange", "S-Bahn, Bus, Car-Share", 24000, "Medium", "Full", 1, 0, 1, "Bus, Car-Share", "Medium", 1, "Regional Station"),
]


def mk_node(t):
    return {
        "label": t[0],
        "id": slugify(t[0]),
        "type": t[15],
        "description": f"{t[0]} mobility node in the Zürich integrated urban transport network.",
        "district": t[1],
        "latitude": t[2],
        "longitude": t[3],
        "role": t[4],
        "primary_modes": t[5],
        "daily_users_estimate": t[6],
        "interchange_capacity": t[7],
        "accessibility": t[8],
        "has_parking": bool(t[9]),
        "has_bikeshare": bool(t[10]),
        "has_carshare": bool(t[11]),
        "first_mile_last_mile": t[12],
        "centrality": t[13],
        "is_regional_gateway": bool(t[14]),
        "tags": ["zurich-mobility", slugify(t[4]), slugify(t[7])],
    }


nodes = [mk_node(t) for t in base_nodes]
labels = {n["label"] for n in nodes}
connections = []


def add_connection(frm, to, type_, mode, frequency_per_hour, estimated_daily_volume, capacity_utilization, avg_travel_time_minutes, reliability_score, requires_transfer, route_name, operator, is_bottleneck, is_key_corridor, resilience_importance, tags, direction="undirected"):
    connections.append(
        {
            "from": frm,
            "to": to,
            "id": f"{slugify(frm)}-{slugify(to)}-{slugify(mode)}-{len(connections) + 1}",
            "type": type_,
            "mode": mode,
            "frequency_per_hour": frequency_per_hour,
            "direction": direction,
            "estimated_daily_volume": estimated_daily_volume,
            "capacity_utilization": capacity_utilization,
            "avg_travel_time_minutes": avg_travel_time_minutes,
            "reliability_score": reliability_score,
            "requires_transfer": requires_transfer,
            "route_name": route_name,
            "operator": operator,
            "is_bottleneck": is_bottleneck,
            "is_key_corridor": is_key_corridor,
            "resilience_importance": resilience_importance,
            "tags": tags,
        }
    )


def fill_connections():
    sbahn_pairs = [
        ("Zürich HB", "Zürich Hardbrücke"), ("Zürich Hardbrücke", "Zürich Altstetten"), ("Zürich HB", "Stadelhofen"), ("Stadelhofen", "Zürich Tiefenbrunnen"),
        ("Zürich Tiefenbrunnen", "Zollikon"), ("Zürich HB", "Zürich Oerlikon"), ("Zürich Oerlikon", "Zürich Flughafen"), ("Zürich Oerlikon", "Zürich Seebach"),
        ("Zürich Oerlikon", "Wallisellen"), ("Wallisellen", "Stettbach"), ("Stettbach", "Dübendorf"), ("Zürich HB", "Zürich Wiedikon"),
        ("Zürich Wiedikon", "Zürich Enge"), ("Zürich Enge", "Zürich Wollishofen"), ("Zürich Wollishofen", "Kilchberg"), ("Kilchberg", "Thalwil"),
        ("Zürich Wiedikon", "Zürich Giesshübel"), ("Zürich Giesshübel", "Zürich Binz"), ("Zürich Binz", "Zürich Leimbach"), ("Zürich Leimbach", "Adliswil"),
        ("Zürich Altstetten", "Schlieren"), ("Schlieren", "Dietikon"), ("Schlieren", "Urdorf"), ("Zürich Oerlikon", "Opfikon"), ("Opfikon", "Kloten"),
        ("Kloten", "Zürich Flughafen"), ("Zürich Altstetten", "Regensdorf-Watt"), ("Regensdorf-Watt", "Zürich Affoltern"), ("Zürich Affoltern", "Zürich Oerlikon"),
        ("Stadelhofen", "Zürich Oerlikon"),
    ]
    for i, (frm, to) in enumerate(sbahn_pairs):
        add_connection(frm, to, "Direct Transit", "S-Bahn", 6 if i < 10 else 4 if i < 26 else 3, max(9000, 62000 - i * 1700), min(0.92, 0.86 - (i % 5) * 0.05 + 0.1), 3 + (i % 7), 0.94 - (i % 4) * 0.02, False, "S-Bahn corridor service", "SBB", i in {0, 1, 2, 5}, True, "Critical" if i < 6 else "High", ["main-corridor", "peak-hour-stress"] if i < 6 else ["s-bahn-link"])

    tram_pairs = [
        ("Zürich Altstetten", "Zürich Albisrieden"), ("Zürich Albisrieden", "Zürich Wiedikon"), ("Zürich Wiedikon", "Zürich Paradeplatz"), ("Zürich Paradeplatz", "Zürich Bellevue"),
        ("Zürich Bellevue", "Stadelhofen"), ("Stadelhofen", "Zürich Tiefenbrunnen"), ("Zürich HB", "Zürich Central"), ("Zürich Central", "Zürich Bellevue"),
        ("Zürich Central", "District 6 Unterstrass Center"), ("District 6 Unterstrass Center", "Zürich Oerlikon"), ("Zürich Oerlikon", "Glattpark"), ("Glattpark", "Zürich Flughafen"),
        ("Zürich Oerlikon", "District 11 Affoltern Center"), ("District 11 Affoltern Center", "Affoltern Zehntenhausplatz"), ("Zürich Oerlikon", "District 12 Schwamendingen Center"),
        ("District 12 Schwamendingen Center", "Schwamendingerplatz"), ("Schwamendingerplatz", "Stettbach"), ("Zürich Hardbrücke", "Zürich Escher-Wyss-Platz"),
        ("Zürich Escher-Wyss-Platz", "District 5 Industriequartier Center"), ("District 5 Industriequartier Center", "District 4 Aussersihl Center"), ("District 4 Aussersihl Center", "Zürich HB"),
        ("Zürich Enge", "District 2 Wollishofen Center"), ("District 2 Wollishofen Center", "Wollishofen Bahnhof"), ("Wollishofen Bahnhof", "Zürich Wollishofen"),
        ("District 3 Wiedikon Center", "Wiedikon Bahnhofplatz"), ("Wiedikon Bahnhofplatz", "Zürich Triemli"), ("District 10 Wipkingen Center", "Hongg Meierhofplatz"),
        ("Hongg Meierhofplatz", "Zürich Escher-Wyss-Platz"),
    ]
    for i, (frm, to) in enumerate(tram_pairs):
        add_connection(frm, to, "Direct Transit", "Tram", 8 if i < 12 else 6, max(7000, 34000 - i * 900), min(0.9, 0.82 - (i % 6) * 0.04 + 0.08), 4 + (i % 6), 0.92 - (i % 4) * 0.02, False, "Tram corridor service", "VBZ", i in {2, 3, 4, 6, 7}, True, "High", ["tram-spine"])

    bus_pairs = [
        ("Zürich HB", "District 4 Aussersihl Center"), ("District 4 Aussersihl Center", "Zürich Hardbrücke"), ("Zürich Hardbrücke", "Zürich Oerlikon"), ("Zürich Oerlikon", "District 12 Schwamendingen Center"),
        ("District 12 Schwamendingen Center", "Dübendorf"), ("Zürich HB", "District 1 City Center"), ("District 1 City Center", "Zürich Bellevue"), ("Zürich Bellevue", "District 8 Riesbach Center"),
        ("District 8 Riesbach Center", "Zürich Tiefenbrunnen"), ("Zürich Enge", "District 2 Wollishofen Center"), ("District 2 Wollishofen Center", "Adliswil"), ("Zürich Wiedikon", "District 3 Wiedikon Center"),
        ("District 3 Wiedikon Center", "Zürich Sihlcity Nord"), ("Zürich Altstetten", "District 9 Altstetten Center"), ("District 9 Altstetten Center", "Altstetten Lindenplatz"), ("Altstetten Lindenplatz", "Schlieren"),
        ("District 10 Wipkingen Center", "Zürich HB"), ("District 11 Affoltern Center", "Zürich Affoltern"), ("Affoltern Zehntenhausplatz", "Zürich Affoltern"), ("Glattpark", "Opfikon"),
        ("Opfikon", "Kloten"), ("Wallisellen", "Dübendorf"),
    ]
    for i, (frm, to) in enumerate(bus_pairs):
        add_connection(frm, to, "Direct Transit", "Bus", 7 if i < 6 else 5, max(5000, 18000 - i * 500), min(0.82, 0.74 - (i % 5) * 0.06 + 0.06), 6 + (i % 6), 0.86 - (i % 4) * 0.02, False, "Bus backbone service", "VBZ", i == 2, True, "Medium", ["bus-backbone"])

    integration_pairs = [
        ("Zürich HB", "District 1 City Center"), ("Zürich HB", "Zürich Central"), ("Stadelhofen", "Zürich Bellevue"), ("Zürich Oerlikon", "Glattpark"),
        ("Zürich Altstetten", "Altstetten Lindenplatz"), ("Zürich Wiedikon", "Wiedikon Bahnhofplatz"), ("Zürich Hardbrücke", "District 5 Industriequartier Center"),
        ("District 12 Schwamendingen Center", "Schwamendingerplatz"), ("District 11 Affoltern Center", "Affoltern Zehntenhausplatz"), ("Zürich Enge", "District 2 Wollishofen Center"),
        ("Stettbach", "District 12 Schwamendingen Center"), ("Wallisellen", "Glattpark"),
    ]
    for i, (frm, to) in enumerate(integration_pairs):
        add_connection(frm, to, "Integration", "Multi-modal", 2, max(2800, 9000 - i * 450), min(0.7, 0.62 - (i % 4) * 0.06 + 0.06), 5 + (i % 5), 0.9 - (i % 3) * 0.02, True, "Integrated transfer link", "Zurich Transport", i in {1, 2}, False, "Medium", ["integration", "first-mile"])

    infrastructure_pairs = [
        ("Zürich HB", "Zürich Paradeplatz"), ("Zürich Paradeplatz", "District 1 City Center"), ("Zürich Bellevue", "District 8 Riesbach Center"), ("Zürich Hardbrücke", "Zürich Escher-Wyss-Platz"),
        ("Zürich Wiedikon", "Zürich Sihlcity Nord"), ("Zürich Oerlikon", "District 11 Affoltern Center"), ("Stadelhofen", "District 7 Fluntern Center"), ("Zürich Altstetten", "District 10 Wipkingen Center"),
    ]
    for i, (frm, to) in enumerate(infrastructure_pairs):
        add_connection(frm, to, "Infrastructure", "Multi-modal", 2 if i < 6 else 1, max(2000, 14000 - i * 1300), min(0.75, 0.69 - i * 0.05), 7 + i, 0.93 - i * 0.01, True, "Active mobility access corridor", "Zurich Transport", False, i in {0, 3}, "High" if i < 2 else "Medium" if i < 6 else "Low", ["infrastructure", "resilience"])


fill_connections()

assert len(nodes) == 54, f"Expected 54 nodes, got {len(nodes)}"
assert len(connections) == 100, f"Expected 100 connections, got {len(connections)}"
assert len(labels) == len(nodes)
for node in nodes:
    assert 47.29 <= node["latitude"] <= 47.46
    assert 8.39 <= node["longitude"] <= 8.62
for connection in connections:
    assert connection["from"] in labels and connection["to"] in labels
    assert 0 <= connection["capacity_utilization"] <= 1
    assert 0 <= connection["reliability_score"] <= 1

output = {"elements": nodes, "connections": connections}
output_path = DATA_DIR / "zurich_mobility_system.json"
output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {output_path} with {len(nodes)} elements and {len(connections)} connections")
