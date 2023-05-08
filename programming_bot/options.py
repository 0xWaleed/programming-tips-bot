import optparse

p = optparse.OptionParser()
p.add_option("--topic", type=str)
p.add_option("--language", type=str)


def app_options_parse():
    options, arguments = p.parse_args()

    if options.topic is None:
        raise ValueError("topic is required")

    if options.language is None:
        raise ValueError("language is required")



    return options

