"""
TODO: DOC
"""
import elasticsearch


def prepare_cli(parser):
    """
    TODO: DOC
    """
    master_subparsers = parser.add_subparsers()
    
    master_elasticsearch_subparser = master_subparsers.add_parser("elasticsearch", help=elasticsearch.__doc__)
    elasticsearch.prepare_cli(master_elasticsearch_subparser)
