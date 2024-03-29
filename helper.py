
class Offsets:
    gom_offset = 0x17FFD28
    active_node = 0x20
    active_node_ptr = 0x10
    lgw_ptrchain = [0x30, 0x18, 0x28]
    reg_players = 0x90
    reg_player_count = 0x18
    playerbase_profile = 0x4B8
    playerbase_movement_context = 0x40
    playerbase_is_local_Player = 0x7F7
    movement_context_direction = 0x22C
    transform_transform_internal = [0xA8, 0x28, 0x28, 0x10, 0x20, 0x10]
    transform_internal_transfpmatrix = 0x38
    transfpmatrix_transform_dependency_index_table_base = 0x20
    health_entry = 0x10
    health_entry_value = 0x10
    player_profile_player_id = 0x10
    player_profile_player_info = 0x28
    player_info_player_name = 0x10
    player_info_experience = 0x74
    player_info_playerside = 0x58
    player_info_regdate = 0x5c
    unity_dict_base = 0x18
    playerbase_healthcontroller = [0x4F0, 0x50, unity_dict_base]
    unity_list_base = 0x10
    unity_list_base_start = 0x20
    unity_string_len = 0x10
    unity_string_value = 0x14
    unity_object_name = 0x60

    # Loot
    LOOT_LIST = 0x60
    LOOT_LIST_ENTITY = 0x10
    LOOT_LIST_COUNT = 0x18
    LOOT_OBJECTS_ENTITY_BASE = 0x20
    UNKNOWN_PTR = 0x10
    INTERACTIVE_CLASS = 0x28
    BASE_OBJECT = 0x10
    GAME_OBJECT = 0x30
    GAME_OBJECT_NAME_PTR = 0x60
    CONTAINERS = ["body", 
                  "XXXcap", 
                  "Ammo_crate_Cap", 
                  "Grenade_box_Door", 
                  "Medical_Door", 
                  "Toolbox_Door", 
                  "card_file_box",
                  "cover_",
                  "lootable",
                  "scontainer_Blue_Barrel_Base_Cap",
                  "scontainer_wood_CAP",
                  "suitcase_plastic_lootable_open",
                  "weapon_box_cover"]

# Experience Table

    EXP_TABLE = {0: 1,
                1000: 2,
                4017: 3,
                8432: 4,
                14256: 5,
                21477: 6,
                30023: 7,
                39936: 8,
                51204: 9,
                63723: 10,
                77563: 11,
                92713: 12,
                111881: 13,
                134674: 14,
                161139: 15,
                191417: 16,
                225194: 17,
                262366: 18,
                302484: 19,
                345751: 20,
                391649: 21,
                440444: 22,
                492366: 23,
                547896: 24,
                609066: 25,
                675913: 26,
                748474: 27,
                826786: 28,
                910885: 29,
                1000809: 30,
                1096593: 31,
                1198275: 32,
                1309251: 33,
                1429580: 34,
                1559321: 35,
                1698532: 36,
                1847272: 37,
                2005600: 38,
                2173575: 39,
                2351255: 40,
                2538699: 41,
                2735966: 42,
                2946585: 43,
                3170637: 44,
                3408202: 45,
                3659361: 46,
                3924195: 47,
                4202784: 48,
                4495210: 49,
                4801553: 50,
                5121894: 51,
                5456314: 52,
                5809667: 53,
                6182063: 54,
                6573613: 55,
                6984426: 56,
                7414613: 57,
                7864284: 58,
                8333549: 59,
                8831052: 60,
                9360623: 61,
                9928578: 62,
                10541848: 63,
                11206300: 64,
                11946977: 65,
                12789143: 66,
                13820522: 67,
                15229487: 68,
                17206065: 69,
                19706065: 70,
                22706065: 71,
                26206065: 72,
                30206065: 73,
                34706065: 74,
                39706065: 75}
    