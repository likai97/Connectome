"""
Reorders connectivity matrices on the basis of the yeo7 network
"""
import numpy as np
import pandas as pd


def reorder_matrices_regions(matrices: list, network: str = 'yeo7') -> np.ndarray:
    """
    Reorders connectivity matrix according to network regions


    Args:
        matrices: list of connectvity Matrices
        network: Yeo7 or Yeo17 network

    Returns:
        List of reordered connectvity Matrices
    """

    assert isinstance(network, str) & (network == "yeo7" or network == "yeo17"), "invalid network"

    lab_to_yeo7 = {'1': '6', '2': '4', '3': '7', '4': '6', '5': '7', '6': '7', '7': '3', '8': '3', '9': '2', '10': '2',
                   '11': '7', '12': '6', '13': '7', '14': '7', '15': '4', '16': '6', '17': '6', '18': '6', '19': '6',
                   '20': '6', '21': '6', '22': '6', '23': '7', '24': '6', '25': '3', '26': '3', '27': '5', '28': '6',
                   '29': '6', '30': '3', '31': '6', '32': '6', '33': '7', '34': '7', '35': '7', '36': '6', '37': '4',
                   '38': '4', '39': '4', '40': '4', '41': '7', '42': '7', '43': '7', '44': '7', '45': '5', '46': '6',
                   '47': '5', '48': '5', '49': '5', '50': '5', '51': '7', '52': '7', '53': '2', '54': '2', '55': '3',
                   '56': '3', '57': '2', '58': '2', '59': '2', '60': '2', '61': '4', '62': '4', '63': '3', '64': '3',
                   '65': '4', '66': '2', '67': '2', '68': '2', '69': '5', '70': '5', '71': '2', '72': '2', '73': '2',
                   '74': '2', '75': '2', '76': '2', '77': '5', '78': '5', '79': '7', '80': '7', '81': '7', '82': '6',
                   '83': '7', '84': '7', '85': '3', '86': '3', '87': '7', '88': '7', '89': '5', '90': '5', '91': '3',
                   '92': '3', '93': '5', '94': '5', '95': '7', '96': '5', '97': '3', '98': '3', '99': '6', '100': '6',
                   '101': '5', '102': '5', '103': '5', '104': '5', '105': '1', '106': '1', '107': '3', '108': '1',
                   '109': '5', '110': '5', '111': '5', '112': '1', '113': '1', '114': '1', '115': '5', '116': '5',
                   '117': '5', '118': '5', '119': '1', '120': '1', '121': '7', '122': '7', '123': '4', '124': '4',
                   '125': '3', '126': '3', '127': '3', '128': '3', '129': '3', '130': '3', '131': '2', '132': '2',
                   '133': '3', '134': '3', '135': '1', '136': '1', '137': '6', '138': '6', '139': '3', '140': '3',
                   '141': '7', '142': '6', '143': '3', '144': '7', '145': '2', '146': '2', '147': '6', '148': '6',
                   '149': '2', '150': '3', '151': '1', '152': '1', '153': '7', '154': '7', '155': '2', '156': '2',
                   '157': '2', '158': '2', '159': '3', '160': '2', '161': '2', '162': '2', '163': '2', '164': '2',
                   '165': '0', '166': '6', '167': '4', '168': '4', '169': '4', '170': '4', '171': '2', '172': '2',
                   '173': '4', '174': '4', '175': '7', '176': '7', '177': '0', '178': '0', '179': '7', '180': '4',
                   '181': '7', '182': '1', '183': '4', '184': '4', '185': '4', '186': '4', '187': '7', '188': '7',
                   '189': '1', '190': '1', '191': '1', '192': '1', '193': '1', '194': '1', '195': '1', '196': '1',
                   '197': '1', '198': '1', '199': '1', '200': '1', '201': '3', '202': '1', '203': '1', '204': '1',
                   '205': '1', '206': '1', '207': '1', '208': '1', '209': '1', '210': '1', '211': '0', '212': '0',
                   '213': '0', '214': '0', '215': '0', '216': '0', '217': '0', '218': '0', '219': '0', '220': '0',
                   '221': '0', '222': '0', '223': '0', '224': '0', '225': '0', '226': '0', '227': '0', '228': '0',
                   '229': '0', '230': '0', '231': '0', '232': '0', '233': '0', '234': '0', '235': '0', '236': '0',
                   '237': '0', '238': '0', '239': '0', '240': '0', '241': '0', '242': '0', '243': '0', '244': '0',
                   '245': '0', '246': '0'}
    lab_to_yeo17 = {'1': '17', '2': '8', '3': '16', '4': '13', '5': '17', '6': '17', '7': '6', '8': '6', '9': '3',
                    '10': '3', '11': '13', '12': '13', '13': '16', '14': '16', '15': '8', '16': '11', '17': '12',
                    '18': '12', '19': '13', '20': '13', '21': '12', '22': '8', '23': '16', '24': '13', '25': '6',
                    '26': '12', '27': '10', '28': '13', '29': '12', '30': '12', '31': '12', '32': '12', '33': '17',
                    '34': '17', '35': '17', '36': '8', '37': '7', '38': '8', '39': '8', '40': '8', '41': '16',
                    '42': '16',
                    '43': '17', '44': '17', '45': '10', '46': '12', '47': '10', '48': '10', '49': '10', '50': '10',
                    '51': '17', '52': '17', '53': '4', '54': '4', '55': '6', '56': '6', '57': '3', '58': '3', '59': '3',
                    '60': '3', '61': '7', '62': '7', '63': '12', '64': '12', '65': '7', '66': '3', '67': '3', '68': '3',
                    '69': '9', '70': '9', '71': '4', '72': '4', '73': '4', '74': '4', '75': '14', '76': '4', '77': '9',
                    '78': '9', '79': '14', '80': '17', '81': '17', '82': '13', '83': '17', '84': '17', '85': '6',
                    '86': '6',
                    '87': '17', '88': '14', '89': '9', '90': '9', '91': '5', '92': '5', '93': '9', '94': '9',
                    '95': '17',
                    '96': '17', '97': '12', '98': '5', '99': '13', '100': '13', '101': '9', '102': '9', '103': '9',
                    '104': '9', '105': '1', '106': '1', '107': '5', '108': '5', '109': '9', '110': '9', '111': '15',
                    '112': '15', '113': '15', '114': '15', '115': '9', '116': '9', '117': '9', '118': '9', '119': '2',
                    '120': '2', '121': '14', '122': '14', '123': '14', '124': '14', '125': '6', '126': '6', '127': '5',
                    '128': '5', '129': '6', '130': '6', '131': '3', '132': '3', '133': '5', '134': '5', '135': '5',
                    '136': '5', '137': '12', '138': '12', '139': '6', '140': '6', '141': '17', '142': '13', '143': '14',
                    '144': '16', '145': '4', '146': '4', '147': '11', '148': '11', '149': '3', '150': '6', '151': '2',
                    '152': '2', '153': '16', '154': '16', '155': '4', '156': '4', '157': '4', '158': '4', '159': '6',
                    '160': '3', '161': '3', '162': '3', '163': '4', '164': '4', '165': '0', '166': '8', '167': '8',
                    '168': '8', '169': '7', '170': '7', '171': '4', '172': '4', '173': '7', '174': '7', '175': '16',
                    '176': '16', '177': '0', '178': '0', '179': '16', '180': '8', '181': '15', '182': '15', '183': '7',
                    '184': '7', '185': '8', '186': '7', '187': '16', '188': '16', '189': '1', '190': '1', '191': '2',
                    '192': '2', '193': '1', '194': '1', '195': '2', '196': '1', '197': '2', '198': '2', '199': '1',
                    '200': '1', '201': '5', '202': '5', '203': '1', '204': '1', '205': '1', '206': '1', '207': '2',
                    '208': '2', '209': '1', '210': '5', '211': '0', '212': '0', '213': '0', '214': '0', '215': '0',
                    '216': '0', '217': '0', '218': '0', '219': '0', '220': '0', '221': '0', '222': '0', '223': '0',
                    '224': '0', '225': '0', '226': '0', '227': '0', '228': '0', '229': '0', '230': '0', '231': '0',
                    '232': '0', '233': '0', '234': '0', '235': '0', '236': '0', '237': '0', '238': '0', '239': '0',
                    '240': '0', '241': '0', '242': '0', '243': '0', '244': '0', '245': '0', '246': '0'}

    if network == 'yeo7':
        sorted_keys = list(dict(sorted(lab_to_yeo7.items(), key=lambda item: item[1])).keys())
        sorted_keys_int = list(map(int, sorted_keys))
        order = [x - 1 for x in sorted_keys_int]
    elif network == 'yeo17':
        sorted_keys = list(dict(sorted(lab_to_yeo17.items(), key=lambda item: item[1])).keys())
        sorted_keys_int = list(map(int, sorted_keys))
        order = [x - 1 for x in sorted_keys_int]

    ordered_conn_mat = []
    for conn_mat in matrices:
        assert isinstance(conn_mat, (np.ndarray, np.generic)), "provided matrix is not an ndarray"

        mat = pd.DataFrame(conn_mat)

        ordered_mat = mat.reindex(index=order, columns=order).to_numpy()

        ordered_conn_mat.append(ordered_mat)

    return ordered_conn_mat
