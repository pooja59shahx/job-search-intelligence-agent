from config_loader import load_search_keywords


def get_all_keywords():
    config = load_search_keywords()

    keywords = []

    for group in [
        "tier_1",
        "tier_2",
        "adjacent",
        "graduate_search",
    ]:
        keywords.extend(config.get(group, []))

    return keywords
