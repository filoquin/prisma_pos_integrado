plots = {
    'TES': {
        'name': 'Test',
        'method': 'pos_execute',
        'cmd': 'TES',
        'cmd_args': [
        ],
        'res_start': 5,
        'send_param_len': False,

        'res_matrix':  [
        ]
    },
    'IMT': {
        'name': 'Reimpresion ultima transaccion',
        'method': 'pos_execute',
        'cmd': 'IMT',
        'cmd_args': [
        ],
        'res_start': 5,
        'send_param_len': False,

        'res_matrix':  [
        ]
    },
    'IMC': {
        'name': 'Reimpresion ultimo cierre',
        'method': 'pos_execute',
        'cmd': 'IMC',
        'cmd_args': [
        ],
        'res_start': 5,
        'send_param_len': False,

        'res_matrix':  [
        ]
    },
    'VEN': {
        'name': 'Venta',
        'method': 'pos_execute',
        'cmd': 'VEN',
        'cmd_args': [
            ('amount', 'N', '{:0>12d}'),
            ('invoice', 'N', '{:0>12d}'),
            ('instaments', 'N', '{:0>2d}'),
            ('card_code', 'N', '{:0>3}'),
            ('plan', 'N', '{:>1d}'),
            ('tip', 'N', '{:0>12d}'),
            ('commerce', 'N', '{:>15}'),
            ('commerce_name', 'A', '{:<23}'),
            ('cuit', 'A', '{:<23}'),
            ('line_mode', 'A', '{}'),
        ],
        'res_start': 10,
        'send_param_len': True,
        'res_matrix':  [
            ('res_code', 0, 2, 'N'),
            ('res_msg', 2, 32, 'A'),
            ('auth_code', 34, 6, 'N'),
            ('coupon', 40, 7, 'N'),
            ('lot', 47, 3, 'N'),
            ('name', 50, 26, 'A'),
            ('last_digits', 76, 4, 'A'),
            ('first_digits', 80, 6, 'A'),
            ('date', 86, 10, 'A'),
            ('time', 96, 8, 'A'),
            ('terminal_id', 104, 1, 'N'),
        ]
    },
    'ANV': {
        'name': 'Anulación de Venta',
        'method': 'pos_execute',
        'cmd': 'ANV',
        'cmd_args': [
            ('coupon', 'N', '{:0>7d}'),
            ('card_code', 'N', '{:0>3}'),
        ],
        'res_start': 5,
        'send_param_len': False,
        'res_matrix':  [
            ('res_code', 0, 2, 'N'),
            ('res_msg', 2, 32, 'A'),
            ('auth_code', 34, 6, 'N'),
            ('ticket', 40, 7, 'N'),
            ('lot', 47, 3, 'N'),
            ('name', 50, 26, 'A'),
            ('first_digits', 76, 6, 'A'),
            ('last_digits', 82, 4, 'A'),
            ('date', 86, 10, 'A'),
            ('time', 96, 8, 'A'),
            ('terminal_id', 104, 8, 'N'),
        ]
    },
    'DEV': {
        'name': 'Devolución',
        'method': 'pos_execute',
        'cmd': 'DEV',
        'cmd_args': [
            ('amount', 'N', '{:0>12d}'),
            ('card_code', 'N', '{:0>3}'),
            ('plan', 'N', '{:>1d}'),
            ('instaments', 'N', '{:0>2d}'),
            ('coupon', 'N', '{:0>7d}'),
            ('date', 'A', '{:<12}'),
            ('invoice', 'N', '{:0>12d}'),
            ('commerce', 'N', '{:>15}'),
            ('commerce_name', 'A', '{:<23}'),
            ('cuit', 'A', '{:<23}'),
            ('line_mode', 'A', '{}'),
        ],
        'res_start': 5,
        'send_param_len': False,
        'res_matrix':  [
            ('res_code', 0, 2, 'N'),
            ('res_msg', 2, 32, 'A'),
            ('auth_code', 34, 6, 'N'),
            ('ticket', 40, 7, 'N'),
            ('lot', 47, 3, 'N'),
            ('name', 50, 26, 'A'),
            ('first_digits', 76, 6, 'A'),
            ('last_digits', 82, 4, 'A'),
            ('date', 86, 10, 'A'),
            ('time', 96, 8, 'A'),
            ('terminal_id', 104, 8, 'N'),
        ]
    },
    'AND': {
        'name': 'Anulación de Devolución',
        'method': 'pos_execute',
        'cmd': 'AND',
        'cmd_args': [
            ('coupon', 'N', '{:0>7d}'),
            ('card_code', 'N', '{:0>3}'),
        ],
        'res_start': 5,
        'send_param_len': False,
        'res_matrix':  [
            ('res_code', 0, 2, 'N'),
            ('res_msg', 2, 32, 'A'),
            ('auth_code', 34, 6, 'N'),
            ('ticket', 40, 7, 'N'),
            ('lot', 47, 3, 'N'),
            ('name', 50, 26, 'A'),
            ('first_digits', 76, 6, 'A'),
            ('last_digits', 82, 4, 'A'),
            ('date', 86, 10, 'A'),
            ('time', 96, 8, 'A'),
            ('terminal_id', 104, 8, 'N'),
        ]
    },
    'ULT': {
        'name': 'Última transacción',
        'method': 'pos_execute',
        'cmd': 'ULT',
        'cmd_args': [
        ],
        'res_start': 10,

        'res_matrix':  [
            ('type', 0, 1, 'N'),
            ('res_code', 1, 2, 'N'),
            ('res_msg', 3, 32, 'A'),
            ('auth_code', 35, 6, 'N'),
            ('ticket', 41, 7, 'N'),
            ('lot', 48, 3, 'N'),
            ('name', 51, 26, 'A'),
            ('first_digits', 77, 6, 'A'),
            ('last_digits', 83, 4, 'A'),
            ('date', 87, 10, 'A'),
            ('time', 97, 8, 'A'),
            ('terminal_id', 105, 8, 'N'),
        ]
    },
    'ULC': {
        'name': 'Último Cierre',
        'method': 'pos_execute',
        'cmd': 'ULC',
        'cmd_args': [
            ('index', 'N', '{:0>4}'),
        ],
        'res_start': 10,        
        'res_matrix':  [
            ('index', 0, 4, 'N'),
            ('pros_code', 4, 3, 'A'),
            ('lot', 7, 3, 'N'),
            ('card_code', 10, 3, 'A'),
            ('sale_quant', 13, 4, 'N'),
            ('sale_amount', 17, 12, 'N'),
            ('void_quant', 29, 4, 'N'),
            ('void_amount', 33, 12, 'N'),
            ('dev_quant', 45, 4, 'n'),
            ('dev_amount', 49, 12, 'N'),
            ('an_dev_quant', 61, 4, 'N'),
            ('an_dev_amount', 65, 12, 'N'),
            ('date', 77, 10, 'A'),
            ('time', 87, 8, 'A'),
            ('terminal_id', 95, 8, 'N'),
        ]
    },
    'UvC': {
        'name': 'Último Commando',
        'method': 'pos_execute',
        'cmd': 'ULC',
        'cmd_args': [
            ('index', 'N', '{:0>4}'),
        ],
        'res_start': 5,        
        'res_matrix':  [
            ('index', 0, 4, 'N'),
            ('type', 0, 1, 'N'),
            ('res_code', 1, 2, 'N'),
            ('res_msg', 3, 32, 'A'),
            ('auth_code', 35, 6, 'N'),
            ('ticket', 41, 7, 'N'),
            ('lot', 48, 3, 'N'),
            ('name', 51, 26, 'A'),
            ('first_digits', 77, 6, 'A'),
            ('last_digits', 83, 4, 'A'),
            ('date', 87, 10, 'A'),
            ('time', 97, 8, 'A'),
            ('terminal_id', 105, 8, 'N'),
        ]
    },
    'CIE': {
        'name': 'Cierre',
        'method': 'pos_execute',
        'cmd': 'CIE',
        'cmd_args': [
        ],
        'send_param_len': True,
        'res_start': 10,

        'res_matrix':  [
            ('res_code', 0, 2, 'N'),
            ('date', 2, 10, 'A'),
            ('time', 12, 8, 'A'),
            ('terminal_id', 20, 8, 'N'), ]
    },
    'TAR': {
        'method': 'pos_execute',
        'cmd': 'TAR',
        'cmd_args': [
            ('index', 'N', '{:0>4d}'),
        ],
        'send_param_len': False,
        'res_start': 10,

        'res_matrix':  [
            ('index', 0, 4, 'N'),
            ('process_code', 4, 3, 'A'),
            ('card_code', 7, 3, 'A'),
            ('card_name', 10, 16, 'A'),
            ('instaments', 26, 2, 'N'),
            ('terminal_id', 28, 8, 'N'),
        ]
    },

    'PRI': {
        'method': 'pos_execute',
        'cmd': 'PRI',
        'cmd_args': [
        ],
        'res_start': 5,

        'res_matrix':  [
            ('code', 0, 3, 'N'),
            ('last_digits', 3, 4, 'A'),
            ('first_digits', 7, 6, 'A'),
            ('terminal_id', 13, 8, 'N'),
        ]
    },

}
