def initialize(context):
    g.security = '600519.SS'
    set_universe([g.security])


def handle_data(context, data):
    df = get_history(10, '1m', ['open', 'high', 'low', 'close', 'volume'],
                     [g.security], fq=None, include=False)
    log.info(df)
