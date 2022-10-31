data = {
    'genstats': {
        'player_side': ('Tribune', 0),
        'start': ('Début', 0),
        'position': ('Pos', 0),
        'minutes': ('Min', 0),
        'buts': ('Buts', 0),
        'pd': ('PD', 0),
        'penm': ('PénM', 0),
        'pent': ('PénT', 0),
        'tirs': ('Tirs', 0),
        'tc': ('TC', 0),
        'cj': ('CJ', 0),
        'cr': ('CR', 0),
        'touches': ('Touches', 0),
        'tcl': ('Tcl', 0),
        'balcontr': ('Balles contrées', 0),
        'inter': ('Int', 0),
        'amt': ('AMT', 0),
        'amb': ('AMB', 0),
        'pr': ('Cmp', 0),
        'attp': ('Att', 0),
        'tpr': ('Cmp%', 0),
        'pva': ('Prog', 0),
        'dr': ('Réussi', 0),
        'attd': ('Tenté', 0),
        'xg': ('xG', 0),
        'npxg': ('npxG', 0),
        'xat': ('xAG', 0)
    },
    'passes': {
        'totdist': ('TotDist', 0),
        'distbut': ('DistBut', 0),
        'shortpr': ('Cmp', 0),
        'shortattp': ('Att', 0),
        'shorttpr': ('Cmp%', 0),
        'midpr': ('Cmp', 1),
        'midattp': ('Att', 1),
        'midtpr': ('Cmp%', 1),
        'longpr': ('Cmp', 2),
        'longattp': ('Att', 2),
        'longtpr': ('Cmp%', 2),
        'xa': ('xA', 0),
        'ptirs': ('PC', 0),
        'p1_3': ('1/3', 0),
        'p16_5': ('PPA', 0),
        'cnt16r': ('CntSR', 0)
    },
    'passes-type': {
        'adjeu': ('Action de jeu', 0),
        'cparr': ('Coup de pied arrêté', 0),
        'trdef_att': ('Tr', 0),
        'tr40_larg': ('Tr', 1),
        'ctr': ('Ctr', 0),
        'pcf': ('PCF', 0),
        'corn': ('Co', 0),
        'corn_rent': ('Rentrant', 0),
        'corn_sort': ('Sortant', 0),
        'corn_droit': ('Droit', 0),
        'pcont': ('Balles contrées', 0)
    },
    'penalty-prep': {
        'pjeu_amt': ('PassJeu', 0),
        'pcparr_amt': ('PassArr', 0),
        'drib_amt': ('Drib', 0),
        'tirs_amt': ('Tirs', 0),
        'faut_amt': ('Ftp', 0),
        'def_amt': ('Déf', 0),
        'pjeu_amd': ('PassJeu', 1),
        'pcparr_amd': ('PassArr', 1),
        'drib_amd': ('Drib', 1),
        'tirs_amd': ('Tirs', 1),
        'faut_amd': ('Ftp', 1),
        'def_amd': ('Déf', 1)
    },
    'defensive-actions': {
        'tclr': ('TclR', 0),
        'tcl_zdef': ('ZDéf', 0),
        'tcl_mid': ('MilTer', 0),
        'tcl_zoff': ('ZOff', 0),
        'tcl_drib': ('Tcl', 0),
        'tcl_dribatt': ('Tenté', 0),
        'tcl_dribfail': ('Passé', 0),
        'tcl_dribrate': ('Tcl%', 0),
        'tirs_contr': ('Tirs', 0),
        'p_contr': ('Passe', 0),
        'tclxint': ('Tcl+Int', 0),
        'deg': ('Dég', 0),
        'err': ('Err', 0)
    },
    'possession': {
        'touch_surfr_def': ('SurfRépDéf', 0),
        'touch_zonedef': ('ZDéf', 0),
        'touch_mid': ('MilTer', 0),
        'touch_zoneoff': ('ZOff', 0),
        'touch_surfr_off': ('SurfRépOff', 0),
        'touch_ajeu': ('Action de jeu', 0),
        'drib_att': ('Tenté', 0),
        'drib_reu': ('Réussi', 0),
        'drib_treu': ('Réussi%', 0),
        'drib_manq': ('Manqué', 0),
        'drip_pert': ('Perte', 0),
        'recus': ('Rec', 0),
        'recus_pavant': ('Prog', 0)
    },
    'various-stats': {
        'cj_deu': ('2CrtJ', 0),
        'fte': ('Fte', 0),
        'fte_pro': ('Ftp', 0),
        'hj': ('HJ', 0),
        'ctr': ('Ctr', 0),
        'pen_con': ('Pcon', 0),
        'csc': ('CSC', 0),
        'recup': ('Récupération', 0),
        'daer_gagn': ('Gagnés', 0),
        'daer_perd': ('Perdus', 0)
    },
    'keeper': {
        'tc_recus': ('TCC', 0),
        'be': ('BE', 0),
        'arrets': ('Arrêts', 0),
        'tarrets': ('Arrêts%', 0),
        'butsptxg': ('PSxG', 0),
        'pen_tirs': ('PénT', 0),
        'pen_con': ('Pc', 0),
        'pen_arr': ('Pa', 0),
        'pen_marq': ('Pm', 0),
        'deg_reu': ('Cmp', 0),
        'deg_att': ('Att', 0),
        'tdeg_reu': ('Cmp%', 0),
        'passes': ('Att', 1),
        'lanc_att': ('Lanc', 0),
        'pass_sup35': ('% de lancement', 0),
        'pass_lmoy': ('LongMoy', 0),
        'sixm_att': ('Att', 2),
        'sixm_sup35':( '% de lancement', 1),
        'sixm_lmoy': ('LongMoy', 1),
        'ctr_adv': ('Adv', 0),
        'ctr_stop': ('Stp', 0),
        'ctr_tstop': ('Stp%', 0),
        'int_horssup':( '#ESR', 0),
        'dist_but_moy': ('DistMoy', 0),
        'cs': ('CS', 0)
    }
}

def get_map_columns(type):
    return data[type]